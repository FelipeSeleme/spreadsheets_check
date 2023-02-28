# spreadsheets_check
This code reads and compares the values between spreadsheets in the financial and accounting sectors of a company.
  
The problem was that the accounting entries needed to be checked against the financial realized in large amounts. Also, 
the data did not have any kind of primary key. The amounts could occur in fractions, spread across different cost centers, 
with no direct relationship between the data in the two spreadsheets. It was necessary to group accounts by sector, 
create a key, calculate totals and differences, then return a third consolidated spreadsheet.  
  
_Spreadsheets .info:_  
~~~
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 108542 entries, 0 to 108541
Data columns (total 30 columns):
 #   Column           Non-Null Count   Dtype         
---  ------           --------------   -----         
 0   FIL              108542 non-null  int64         
 1   TC               108542 non-null  object        
 2   EMISSAO          108542 non-null  datetime64[ns]
 3   COMPET_INICIAL   107407 non-null  datetime64[ns]
 4   COMPET_FINAL     107486 non-null  datetime64[ns]
 5   VENC             108542 non-null  datetime64[ns]
 6   TITULO           108542 non-null  object        
 7   COD_REFERENCIA   108503 non-null  object        
 8   TD               108542 non-null  object        
 9   ST               108542 non-null  object        
 10  SIT              108542 non-null  int64         
 11  LIQUIDACAO       41718 non-null   datetime64[ns]
 12  CANCELAMENTO     16 non-null      datetime64[ns]
 13  CLIENTE          108542 non-null  int64         
 14  NOME             108542 non-null  object        
 15  CNPJ             108542 non-null  int64         
 16  VALOR            108542 non-null  float64       
 17  IMP_FAT          389 non-null     object        
 18  VAL_IRRF         108542 non-null  float64       
 19  VAL_LIQUIDO_NDO  108542 non-null  float64       
 20  RECEBIDO         108542 non-null  float64       
 21  OUTRAS_BAIXAS    108542 non-null  int64         
 22  IMP_RETIDO       108542 non-null  float64       
 23  VAL_ATUAL        108542 non-null  float64       
 24  NDO              108542 non-null  object        
 25  OPER             108542 non-null  object        
 26  COD_VERSAO       108542 non-null  int64         
 27  COD_CONTA        108542 non-null  object        
 28  REDUZIDO         108542 non-null  int64         
 29  DESCRICAO        108542 non-null  object        
dtypes: datetime64[ns](6), float64(6), int64(7), object(11)
memory usage: 24.8+ MB
~~~
  
~~~
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 82088 entries, 0 to 82087
Data columns (total 19 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   Data            81967 non-null  datetime64[ns]
 1   Filial          81967 non-null  float64       
 2   Lanc            81967 non-null  float64       
 3   Complemento     81967 non-null  object        
 4   Conta Auxiliar  81981 non-null  object        
 5   Documento       82077 non-null  object        
 6   Débito          81717 non-null  object        
 7   Crédito         474 non-null    object        
 8   Valor           82082 non-null  object        
 9   Parcial         958 non-null    object        
 10  Fiscal ou ANS   13273 non-null  object        
 11  Nome            82001 non-null  object        
 12  CPF / CNPJ      81946 non-null  object        
 13  Vencimento      81967 non-null  object        
 14  Reduzido        81967 non-null  float64       
 15  Estendida       81967 non-null  object        
 16  ANS             81967 non-null  float64       
 17  Idade de Saldo  81967 non-null  object        
 18  Tipo            10307 non-null  object        
dtypes: datetime64[ns](1), float64(4), object(14)
memory usage: 11.9+ MB
~~~
