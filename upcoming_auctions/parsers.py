from typing import List
import re 
from bs4 import BeautifulSoup

from upcoming_auctions.interfaces import AuctionEvent, ScrapperResult, SfiAuctionItemDetails

def parse_online_sell(item) -> List[AuctionEvent]:
    auction_items = []
    heading = item.get_text(strip=True)
    data = item.parent.find_next_siblings('p')[0].contents
    try:
        summary = data[0].contents[1]
        date = data[2].contents[1]
        address = None
    except IndexError:
        summary = date = None

    try:
        hdnNumLicit = data[4].contents[1].attrs['onclick'].split("'")[1]
        hdnSgComissao = data[4].contents[1].attrs['onclick'].split("'")[3]
        hdnNumTipoVenda = data[4].contents[1].attrs['onclick'].split("'")[5]
        edital = None
    except (IndexError, AttributeError):
        hdnNumLicit = hdnSgComissao = hdnNumTipoVenda = None

    auction_items.append(AuctionEvent(
            heading=heading,
            summary=summary,
            date=date,
            address=address,
            hdnNumLicit=hdnNumLicit,
            hdnSgComissao=hdnSgComissao,
            hdnNumTipoVenda=hdnNumTipoVenda,
            edital=edital
        ))
    
    return auction_items

def parse_open_bidding(item) -> List[AuctionEvent]:
    auction_items = []
    heading = item.get_text(strip=True)
    try:
        first_sibling = item.parent.find_next_siblings('p')[0].get_text(strip=True)
        summary = first_sibling.split("Tipos de imóveis:")[1].split("Dados do leilão:")[0].strip()
        date = first_sibling.split('Dados do leilão:')[1].split('Endereço:')[0].split('Data:')[1].strip()
        address = first_sibling.split('Dados do leilão:')[1].split('Endereço:')[1].strip()
    except IndexError:
        summary = date = address = None

    try:
        second_sibling = item.parent.find_next_siblings('p')[1]
        hdnNumLicit = second_sibling.contents[1].attrs['onclick'].split("'")[1]
        hdnSgComissao = second_sibling.contents[1].attrs['onclick'].split("'")[3]
        hdnNumTipoVenda = second_sibling.contents[1].attrs['onclick'].split("'")[5]
        edital = second_sibling.contents[3].attrs['onclick'].split("'")[1]
    except (IndexError, AttributeError):
        hdnNumLicit = hdnSgComissao = hdnNumTipoVenda = edital = None

    auction_items.append(AuctionEvent(
            heading=heading,
            summary=summary,
            date=date,
            address=address,
            hdnNumLicit=hdnNumLicit,
            hdnSgComissao=hdnSgComissao,
            hdnNumTipoVenda=hdnNumTipoVenda,
            edital=edital
        ))
    
    return auction_items

def parse_sfi_auction(item) -> List[AuctionEvent]:
    auction_items = []
    heading = item.get_text(strip=True)
    try:
        first_sibling = item.parent.find_next_siblings('p')[0].get_text(strip=True)
        summary = first_sibling.split("Tipos de imóveis:")[1].split("Dados do leilão:")[0].strip()
        date = first_sibling.split('Dados do leilão:')[1].split('Endereço:')[0].split('Data:')[1].strip()
        address = first_sibling.split('Dados do leilão:')[1].split('Endereço:')[1].strip()
    except IndexError:
        summary = date = address = None

    try:
        second_sibling = item.parent.find_next_siblings('p')[1]
        hdnNumLicit = second_sibling.contents[1].attrs['onclick'].split("'")[1]
        hdnSgComissao = second_sibling.contents[1].attrs['onclick'].split("'")[3]
        hdnNumTipoVenda = second_sibling.contents[1].attrs['onclick'].split("'")[5]
        edital = second_sibling.contents[3].attrs['onclick'].split("'")[1]
    except (IndexError, AttributeError):
        hdnNumLicit = hdnSgComissao = hdnNumTipoVenda = edital = None

    auction_items.append(AuctionEvent(
            heading=heading,
            summary=summary,
            date=date,
            address=address,
            hdnNumLicit=hdnNumLicit,
            hdnSgComissao=hdnSgComissao,
            hdnNumTipoVenda=hdnNumTipoVenda,
            edital=edital
        ))
    
    return auction_items

def parse_auction_items(event: BeautifulSoup) -> List[str]:
    all_ids = []
    for input_tag in event:
        if input_tag != ' ' and input_tag.get('value') and 'hdnImov' in input_tag.get('id'):
            ids = input_tag['value'].split('||')
            all_ids.extend(ids)
    return all_ids

def parse_sfi_auction_item_details(acc: ScrapperResult, event: BeautifulSoup):
    heading = event.find('h5').get_text(strip=True)
    content = event.find('div', {'class': 'content'})
    type_ = content.find('span').find_next('strong').get_text(strip=True)
    avaliation_value = content.find('p').get_text(strip=True).split('R$')[1].split('V')[0]
    min_sale_value_1st_auction = content.find('p').get_text(strip=True).split('R$')[2].split('V')[0]
    min_sale_value_2nd_auction = content.find('p').get_text(strip=True).split('R$')[3].split('V')[0]
    city = content.find(string="Comarca: ").parent.find('strong').get_text(strip=True).split('-')[0]
    estate = content.find(string="Comarca: ").parent.find('strong').get_text(strip=True).split('-')[1]
    description = event.find(string="Descrição:").parent.parent.get_text(strip=True).split('Descrição:')[1].split('.')[0]
    
    return SfiAuctionItemDetails(
        name=heading,
        type=type_,
        avaliation_value=parse_string_to_float(avaliation_value),
        first_auction_value=parse_string_to_float(min_sale_value_1st_auction),
        second_auction_value=parse_string_to_float(min_sale_value_2nd_auction),
        city=city,
        state=estate,
        description=description
    )

def parse_string_to_float(string: str) -> float:
    return float(re.sub(r'[^\d,]', '', string).replace(',', '.'))
    

    