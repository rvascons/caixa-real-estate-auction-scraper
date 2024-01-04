from fastapi import FastAPI
from httpx import AsyncClient, AsyncHTTPTransport
from asyncio import Semaphore, create_task, gather

from upcoming_auctions.services import sort_auction_events, set_starting_cookies, get_auction_event_items, get_auction_item_details_and_sort
from upcoming_auctions.interfaces import ScrapperResult
from interfaces import BrazilianState

app = FastAPI()

@app.get("/caixa/upcoming/{state}")
async def get_upcoming(state: BrazilianState):

    client = AsyncClient(timeout=240, transport=AsyncHTTPTransport(retries=3))
    data = ScrapperResult()
    await set_starting_cookies(client)
    events = await sort_auction_events(str(state.value), client)
    
    semaphore = Semaphore(20)
    tasks = []

    for event in events:
        ids = await get_auction_event_items(event, client)
        for id in ids:
            await semaphore.acquire()
            task = create_task(get_auction_item_details_and_sort(data, id, event, client))
            task.add_done_callback(lambda t: semaphore.release())
            tasks.append(task)

    await gather(*tasks)
    return data
