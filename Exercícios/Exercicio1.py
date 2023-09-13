
def tabuada(tab):
    x = tab
    y = 0
    while y <= 10:
        print(f'{x} X {y} = {x*y}')
        y += 1
def cab():
    print("Bem vindo! Por favor, siga as instruções abaixo:")
    user = str(input("Digite seu nome: "))
    print(f'Bem vindo {user}.')

def chama_tab():
    tab = int(input("Qual tabuada você quer? "))
    print(tab)
    tabuada(tab)

def finalizar():
    print("Deseja usar novamente?")

    restart = int(input("(1) Sim - (2) Não"))

    while restart == 1:
        chama_tab()

def principal():
    cab()
    chama_tab()
    finalizar()


if(__name__ == "__main__"):
    principal()
