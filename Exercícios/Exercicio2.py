def chama_conv(coin, qtd):
    if coin == 1:
        y = 5.19
        x = qtd
        print(f'Você pode comprar € {x * y}.')
    elif coin == 2:
        y = 4.87
        x = qtd
        print(f'Você pode comprar US$ {x * y}.')
    elif coin == 3:
        y = 6.03
        x = qtd
        print(f'Você pode comprar £$ {x * y}.')

def finalizar(coin, qtd):
    print("Deseja usar novamente?")

    restart = int(input("(1) Sim - (2) Não"))

    if restart == 1:
        chama_conv(coin, qtd)
    else:
        print("Obrigado por utilizar")

def principal():
    print("*** Bem Vindo ao seu Conversor de Moedas ***")
    user = str(input("Digite seu nome: "))
    print(f'Bem vindo {user.title()}.')

    qtd = float(input("Quanto você tem? R$"))

    print(f'Você tem R$ {qtd}.')

    print("Qual moeda você quer comprar?")
    coin = int(input("(1): Euro - (2): Dólar - (3): Libra"))
    chama_conv(coin, qtd)

    
if(__name__ == "__main__"):
    principal()

