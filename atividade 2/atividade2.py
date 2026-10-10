from datetime import datetime, timedelta
import requests

def cotar_dia(data):
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json"
    res = requests.get(url)
    res = res.json()
    
    if res['value']:
        return res['value'][0]['cotacaoCompra']
    else:
        
        data_obj = datetime.strptime(data, "%m-%d-%Y") - timedelta(days=1)
        data_anterior = datetime.strftime(data_obj, "%m-%d-%Y")
        return cotar_dia(data_anterior)

def cotar():
    
    cotacoes = []
    data_atual = datetime.now()
    
    for i in range(365):
        dia_alvo = data_atual - timedelta(days=i)
        data_formatada = datetime.strftime(dia_alvo, "%m-%d-%Y")
        
        valor_cotacao = cotar_dia(data_formatada)
        cotacoes.append(float(valor_cotacao))
        
    return cotacoes