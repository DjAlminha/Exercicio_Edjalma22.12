import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv (r'S:\COM\Human_Resources\01.Engineering_Tech_School\02.Internal\10 - Aprendizes\5 - Desenvolvimento de Sistemas\Arquivos a serem disponibilizados\exercicioedjalma.csv')
df.columns=['data']
lista = df['data'].str.split('/',n=3,expand=True)
df['dia'] = lista[0]
df['mes'] = lista[1]
df['ano'] = lista[2]

print("O que você deseja fazer? ")
print("[1] gráfico de dia")
print("[2] gráfico de mês")
print("[3] gráfico de ano")
op = int(input())

df_dia = df.groupby(['dia']).size().reset_index(name="Quantidade dias")
df_mes = df.groupby(['mes']).size().reset_index(name="Quantidade meses")
df_ano = df.groupby(['ano']).size().reset_index(name="Quantidade anos")
if(op == 1):
    plt.figure(figsize=(20, 10))
    plt.plot(df_dia['dia'],df_dia['Quantidade dias'])
    plt.xticks(rotation='vertical')
    plt.title('Quantidade por dia')
    plt.show()

    
elif(op == 2):
    plt.figure(figsize=(20, 10)) 
    plt.plot(['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'],df_mes['Quantidade meses'])
    plt.xticks(rotation='vertical')
    plt.title('Quantidade por mes')
    plt.show()

elif(op == 3): 
    plt.figure(figsize=(20, 10)) 
    plt.plot(df_ano['ano'],df_ano['Quantidade anos'])
    plt.xticks(rotation='vertical')
    plt.title('Quantidade por ano')
    plt.show()
else:
    print("Erro")
    





