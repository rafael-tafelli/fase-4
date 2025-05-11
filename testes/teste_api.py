import requests

# Pegando histórico de preços
vEndPoint = 'http://localhost:8000/api/historico_preco'
vPayload = {
    'acao': 'PETR4.SA',
    'data_inicio': '2023-01-01',
    'data_fim': '2023-01-05'
}

vResponse = requests.post(vEndPoint, json=vPayload)
print('Historico de Preços\n')
print(vResponse.json())
print('----------------------------------')


# Prevendo preços
vEndPoint = 'http://localhost:8000/api/predict'
vPayload = {
    'precos_anteriores': [1, 2, 3, 4, 5]
}

vResponse = requests.post(vEndPoint, json=vPayload)
print('Previsão de Preços\n')
print(vResponse.json())
print('----------------------------------')