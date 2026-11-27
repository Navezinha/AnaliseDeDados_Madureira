import pandas as pd 

idades_lista = [25, 30, 22, 28]

idades_series = pd.Series([25, 30, 22,  28])

print(f"Lista: \n{idades_lista}\n")
print(f"Series: \n{idades_series}")

notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])
print(notas['Maria']) #acessando a nota de Maria pelo rótulo
print(notas.iloc[2]) #acessando notas de Pedro pela posição
print(notas.mean()) #calculando a média das notas
print(notas[notas>8]) #filtrando notas maiores qe 8
print(notas.describe()) #estatística descritiva das notas

#Operações aritméticas e entre duas séries
#aumentar todas as notas em 10% de uma vez só
notasAjustadas = notas * 1.10
print(notasAjustadas)

#Comparar com uma segunda séries
notas_exame_final = pd.Series([10, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana'])
diferenca = notas_exame_final - notasAjustadas

print(diferenca)

#dataFrames: Lendo planilhas excel

df = pd.read_excel('base_invest.xlsx') #Lê a planilha Excel da pasta
print(df.head()) #Exibe as 5 primeiras linhas

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

print(df_transacoes.head())
print(df_ativo.head())

