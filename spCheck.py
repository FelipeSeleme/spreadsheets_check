import pandas as pd

# configurações de exibição do pd:
pd.set_option('display.width', 1080)
pd.set_option('display.max_columns', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# leitura das planilhas a serem conciliadas:
df_financeiro = pd.read_excel(r'Conciliacao.xlsx', sheet_name="Financeiro")
df_contabil = pd.read_excel(r'Conciliacao.xlsx', sheet_name="Contábil")

# filtro das colunas a serem utilizadas:
df_financeiro = df_financeiro[['TITULO', 'REDUZIDO', 'VAL_ATUAL']].round(2)
df_contabil = df_contabil[['Documento', 'Reduzido', 'Valor']].round(2)

# criação das chaves financeiras e contábeis (índices):
for indice in df_financeiro.index:
    df_financeiro.loc[indice, 'CHAVE'] = \
        f"{str(df_financeiro.loc[indice, 'REDUZIDO'])}/{str(df_financeiro.loc[indice, 'TITULO'])}"
for indice in df_contabil.index:
    df_contabil.loc[indice, 'CHAVE'] = \
        f"{str(df_contabil.loc[indice, 'Reduzido'])}/{str(df_contabil.loc[indice, 'Documento'])}"

# agrupamento dos valores por chave:
df_valor_fin = df_financeiro[['CHAVE', 'VAL_ATUAL']].groupby('CHAVE').sum()
df_valor_con = df_contabil[['CHAVE', 'Valor']].groupby('CHAVE').sum()

# mesclagem dos valores das planilhas conforme as chaves:
df_concilia = df_valor_fin.merge(df_valor_con, how='outer', on='CHAVE')\
    .rename(columns={'VAL_ATUAL': 'Financeiro', 'Valor': 'Contabil'}).round(2)

# cálculo das diferenças entre os valores totais das chaves:
for chave in df_concilia.index:
    df_concilia.loc[chave, 'Diferenca'] = df_concilia.loc[chave, 'Financeiro'] + df_concilia.loc[chave, 'Contabil']
df_concilia = df_concilia.round(2)
print(df_concilia)

# exportação do resultado para arquivo Excel:
df_concilia.to_excel('Resultado.xlsx')
