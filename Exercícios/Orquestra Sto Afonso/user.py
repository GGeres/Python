def usuario():
    nome = input('Digite seu nome de usuário: \n')
    if str(nome) == 'Gustavo' or nome == 'Ed':
        print('Bem vindo!')
        options()
    else:print('Usuário não encontrado, tente novamente!')


def options():
    input('Escolha as opções abaixo: \n')