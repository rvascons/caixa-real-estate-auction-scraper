from pydantic import BaseModel
from typing import Optional

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