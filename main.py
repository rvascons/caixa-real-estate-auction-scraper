from interfaces import BrazilianState
from fastapi import FastAPI
from httpx import AsyncClient
from upcoming_auctions.services import sort_auction_events, set_starting_cookies, get_auction_event_items

app = FastAPI()

@app.get("/caixa/upcoming/{state}")
async def get_upcoming(state: BrazilianState):
    client = AsyncClient(timeout=30.0)
    await set_starting_cookies(client)
    events = await sort_auction_events(str(state.value), client)
    for event in events:
        event.ids = await get_auction_event_items(event, client)

    return events