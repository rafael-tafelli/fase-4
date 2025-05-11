import requests
import pandas as pd
from datetime import datetime

# Definir o endpoint da API
vEndPoint = 'http://localhost:8000/api/historico_preco'

# Pegando histórico de preços
vBase = pd.DataFrame()
vListaAcoes = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']
for acao in vListaAcoes:
    vPayload = {
        'acao': acao,
        'data_inicio': '2023-01-01',
        'data_fim': '2023-01-05'
    }

    vResponse = requests.post(vEndPoint, json=vPayload)

    if vResponse.status_code == 200:
        vBase_Json = vResponse.json()
        vBaseTemp = pd.DataFrame(vBase_Json)
        vBase = pd.concat([vBase, vBaseTemp], ignore_index=True)


# Tratando valores nulos
vBase.fillna(0, inplace=True)

# Convertendo a coluna 'Date' para o formato datetime
vBase['Date'] = pd.to_datetime(vBase['Date'])

# Exportar para CSV
vBase.to_csv(fr'saida_historico_csv\historico_precos_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv', index=False)