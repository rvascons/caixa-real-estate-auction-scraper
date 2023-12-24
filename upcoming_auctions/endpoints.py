from httpx import AsyncClient
from upcoming_auctions.interfaces import EventListParameters
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

async def get_auction_items(params: EventListParameters, client: AsyncClient) -> str:
    url = "https://venda-imoveis.caixa.gov.br/sistema/carregaPesquisaImoveisLicitacoes.asp"
    payload = "NumLicit={}&SgComissao={}&NumTipoVenda={}".format(params.hdnNumLicit, params.hdnSgComissao, params.hdnNumTipoVenda)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://venda-imoveis.caixa.gov.br',
        'Connection': 'keep-alive',
        'Referer': 'https://venda-imoveis.caixa.gov.br/sistema/busca-imovel.asp?hdnOrigem=licitacoes',
        'Cookie': '__uzma=6c920056-3eed-4e15-bc96-05a69383043e; __uzmb=1702920503; __uzme=5926; __uzmc=335291615091368; __uzmd=1703088548; ASPSESSIONIDQASRACDQ=OKPHJCIDFKFIPMLPGBMGGMNF; ARRAffinity18=80c156797a9be6fdd56ce2ad7df9a55c4a765a0d73acd743906dcb39a17ffd54; _ga_PD5EBJFQ7X=GS1.1.1703088508.11.1.1703088548.0.0.0; _gcl_au=1.1.1581796920.1702920736; _ga=GA1.1.1188126861.1702920737; _ga_RD3F5P2Z1Q=GS1.3.1702920736.1.1.1702922145.60.0.0; AdoptVisitorId=BwVgbMCcDGkEwFoCGATADAMwQFmwRhQUiQGYwExowMC44Q4AjOIA; _ga=GA1.4.1188126861.1702920737; ASPSESSIONIDQQRCCRQD=LMMDCBKDFGBCKOABFPOCIAJC; ARRAffinity19=ad91cb854ad7447e57d11395e878f131973f2b51c1c83aa7df0fbae4066a198d; ASPSESSIONIDCCBAADBQ=JINJFOEAJDMIFHLECGHCNABB; ASPSESSIONIDQADSARTC=NDNJOMGAIAKNFENFKJDCJMHI; ASPSESSIONIDSASQABBS=DDOFEKBBPGMFOHPKCLAFPLKA; ASPSESSIONIDQQBQBSQD=PNDJNIDBPBCOHDAJAAAHPNDO; cptjxgKx3iXPAw1X=v1NFLQgwSDQkn; _gid=GA1.4.1222446698.1703088513; __uzma=614eb2de-8aa0-4aa7-9896-5827b20521ee; __uzmb=1702921859; __uzmc=726171615327468; __uzmd=1703089584; __uzme=9598',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    response = await client.request("POST", url, headers=headers, data=payload)
    return response