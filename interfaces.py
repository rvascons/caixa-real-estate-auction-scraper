from enum import Enum
from pydantic import BaseModel
from typing import Optional

class BrazilianState(Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"
class AuctionItem(BaseModel):
    heading: str
    summary: Optional[str]
    date: Optional[str]
    address: Optional[str]
    hdnNumLicit: Optional[str]
    hdnSgComissao: Optional[str]
    hdnNumTipoVenda: Optional[str]
    edital: Optional[str]