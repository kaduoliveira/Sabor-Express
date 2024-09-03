import os
import time

#variaveis globais
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░'''
)

def exibir_opcao():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair')
    print('\n')

def finaliza_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    print('''
█▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀█   ▄▀█ █▀█ █▀█
█▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █░▀█ █▄▀ █▄█   █▄█   █▀█ █▀▀ █▀▀''')
    print('\n')
    #contagem_regressiva()
    os.system('cls')
    
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opcao inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls') #limpando a tela
    linha = '-' * (len(texto))
    print(f'{linha}\n{texto}\n{linha}')
    print()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante = input('\n Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f' Digite a Categoria do restaurante {nome_do_restaurante.upper()}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'\n\n O restaurante {nome_do_restaurante.upper()} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('LISTANDO RESTAURANTES')
    #código de exibição de restaurantes cadastrados
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado' #uso de ternario
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('ATIVAR RESTAURANTE')
    print('\n Restaurantes cadastrados: \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    nome_restaurante = input('\n Digite o nome do restaurante que deseja mudar o estado: ')

    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #aqui ele inverte o valor booleanodo 'ativo' na lista
            mensagem = f'\n O restaurante {nome_restaurante} foi ativado com Sucesso' if restaurante['ativo'] else f' O Restaurante {nome_restaurante} foi DESATIVADO com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('\n Restaurante não encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida=int(input('Digite a sua opção: '))
        #opcao_escolhida = int(opcao_escolhida)
        print(f'\nVocê escolheu a opção {opcao_escolhida} \n')
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finaliza_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def contagem_regressiva(tempo=1):
    '''Está função exibe um relogio em contagem regressiva'''
    while tempo:
        mins, secs = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end='\r')
        time.sleep(1)
        tempo -= 1

    
print('\n')

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcao()
    escolher_opcao()
    

if __name__ == '__main__':
    main()
