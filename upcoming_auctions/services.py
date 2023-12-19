from httpx import AsyncClient
from bs4 import BeautifulSoup
from typing import List

from interfaces import AuctionItem
async def get_bidding_page(client: AsyncClient):
    url = "https://venda-imoveis.caixa.gov.br/sistema/busca-licitacoes.asp?sltTipoBusca=licitacoes"
    headers = {
        'Cookie': 'ARRAffinity18=ad91cb854ad7447e57d11395e878f131973f2b51c1c83aa7df0fbae4066a198d; ASPSESSIONIDQQRCCRQD=OGJCCBKDGAIALMCCKKHBMMOF; __uzma=614eb2de-8aa0-4aa7-9896-5827b20521ee; __uzmb=1702921859; __uzmc=722432284436; __uzmd=1702922419; __uzme=9598; cptjxgKx3iXPAw1X=v1NVLQgwSDOzb'
    }
    response = await client.get(url, headers=headers)
    return response

async def list_biddings(state: str, client: AsyncClient) -> str:
    url = "https://venda-imoveis.caixa.gov.br/sistema/carregaListaLicitacoes.asp"
    payload = "cmb_estado={}".format(state)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://venda-imoveis.caixa.gov.br',
        'Connection': 'keep-alive',
        'Referer': 'https://venda-imoveis.caixa.gov.br/sistema/busca-licitacoes.asp?sltTipoBusca=licitacoes',
        'Cookie': '__uzma=6c920056-3eed-4e15-bc96-05a69383043e; __uzmb=1702920503; __uzme=5926; __uzmc=971102545631; __uzmd=1702922158; ASPSESSIONIDQASRACDQ=OKPHJCIDFKFIPMLPGBMGGMNF; ARRAffinity18=80c156797a9be6fdd56ce2ad7df9a55c4a765a0d73acd743906dcb39a17ffd54; _ga_PD5EBJFQ7X=GS1.1.1702920077.10.1.1702922160.0.0.0; _gcl_au=1.1.1581796920.1702920736; _ga=GA1.1.1188126861.1702920737; _gid=GA1.3.1029848143.1702920737; _ga_RD3F5P2Z1Q=GS1.3.1702920736.1.1.1702922145.60.0.0; AdoptVisitorId=BwVgbMCcDGkEwFoCGATADAMwQFmwRhQUiQGYwExowMC44Q4AjOIA; _ga=GA1.4.1188126861.1702920737; _gid=GA1.4.1029848143.1702920737; cptjxgKx3iXPAw1X=v1NVLQgwSDOzb; ARRAffinity18=ad91cb854ad7447e57d11395e878f131973f2b51c1c83aa7df0fbae4066a198d; ASPSESSIONIDQQRCCRQD=OGJCCBKDGAIALMCCKKHBMMOF; __uzma=614eb2de-8aa0-4aa7-9896-5827b20521ee; __uzmb=1702921859; __uzmc=294522825662; __uzmd=1702923017; __uzme=9598',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    response = await client.post(url, headers=headers, data=payload)
    return response

'''
<span>
        <h5>Leilão SFI - Edital Único 0029/0223 - CPA/RE - AC</h5>
</span>
<p><span><strong>Tipos de imóveis: </strong>Casas - 114, Apartamentos - 173, Outros - 9</span><br /><span><strong>Dados
                        do leilão: </strong>Data: 18/01/2024 às 10:00hs. Endereço: www.hammer.lel.br</span></p>
<p class="action"> <a class="submit-d submit-white submit-small" href="#"
                onclick="javascript:ListarEdital('00290223','CPA/RE','14')"
                title="Listar todos os imóveis deste edital">Listar todos os imóveis deste edital</a> <a
                class="submit-d submit-white submit-small" href="#"
                onclick="javascript:ExibeDoc('/editais/EL00290223CPARE.PDF')">Baixar edital e anexos</a><br /><span
                style="font-size:0.7em;">(Data do arquivo: 15/12/2023 09:51:36)</span></p><br>
<hr /><br><span>
        <h5>Leilão SFI - Edital Único 0032/0223 - CPA/RE - AC</h5>
</span>
<p><span><strong>Tipos de imóveis: </strong>Casas - 170, Apartamentos - 124, Outros - 2</span><br /><span><strong>Dados
                        do leilão: </strong>Data: 24/01/2024 às 10:00hs. Endereço: www.mgl.com.br</span></p>
<p class="action"> <a class="submit-d submit-white submit-small" href="#"
                onclick="javascript:ListarEdital('00320223','CPA/RE','14')"
                title="Listar todos os imóveis deste edital">Listar todos os imóveis deste edital</a> <a
                class="submit-d submit-white submit-small" href="#"
                onclick="javascript:ExibeDoc('/editais/EL00320223CPARE.PDF')">Baixar edital e anexos</a><br /><span
                style="font-size:0.7em;">(Data do arquivo: 18/12/2023 11:06:23)</span></p><br>
<hr /><br>
'''
def parse_auction_data(html_content: str) -> List[AuctionItem]:
    soup = BeautifulSoup(html_content, 'html.parser')
    auction_items = []

    for item in soup.find_all('h5'):
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

        auction_items.append(AuctionItem(
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