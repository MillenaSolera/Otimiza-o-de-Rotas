import pandas as pd

# Define warehouses
centros_distribuicao = pd.DataFrame({
    'Centro_ID': ['Belém', 'Recife', 'São Paulo', 'Curitiba'],
    #'Capacidade_Armazenagem (t)': [200, 300, 500, 400],
    #'Endereco': ['Belém, PA', 'Recife, PE', 'São Paulo, SP', 'Curitiba, PR']
})


# Define 30 trucks
caminhoes = pd.DataFrame({
    'Caminhao_ID': [f'C{str(i).zfill(3)}' for i in range(1, 31)],
    'Centro_Distribuicao': ['Belém']*8 + ['Recife']*7 + ['São Paulo']*8 + ['Curitiba']*7,
    'Capacidade_Ton': [10, 12, 8, 15, 10, 11, 13, 9, 10, 12, 8, 15, 10, 11, 13, 9, 10, 12, 8, 15, 
                       10, 11, 13, 9, 10, 12, 8, 15, 10, 11],
    'Items_Carregados': [[] for _ in range(30)], # Lista de 30 listas vazias

    # Aqui consideraremos apenas os Kms não as horas considerando que os caminhões terão uma velocidade média
    # Aplicaremos o algoritmo TSP aos nós de entrega

    'Distancia_Servico': [value * 300 for value in [10, 12, 8, 15, 10, 11, 13, 9, 10, 12, 8, 15, 10, 11, 13, 9, 10, 12, 8, 15, 
                       10, 11, 13, 9, 10, 12, 8, 15, 10, 11]]

    
})

cidades_brasil = [
    {'cidade': 'São Paulo', 'coordenadas': '-23.5505, -46.6333'},
    {'cidade': 'Curitiba', 'coordenadas': '-25.4296, -49.2718'},
    {'cidade': 'Recife', 'coordenadas': '-8.0476, -34.8770'},
    {'cidade': 'Belém', 'coordenadas': '-1.4558, -48.4909'},

    {'cidade': 'Rio de Janeiro', 'coordenadas': '-22.9068, -43.1729'},
    {'cidade': 'Belo Horizonte', 'coordenadas': '-19.9191, -43.9386'},
    {'cidade': 'Salvador', 'coordenadas': '-12.9714, -38.5014'},
    {'cidade': 'Brasília', 'coordenadas': '-15.7801, -47.9292'},
    {'cidade': 'Fortaleza', 'coordenadas': '-3.7172, -38.5437'},
    {'cidade': 'Porto Alegre', 'coordenadas': '-30.0346, -51.2177'},
    {'cidade': 'Manaus', 'coordenadas': '-3.1190, -60.2449'},
    {'cidade': 'Goiânia', 'coordenadas': '-16.6869, -49.2648'},
    {'cidade': 'Campinas', 'coordenadas': '-23.1857, -46.8978'},
    {'cidade': 'São Luís', 'coordenadas': '-2.5387, -44.2827'},
    {'cidade': 'Natal', 'coordenadas': '-5.7945, -35.2110'},
    {'cidade': 'Maceió', 'coordenadas': '-9.6658, -35.7350'},
    {'cidade': 'Teresina', 'coordenadas': '-5.0891, -42.8034'},
    {'cidade': 'Aracaju', 'coordenadas': '-10.9472, -37.0731'},
    {'cidade': 'João Pessoa', 'coordenadas': '-7.1195, -34.8450'},
    {'cidade': 'Uberlândia', 'coordenadas': '-18.9121, -48.2750'},
    {'cidade': 'Ribeirão Preto', 'coordenadas': '-21.1773, -47.8103'},
    {'cidade': 'Bauru', 'coordenadas': '-22.3145, -49.0604'},
    {'cidade': 'Blumenau', 'coordenadas': '-26.9194, -49.0673'},
    {'cidade': 'Vitória', 'coordenadas': '-20.3155, -40.3128'},
    {'cidade': 'Caxias do Sul', 'coordenadas': '-29.1707, -51.1797'},
    {'cidade': 'Sorocaba', 'coordenadas': '-23.5012, -47.4581'},
    {'cidade': 'Diadema', 'coordenadas': '-23.6856, -46.5654'},
    {'cidade': 'Juiz de Fora', 'coordenadas': '-21.7655, -43.3487'},
    {'cidade': 'Franca', 'coordenadas': '-20.5380, -47.5163'},
    {'cidade': 'São Bernardo do Campo', 'coordenadas': '-23.6820, -46.5642'},
    {'cidade': 'São José dos Campos', 'coordenadas': '-23.1896, -45.8989'},
    {'cidade': 'Niterói', 'coordenadas': '-22.8830, -43.1033'},
    {'cidade': 'Porto Velho', 'coordenadas': '-8.7610, -63.9039'},
    {'cidade': 'Macapá', 'coordenadas': '0.0340, -51.0694'},
    {'cidade': 'Boa Vista', 'coordenadas': '2.8231, -60.6753'},
    {'cidade': 'São João de Meriti', 'coordenadas': '-22.8071, -43.4000'}
]
