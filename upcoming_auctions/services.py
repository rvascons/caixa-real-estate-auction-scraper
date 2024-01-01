from bs4 import BeautifulSoup
import time 
from typing import List
from upcoming_auctions.parsers import parse_online_sell, parse_sfi_auction, parse_open_bidding, parse_auction_items, parse_sfi_auction_item_details
from upcoming_auctions.endpoints import get_bidding_page, list_biddings, get_auction_items, get_auction_item_details
from upcoming_auctions.interfaces import AuctionEvent, EventListParameters, ScrapperResult
from httpx import AsyncClient

async def set_starting_cookies(client: AsyncClient) -> None:
    await get_bidding_page(client)

async def sort_auction_events(state: str, client: AsyncClient) -> List[AuctionEvent]:
    response = await list_biddings(state, client)
    soup = BeautifulSoup(response, 'html.parser')
    auction_events = []

    for item in soup.find_all('h5'):
        heading = item.get_text(strip=True)
        if 'Venda Online' in heading:
            auction_events.extend(parse_online_sell(item))
        elif 'Leilão SFI' in heading:
            auction_events.extend(parse_sfi_auction(item))
        elif 'Licitação Aberta' in heading:
            auction_events.extend(parse_open_bidding(item))

    return auction_events

async def get_auction_event_items(auction_event: AuctionEvent, client: AsyncClient) -> List[str]:
    event_params: EventListParameters = EventListParameters(
        hdnNumLicit=auction_event.hdnNumLicit,
        hdnSgComissao=auction_event.hdnSgComissao,
        hdnNumTipoVenda=auction_event.hdnNumTipoVenda
    )
    response = await get_auction_items(event_params, client)
    soup = BeautifulSoup(response, 'html.parser')
    auction_items = parse_auction_items(soup)
    return auction_items
    
async def get_auction_item_details_and_sort(data: ScrapperResult, id: str, event: AuctionEvent, client: AsyncClient) -> BeautifulSoup:
    response = await get_auction_item_details(id, client)
    item_details = BeautifulSoup(response, 'html.parser')
    # Online Sell
    if event.hdnNumTipoVenda == '33':
        pass
    # Open Bidding
    elif event.hdnNumTipoVenda == '21':
        pass
    # SFI Auction
    elif event.hdnNumTipoVenda == '14':
        result = parse_sfi_auction_item_details(data, item_details)
        data.sfi_auction_items.append(result)