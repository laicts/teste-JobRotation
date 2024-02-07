import json

def calcular_faturamento(valor_faturamento):
    valor_faturamento = [faturamento for faturamento in valor_faturamento if faturamento > 0]
    menor_faturamento = min(valor_faturamento)
    maior_faturamento = max(valor_faturamento)
    
    media = sum(valor_faturamento) / len(valor_faturamento)
    dias_acima_da_media = sum(1 for faturamento in valor_faturamento if faturamento > media)

    return menor_faturamento, maior_faturamento, dias_acima_da_media


with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

def dados_valor():
    valor_faturamento = [valor['valor'] for valor in dados]
    print(valor_faturamento)

menor, maior, dias_acima_media = calcular_faturamento([valor['valor'] for valor in dados])
print("Menor valor de faturamento diário:", menor)
print("Maior valor de faturamento diário:", maior)
print("Número de dias em que o faturamento foi superior à média mensal:", dias_acima_media)


faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total_mensal = sum(faturamento_por_estado.values())


percentuais_por_estado = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / valor_total_mensal) * 100
    percentuais_por_estado[estado] = percentual


for estado, percentual in percentuais_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
