from pydantic import BaseModel
from typing import Optional, List

class AuctionEvent(BaseModel):
    heading: str
    summary: Optional[str]
    date: Optional[str]
    address: Optional[str]
    hdnNumLicit: Optional[str]
    hdnSgComissao: Optional[str]
    hdnNumTipoVenda: Optional[str]
    edital: Optional[str]
    ids: Optional[list] = []

class EventListParameters(BaseModel):
    hdnNumLicit: str
    hdnSgComissao: str
    hdnNumTipoVenda: str

class SfiAuctionItemDetails(BaseModel):
    name: str
    type: str
    avaliation_value: float
    first_auction_value: float
    second_auction_value: float
    city: str
    state: str
    description: str

class OpenBiddingAuctionItemDetails(BaseModel):
    name: str
    type: str
    avaliation_value: float
    minimum_value: float
    city: str
    state: str
    description: str

class OnlineSellAuctionItemDetails(BaseModel):
    name: str
    type: str
    avaliation_value: float
    minimum_value: float
    discount: float
    city: str
    state: str
    description: str

class ScrapperResult(BaseModel):
    sfi_auction_items: List[SfiAuctionItemDetails] = []
    open_bidding_items: List[OpenBiddingAuctionItemDetails] = []
    online_sell_items: List[OnlineSellAuctionItemDetails] = []

    
