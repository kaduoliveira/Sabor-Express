import os
import time


def exibir_nome_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░'''
)

def exibir_opcao():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
    print('\n')

def finaliza_app():
    print('''
█▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀█   ▄▀█ █▀█ █▀█
█▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █░▀█ █▄▀ █▄█   █▄█   █▀█ █▀▀ █▀▀''')
    print('\n')
    #contagem_regressiva() retirei ele dessa funcção e listei ele direto na main
    #os.system('cls') coloquei esse comando dentro do contagem regressiva
    
opcao_escolhida = 1

def escolher_opcao():
    opcao_escolhida=int(input('Digite a sua opção: '))
    #opcao_escolhida = int(opcao_escolhida)
    print(f'\nVocê escolheu a opção {opcao_escolhida} \n')
    
    '''
#Código usando if elif else
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finaliza_app()
    '''
#Código usando match, lembrando que apenas é compativel a partir do python 3.1
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurante')
        case 3:
            print('Ativar restaurante')
        case 4:
            finaliza_app()
        case _:
            print('Opção inválida\n')
            escolher_opcao()

    print('\n')

def contagem_regressiva(tempo=2):
    while tempo:
        mins, secs = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end='\r') esse comando imprime o relogio de contagem regressiva
        time.sleep(1)
        tempo -= 1
    os.system("cls")

    
print('\n')

def main():
    exibir_nome_programa()
    exibir_opcao()
    escolher_opcao()
    contagem_regressiva()
        

if __name__ == '__main__':
    main()
