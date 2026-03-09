import pandas as pd

'''Ler e mostras as primeiras linhas do arquivo'''
df = pd.read_csv('dados_treino_pandas.csv')
df.head()

'''tipos das colunas, quantidade de valores nulos, estatísticas das colunas numéricas'''
df.info()
df.describe()

'''Mostre apenas vendas da cidade: São Paulo'''
SPloc = df.loc[df['cidade']=='São Paulo'] #ou
SPquery = df.query('cidade == "São Paulo"')

'''Crie um DataFrame contendo apenas: cliente, produto ,valor_total'''
novo_df = df.loc[:,['cliente','produto','valor_total']]

'''Descubra quantas vendas cada produto teve.'''
qtd_produtos = df['produto'].value_counts() #Conta a frequencia que cada elemento aparece na coluna;

'''Veja quantos valores nulos existem na coluna: idade'''
df['idade'].isna().sum() #isna() retorna um bool para casa celula na verificação;

'''Substitua os valores nulos da coluna idade pela média das idades.'''
#é usada para preencher, substituir ou remover valores ausentes (NaN/NaN/null) em DataFrames ou Séries
testes = df['idade'].fillna(df['idade'].mean())
print(testes.isna().sum())






