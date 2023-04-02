#Tentativa 1 - CRUD
opc = ''
cad = {}
prod = {}
vendas = {}
cod = 0
#Menu principal

def conferir(Estoque): #Função para tratar informações inválidas digitadas
    try:
         int(Estoque)
    except ValueError:
         return False
    return True

while opc != '0':
    print("""
[1] Cadastrar
[2] Clientes
[3] Motos
[4] Vendas
[0] Sair
    """)
    opc = input('Digite uma opção:')
    if opc == '1':

        while opc != '0':
            print("""
[1] Cadastrar Cliente
[2] Cadastrar Moto
[0] Sair
            """)
            opc = input('Digite uma opção:')
            if opc == '1':


                while True: #Cadastro Perfil Cliente
                    print('\nAdicione um novo Cliente\n')
                    Cliente = []
                    nome = ''
                    cpf = ''
                    tel = ''

                    nome = input('Nome do cliente: ')
                    if nome in cad:
                        print('Nome já cadastrado!')
                    else:
                        Cliente.append(nome)
                        cpf = input ('CPF: ')
                        Cliente.append(cpf)
                        tel = input ('Telefone: ')
                        Cliente.append(tel)


                        cad[f'{nome}'] = Cliente[1:]

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')

                    for x, y in cad.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    while True:
                        t = input('\n\nDeseja continuar? [S/N]: ')

                        if t[0] in 'Nn':
                            break
                        elif t[0] in 'Ss':
                            break
                        else:
                            print('Dígito inválido!')


                    if t[0] in 'Nn':
                        break

            if opc == '2':

                while True: #Cadastro Produto
                    print('\nAdicione um novo produto\n')
                    Produto = []
                    Moto = ''
                    Pot = ''
                    Estoque = ''

                    Moto = input('Nome da Moto: ')
                    if Moto in prod:
                        print('Moto já cadastrada!')
                    else:
                        Produto.append(Moto)
                        Pot = input ('Potência: ')
                        Produto.append(Pot)
                        Estoque = input('Estoque: ')

                        while conferir(Estoque) == False: #Conferir número inteiro sem interromper
                            print('Digite um número inteiro!')
                            Estoque = input('Estoque: ')

                        Produto.append(Estoque)


                        prod[f'{Moto}'] = Produto[1:]

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    while True:
                        t = input('\n\nDeseja continuar? [S/N]: ')

                        if t[0] in 'Nn':
                            break
                        elif t[0] in 'Ss':
                            break
                        else:
                            print('Dígito inválido!')


                    if t[0] in 'Nn':
                        break

            if opc == '0':
                opc = ''
                break

    if opc == '2':
        while opc != '0':
            print("""
[1] Exibir todos os clientes
[2] Consultar cliente
[3] Excluir cliente
[4] Alterar Cliente
[0] Sair
            """)
            opc = input('Digite uma opção:')

            if opc == '1': #Exibir todos os clientes
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    for x, y in cad.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

            if opc == '2': #Consultar um cliente
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    consulta = input('\nDigite o nome da moto que deseja consultar: ')
                    if consulta in cad:

                        print(f'{"":-<57}')
                        print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                        print(f'{"":-<57}')

                        for clientes, dados in cad.items():
                            if consulta == clientes:
                                print(f'{clientes: <20}{dados[0]: <20}{dados[1]: <20}')

            if opc == '3': #Exclusão
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo Exclusão de item chave
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    for x, y in cad.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    excluir = input('\nDigite o nome do Cliente que deseja excluir: ')
                    if excluir in cad:
                        del(cad[excluir])
                        print(f'Cliente {excluir} excluído!')
                    else:
                        print('Não existe!')


            if opc == '4': #Alterar
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo alteração
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    for x, y in cad.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    alterar = input('\nDigite o nome do Cliente que deseja alterar: ')
                    if alterar in cad:
                        print(f'[Cliente {alterar} selecionado]')
                        Cliente = []

                        for x, y in cad.items():
                            if x == alterar:
                                print(f'{"":-<57}')
                                print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                                print(f'{"":-<57}')
                                print(f'{x: <20}{y[0]: <20}{y[1]: <20}\n')


                        nome = input('Digite o nome: ')
                        Cliente.append(nome)
                        cpf = input('CPF: ')
                        Cliente.append(cpf)
                        tel = input('Telefone: ')
                        Cliente.append(tel)

                        del (cad[alterar])
                        cad[f'{nome}'] = Cliente[1:]

                        print('Alteração concluída!')

                    else:
                        print('Não existe!')

            if opc == '0':
                opc = ''
                break
    if opc == '3': #Menu Motos
        while opc != '0':
            print("""
[1] Exibir todas as motos
[2] Consultar moto
[3] Excluir moto
[4] Alterar moto
[0] Sair
            """)
            opc = input('Digite uma opção:')

            if opc == '1': #Exibir todas as motos
                if prod == {}:
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

            if opc == '2': #Consultar uma moto
                if prod == {}:
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    consulta = input('\nDigite o nome da moto que deseja consultar: ')
                    if consulta in prod:

                        print(f'{"":-<57}')
                        print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                        print(f'{"":-<57}')

                        for produtos, moto in prod.items():
                            if consulta == produtos:
                                print(f'{produtos: <20}{moto[0]: <20}{moto[1]: <20}')


                    else:
                        print(f'{consulta} não existe no estoque!')

            if opc == '3': #Excluir moto
                if prod == {}:
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo Exclusão de item chave

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    #Entrada - Moto a ser excluída
                    excluir = input('\nDigite o nome da moto que deseja excluir: ')
                    if excluir in prod:
                        del(prod[excluir])
                        print(f'Moto {excluir} excluído!')
                    else:
                        print('Não existe no estoque!')


            if opc == '4': #Alterar moto
                if prod == {}:
                    #Exibir cadastro e mensagem, caso esteja vazio.
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo alteração

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    alterar = input('\nDigite o nome da moto que deseja alterar: ')

                    if alterar in prod:
                        print(f'[Moto {alterar} selecionada]')

                        for x, y in prod.items():
                            if x == alterar:
                                print(f'{"":-<57}')
                                print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                                print(f'{"":-<57}')
                                print(f'{x: <20}{y[0]: <20}{y[1]: <20}\n')
                                Produto = []
                                Moto = ''
                                Pot = ''
                                Estoque = ''

                        Moto = input('Nome da Moto: ')
                        Produto.append(Moto)
                        Pot = input('Potência: ')
                        Produto.append(Pot)
                        Estoque = input('Estoque: ')

                        while conferir(Estoque) == False:  # Conferir número inteiro sem interromper
                            print('Digite um número inteiro!')
                            Estoque = input('Estoque: ')
                        Produto.append(Estoque)

                        del (prod[alterar])
                        prod[f'{Moto}'] = Produto[1:]


                        print('Alteração concluída!')

                    else:
                        print('Não existe!')

            if opc == '0': #Sair
                opc = ''
                break


    if opc == '4':  # Menu vendas
        while opc != '0':
            print("""
[1] Vender
[2] Histórico
[0] Sair
""")
            opc = input('Digite uma opção:')

            if opc == '1':  #Vender
                if cad == {}:
                    print('Cadastro de clientes vazio!')
                elif prod == {}:
                    print('Cadastro de produtos vazio!')
                else:
                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')

                    for x, y in cad.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')
                    vcliente = input('\nDigite o nome do cliente comprador: ')
                    if vcliente in cad:
                        # Exibir cadastro
                        print(f'{"":-<57}')
                        print(f'{"Moto": <19} {"Potência": <19} {"Estoque": <19}')
                        print(f'{"":-<57}')
                        for x, y in prod.items():
                            print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                        #Entrada de dados - Moto a ser vendida
                        vproduto = input('\nDigite o nome da moto a ser vendida: ')
                        if vproduto in prod:

                            qtd = input('Digite a quantidade vendida:')
                            while not conferir(qtd): #Verificação do número digitado - Deve ser inteiro
                                print('Digite apenas números inteiros')
                                qtd = input('Digite a quantidade vendida:')
                            qtd = int(qtd)

                            for x, y in prod.items():
                                if vproduto == x:
                                    if int(y[1]) <= 0:
                                        print('Estoque ZERADO! Não é possível realizar venda!')
                                    else:
                                        y[1] = int(y[1]) - qtd
                                        print(f'{qtd} unidade(s) vendida(s)\n')
                                        cod += 1
                                        vendas[f'{cod}'] = vcliente, vproduto, qtd



                        else:
                            print('Produto não encontrado!') #Caso o produto digitado seja inválido
                    else:
                        print('Cliente não encontrado!') #Caso o Cliente digitado seja inválido

            if opc == '2':  #Exibir histórico de vendas
                print(f'{"":-<57}')
                print(f'{"Comprador": <19} {"Produto": <19} {"Quantidade Vendida": <19}')
                print(f'{"":-<57}')
                for nome, info in vendas.items():
                    print(f'{info[0]: <20}{info[1]: <20}{info[2]: <20}')

            if opc == '0': #Sair
                opc = ''
                break
