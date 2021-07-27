import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6a7576742d7ded03f4f87fd82d19c34c"
# Your Auth Token from twilio.com/console
auth_token  = "66e34334b0b35672ee6657aacad83f15"

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511971466854",
            from_="+14842832056",
            body=f'No mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')

        print(message.sid)


# Para cada arquivo:

# Verificar se algum valor naquele arquivo na coluna de vendas é maior que 50.000,00

# Se for maior que 55.000,00 -> Envia um SMS com o nome, mês e as vendas do vendedor

