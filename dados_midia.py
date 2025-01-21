import os
os.system('cls')
login = []
cadastro = []
op = 0
while op != 6:
    print('1 - CADASTRAR LOGIN')
    print('2 - VER CADASTRO')
    print('3 - LISTAR CADASTRO')
    print('4 - ALTERAR CADASTRO')
    print('5 - EXCLUIR CADASTRO')
    print('6 - SAIR')
    
    op = int(input('Digite opção desejada.. \n (lembrando que é obrigatorio você fazer o primiero passo):  '))
    print(' press ENTER')
    input()
    os.system('cls')
    
    match op:
        case 1:
            cadastro.append(input(f'Digite seu nome:  '))
            cadastro.append(input(f'Digite seu gmail: '))
            cadastro.append(input(f'Digite sua id do instagrma: '))
            cadastro.append(int(input(f'Digite sua idade: ')))   
            cadastro.append(int(input(f'Digite seu CPF:  ')))
            login.append(cadastro[:])
            print('press ENTER')
            input()
            os.system('cls')
        case 2:
            nome  = input(f'diigte o nome do login: ')
            for visualizar in login:
                if visualizar[0] == nome:
                    print(f'NOME: {visualizar[0]}')
                    print(f'GMAIL: {visualizar[1]}')
                    print(f'ID INSTAGRAM: {visualizar[2]}')
                    print(f'IDADE: {visualizar[3]}')
                    print(f'CPF: {visualizar[4]}')
                    print('press ENTER')
                    input()
                    os.system('cls')
                elif visualizar != nome:
                    print('nome não encontrado')
                    print('press ENTER')
                    input()
                    os.system()
        case 3: 
            nome = input(f'digite o nome do login que deseja listar: ')
            for listar in login:
                if listar[0] == nome:
                    print(f'NOME: {listar[0]}')
                    print(f'GMAIL: {listar[1]}')
                    print(f'ID INSTAGRAM: {listar[2]}')
                    print(f'IDADE: {listar[3]}')
                    print(f'CPF: {listar[4]}')
                    print('press ENTER')
                    input()
                    os.system('cls')
                else:
                    print('nome não encontrado')
                    print('press ENTER')
                    input()
                    os.system('cls')    
        case 4:
            nome = input('digite o nome do login que você deseja alterar: ')
            for alterar in login:
                if alterar[0] == nome:
                    alterar[0] = input(f'Digite o novo NOME:')
                    alterar[1] = input(f'Digite o novo GMAIL:')
                    alterar[2] = input(f'Digite o novo ID INSTA:')
                    alterar[3] = int(input(f'Digite a nova IDADE:'))
                    alterar[4] = int(input(f'Digite o novo CPF:'))
                    print('CADASTRO ALTERADO! \n confira...')
                    print(f'NOME: {alterar[0]}')
                    print(f'GMAIL: {alterar[1]}')
                    print(f'ID INSTAGRAM: {alterar[2]}')
                    print(f'IDADE: {alterar[3]}')
                    print(f'CPF: {alterar[4]}')
                    print('press ENTER')
                    input()
                    os.system('cls')
                else:
                    print('nome não encontrado')
                    print('press ENTER')
                    input()
                    os.system('cls')


        case 5:
            nome = input(f'digite o nome do login que deseja excluir: ')
            for excluir in login:
                if excluir[0] == nome:
                    x = input('excluir login [sim/nao]: ').upper()
                    if x == 'SIM':
                        login.remove(excluir)
                        print(f'login de {nome} excluido')
                        print('press ENTER')
                        input()
                        
                    elif x == 'NAO':
                        print(f'login de {nome} nao excluidos. voltando...')
                        print('press ENTER')
                        input()
                        os.system('cls')
                    else:
                        print('LOGIN NÃO ENCONTRADO')
                        print('press ENTER')
                        input()
                        os.system('cls')
        case 6:
            a = input('deseja continuar ou sair? [sim/nao]')
            if a == 'sim':
                print('continuando')
                print('press ENTER')
                input()
                os.system('cls')                
            elif a =='nao':
                print('encerrando!')
                break           
            else:
                print('digite sim ou nao')           
                input()
                os.system('cls')            





