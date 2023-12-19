from interfaces import BrazilianState
from fastapi import FastAPI
from httpx import AsyncClient
from upcoming_auctions.services import get_bidding_page, list_biddings, parse_auction_data

app = FastAPI()

@app.get("/caixa/upcoming/{state}")
async def get_upcoming(state: BrazilianState):
    client = AsyncClient(timeout=30.0)
    await get_bidding_page(client)
    response = await list_biddings(str(state.value), client)
    return parse_auction_data(response)