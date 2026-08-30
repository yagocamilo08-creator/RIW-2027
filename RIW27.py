# Algoritmo de Matchmaking: Rio Innovation Week 2026
# A Rio Innovation Week (RIW) 2027 está se aproximando e a organização precisa de um sistema inteligente para otimizar as rodadas de negócios. Como engenheiro de software do evento, você foi encarregado de criar um sistema que conecte automaticamente startups a potenciais investidores. O sistema deve analisar os setores de atuação e cruzar os dados financeiros para recomendar negócios com alta probabilidade de sucesso.

# Objetivo
# Desenvolver um algoritmo em Python que processe duas estruturas de dados (Startups e Investidores) e retorne as combinações válidas com base no setor de interesse e na capacidade de investimento.
# fazer uma função com as duas lista e os investidores tem q tem o mesmo setor igual das startups e um capital maior que os investimentos 

# fazer uma lista de dicionarios de startups
# exemplo: startups = [{'nome': 'EcoTech', 'setor': 'Sustentabilidade', 'investimento_necessario': 150000}]
# investidores_riw = [{'nome': 'Venture Rio', 'setores_interesse': ['Fintech', 'Agritech'], 'capital_disponivel': 600000}]

import sqlite3 as bd

setores= ['Fintech', 'Healthtech', 'Edtech', 'E-commerce', 'SaaS B2B', 'Foodtech', 'Proptech', 'Insurtech', 'Agtech', 'Cleantech', 'Logtech', 'Mobilidade', 'Martech', 'Gaming', 'Blockchain', 'Deeptech ', 'Govtech', 'HRtec']
def criar_banco():

    """
    Cria (se ainda não existir) o banco de dados RIW27.bd e as tabelas
    STARTUPS e INVESTIDORES, cada uma com seus respectivos campos.
    """

    with bd.connect('RIW27.bd') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS STARTUPS(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        setor TEXT NOT NULL,
                        investimento_necessario INTEGER)''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS INVESTIDORES(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       setor_interesse TEXT NOT NULL,
                       capital_disponivel INTEGER) ''')
        conexao.commit()
        return conexao

def menu(): 
    
    """
    Exibe as opções do sistema na tela e devolve a opção digitada pelo usuário
    (ainda como texto, sem converter para número).
    """

    print('Opção 1: Inscrever ')
    print('Opção 2: Analisar ')
    print('Opção 3: Deletar ')
    print('Opção 4: Atualizar ')
    print('Opção 5: Cruzar dados ')
    print('Opção 6: Sair do programa')
    opcao = input('Digite sua opção(apenas número): ')
    return opcao

def pedir_numero(mensagem): 

    """
    Pede um número inteiro ao usuário e só retorna quando a entrada for válida.
    Repete a pergunta caso o usuário digite algo que não seja um número,
    ou um número negativo.
    """

    while True:
        try:
            n = int(input(mensagem))
            if n <0:
                print('Número inválido!')
            else:
                return n
        except ValueError :
            print('Digite um número válido.')
            

def confirmar(mensagem):

    """
    Pede uma confirmação (S ou N) ao usuário e só retorna quando a resposta
    for válida. Usada antes de ações que alteram dados, como o 'atualizar'.
    """

    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print('Digite apenas S ou N.') == 'N'

def leitura_startup():
    with bd.connect('RIW27.bd') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute('SELECT * FROM STARTUPS')
                    startups = cursor.fetchall()
                    for startup in startups:
                        (id,nome,setor,investimento_necessario) = startup
                        print(f'Nome da startup: {nome}, setor que atua: {setor}, investimento necessario: R${investimento_necessario}')

def leitura_investidores():
    with bd.connect('RIW27.bd') as conexao:
                        cursor = conexao.cursor()
                        cursor.execute('SELECT * FROM INVESTIDORES')
                        investidores = cursor.fetchall()
                        for investidor in investidores:
                            (id,nome,setor_interesse,capital_disponivel) = investidor
                            print(f'Nome do investidor: {nome}, setor de interesse: {setor_interesse}, capital disponível: R${capital_disponivel}')

def leitura():

    """
    Lista os registros salvos no banco.
    tipo 1 -> mostra todas as startups
    tipo 2 -> mostra todos os investidores
    """

    while True:
        tipo = pedir_numero('Digite um número 1 ou 2. Sendo 1 para startup e 2 para investidor: ')
        if tipo == 1:
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM STARTUPS')
                startups = cursor.fetchall()
                for startup in startups:
                    (id,nome,setor,investimento_necessario) = startup
                    print(f'Nome da startup: {nome}, setor que atua: {setor}, investimento necessario: R${investimento_necessario}')
                break
        elif tipo == 2:
            with bd.connect('RIW27.bd') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute('SELECT * FROM INVESTIDORES')
                    investidores = cursor.fetchall()
                    for investidor in investidores:
                        (id,nome,setor_interesse,capital_disponivel) = investidor
                        print(f'Nome do investidor: {nome}, setor de interesse: {setor_interesse}, capital disponível: R${capital_disponivel}')
                    break
        else: 
            print('Digite um valor válido')
             
            

def inscrever():

    """
    Cadastra um novo registro no banco.
    tipo 1 -> cadastra uma startup (nome, setor, investimento necessário)
    tipo 2 -> cadastra um investidor (nome, setor de interesse, capital disponível)
    """

    while True:
        tipo = pedir_numero('Digite um número 1 ou 2. Sendo 1 para startup e 2 para investidor: ')
        if tipo == 1: #tipo 1 = startups
            print('Vamos inscrever uma startup!')
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                print('Para voce increver uma startup, precisamos das seguintes informações: nome, setor e investimento necessario.')
                print('Primeiro vamos começar pelo nome.')
                nome_startup = input('Escreva o nome da sua startup: ')
                print(f'Em seguida o setor que esta empresa atua: {setores}.')
                setor = input('Selecione o setor: ')
                print('Por fim, o investimento necessario que essa empresa necessita')
                investimento_necessario = pedir_numero('Escreva o valor: ')
                cursor.execute('INSERT INTO STARTUPS (nome,setor,investimento_necessario) VALUES(?,?,?)',(nome_startup,setor,investimento_necessario))
                print(f'Inscrição da(o) {nome_startup} concluído com sucesso!🥳')
                conexao.commit
                break
        elif tipo == 2: #tipo 2 = insvestidor
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                print('Vamos inscrever um investidor!')
                print('Para voce increver uma startup, precisamos das seguintes informações: nome, setor_interesse e capital disponível.')
                print('Primeiro vamos começar pelo nome.')
                nome_investidor = input('Digite seu nome: ')
                print(f'Em seguida o setor de interesse: {setores}.')
                setor_interesse = input('Escreva o setor: ')
                print('Por fim, o seu capital disponivel')
                capital_disponivel = pedir_numero('Digite o valor: ')
                cursor.execute('INSERT INTO INVESTIDORES (nome,setor_interesse,capital_disponivel) VALUES(?,?,?)',(nome_investidor,setor_interesse,capital_disponivel))
                print(f'Inscrição da(o) {nome_investidor} concluído com sucesso!🥳')
                conexao.commit()
                break

        else: 
            print('Digite um valor válido') 
             
def deletar():

    """
    Remove um registro do banco pelo nome.
    tipo 1 -> deleta uma startup
    tipo 2 -> deleta um investidor
    Antes de pedir o nome, chama leitura(tipo) para mostrar os registros existentes.
    """

    while True:
        tipo = pedir_numero('Digite um número 1 ou 2. Sendo 1 para startup e 2 para investidor: ')
        if tipo == 1: #tipo 1 = startups
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                leitura_startup()
                nome = input('Qual startup você deseja deletar: ')
                cursor.execute('DELETE FROM STARTUPS WHERE nome = ?', (nome,))
                conexao.commit()
                print(f'A startup {nome} foi deletado!')
            break


        elif tipo == 2: #tipo 2 = insvestidor
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()

                leitura_investidores()
                nome = input('Qual investidor(a) você deseja deletar: ').capitalize()
                cursor.execute('DELETE FROM INVESTIDORES WHERE nome = ?', (nome,))
                conexao.commit()
                print(f'O(a) investidor(a) {nome} foi deletado(a)!')
            break

        else: 
            print('Digite um valor válido') 

        
def atualizar():

    """
    Edita um campo específico de um registro já cadastrado.
    tipo 1 -> atualiza uma startup (nome, setor ou investimento necessário)
    tipo 2 -> atualiza um investidor (nome, setor de interesse ou capital disponível)
    Pede confirmação antes de aplicar a alteração.
    """

    while True:
        tipo = pedir_numero('Digite um número 1 ou 2. Sendo 1 para startup e 2 para investidor: ')
        if tipo == 1: #tipo 1 = startups
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                leitura_startup()
                nome = input('Qual startup deseja atualizar: ')

                if confirmar('Deseja realmente mudar algo nesta startup(S/N)? '):
                    print('Nenhuma alteração foi feita')
                    return

                print('O que deseja atualizar? ')
                print('1- Nome')
                print('2- Setor')
                print('3- Investimento Necessário')
                campo = input('Qual das opções voce deseja(digite somente o número): ')

                if campo == '1':
                    novo_valor = input('Digite o novo nome: ')
                    cursor.execute('UPDATE STARTUPS SET nome = ? WHERE nome = ?', (novo_valor, nome))
                elif campo == '2':
                    novo_valor = input(f'Para qual setor deseja atualizar {setores}: ')
                    cursor.execute('UPDATE STARTUPS SET setor = ? WHERE nome = ?', (novo_valor, nome))
                elif campo == '3':
                    novo_valor = pedir_numero('Qual será o novo investimento necessário:  ')
                    cursor.execute('UPDATE STARTUPS SET investimento_necessario = ? WHERE nome = ?', (novo_valor, nome))
                else: 
                    print('Opção inválida. Nenhuma alteração foi feita.')
                    return 
                conexao.commit()
                print('Atualização feita com sucesso!')
        elif tipo == 2: # Tipo 2 = Investidores
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                leitura_investidores()
                nome = input('Qual investidor deseja atualizar: ')

                if confirmar('Deseja realmente mudar algo neste investidor(S/N)? ') == 'N':
                    print('Nenhuma alteração foi feita')
                    return

                print('O que deseja atualizar? ')
                print('1- Nome')
                print('2- Setor de Interesse')
                print('3- Capital Disponível ')
                campo = input('Qual das opções voce deseja(digite somente o número): ')

                if campo == '1':
                    novo_valor = input('Digite o novo nome: ')
                    cursor.execute('UPDATE INVESTIDORES SET nome = ? WHERE nome = ?', (novo_valor, nome))
                elif campo == '2':
                    novo_valor = input(f'Qual será seu novo setor de interesse {setores}: ')
                    cursor.execute('UPDATE INVESTIDORES SET setor_interesse = ? WHERE nome = ?', (novo_valor, nome))
                elif campo == '3':
                    novo_valor = pedir_numero('Qual seu novo capital disponível :  ')
                    cursor.execute('UPDATE INVESTIDORES SET capital_disponivel = ? WHERE nome = ?', (novo_valor, nome))
                elif campo == '4':
                    exit

                else: 
                    print('Opção inválida. Nenhuma alteração foi feita.')
                    return 
                conexao.commit()
                print('Atualização feita com sucesso!')
        else:
            print('Digite um valor válido')

def cruzar_dados():

    """
    Compara todas as startups com todos os investidores cadastrados e
    imprime na tela os pares que forem compatíveis.
 
    Um par é considerado match quando:
    - o setor da startup é igual ao setor de interesse do investidor
      (comparação feita ignorando maiúsculas/minúsculas e espaços extras)
    - o capital disponível do investidor é maior ou igual ao investimento
      necessário pela startup
    """

    with bd.connect('RIW27.bd') as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM STARTUPS')
        startups = cursor.fetchall()
        cursor.execute('SELECT * FROM INVESTIDORES')
        investidores = cursor.fetchall()
        encontrou_par = False
        for startup in startups:
            for investidor in investidores:
                (id,nome_startup,setor,investimento_necessario) = startup
                (id,nome_investidor,setor_interesse,capital_disponivel) = investidor        
                if setor_interesse.lower().strip() == setor.lower().strip() and capital_disponivel >= investimento_necessario:
                    encontrou_par = True
                    print(f'✅ Match: {nome_startup} ({setor}, precisa de {investimento_necessario}) '
                           f'com {nome_investidor} (capital de {capital_disponivel})')
        if not encontrou_par:
            print('Nenhum par compatível foi encontrado.')

def main():
    """
    Loop principal do programa: mostra o menu e chama a função
    correspondente à opção escolhida, até o usuário sair (opção 6).
    """
    
    while True:
        opcao = menu()
        if opcao == '1':
            inscrever()
        elif opcao == '2':
            leitura()
        elif opcao == '3':
            deletar()
        elif opcao == '4':
            atualizar()
        elif opcao == '5':
            cruzar_dados()
        elif opcao == '6':
            break
        else:
            print('Digite uma opção válida!')
main()





# fazer com que a pergunta da leitura nao apareça na função de deletar. Criar uma função de leitura global, e ela so vai ser chamada dentro das outras funções 


# 