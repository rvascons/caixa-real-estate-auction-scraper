from typing import List
from bs4 import BeautifulSoup

from upcoming_auctions.interfaces import AuctionEvent

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