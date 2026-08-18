# Algoritmo de Matchmaking: Rio Innovation Week 2026
# A Rio Innovation Week (RIW) 2027 está se aproximando e a organização precisa de um sistema inteligente para otimizar as rodadas de negócios. Como engenheiro de software do evento, você foi encarregado de criar um sistema que conecte automaticamente startups a potenciais investidores. O sistema deve analisar os setores de atuação e cruzar os dados financeiros para recomendar negócios com alta probabilidade de sucesso.

# Objetivo
# Desenvolver um algoritmo em Python que processe duas estruturas de dados (Startups e Investidores) e retorne as combinações válidas com base no setor de interesse e na capacidade de investimento.
# fazer uma função com as duas lista e os investidores tem q tem o mesmo setor igual das startups e um capital maior que os investimentos 

# fazer uma lista de dicionarios de startups
# exemplo: startups = [{'nome': 'EcoTech', 'setor': 'Sustentabilidade', 'investimento_necessario': 150000}]
# investidores_riw = [{'nome': 'Venture Rio', 'setores_interesse': ['Fintech', 'Agritech'], 'capital_disponivel': 600000}]

import sqlite3 as bd

setores= ['Fintech, Healthtech, Edtech, E-commerce, SaaS B2B, Foodtech, Proptech, Insurtech, Agtech, Cleantech, Logtech, Mobilidade, Martech, Gaming, Web3/Blockchain, Deeptech (IA/Biotech), Govtech, HRtec']

def criar_banco():
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
    print('Opção 1: Inscrever ')
    print('Opção 2: Analisar todos ')
    print('Opção 3: Deletar ')
    print('Opção 4: Listar ')
    print('Opção 5: Atualizar ')
    print('Opção 6: Cruzar dados ')
    opcao = input('Digite sua opção(apenas número): ')
    return opcao

def leitura(tipo):
    while True:
        if tipo == 1:
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM STARTUPS')
                startups = cursor.fetchall()
                for startup in startups:
                    (id,nome,setor,investimento_necessario) = startup
                    print(f'Nome da startup: {nome}, setor que atua: {setor}, investimento necessario: {investimento_necessario}')
                break
        elif tipo == 2:
            with bd.connect('RIW27.bd') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute('SELECT * FROM INVESTIDORES')
                    investidores = cursor.fetchall()
                    for investidor in investidores:
                        (id,nome,setor_interesse,capital_disponivel) = investidor
                        print(f'Nome do investidor: {nome}, setor de interesse: {setor_interesse}, capital disponível: {capital_disponivel}')
                    break
        else: 
            print('Digite um valor válido') 

def inscrever(tipo):
    while True:
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
                investimento_necessario = int(input('Escreva o valor: '))
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
                capital_disponivel = int(input('Digite o valor: '))
                cursor.execute('INSERT INTO INVESTIDORES (nome,setor_interesse,capital_disponivel) VALUES(?,?,?)',(nome_investidor,setor_interesse,capital_disponivel))
                conexao.commit()
                break

        else: 
            print('Digite um valor válido') 
             
def deletar(tipo):
    while True:
        if tipo == 1: #tipo 1 = startups
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                leitura(tipo)
                nome = input('Qual startup você deseja deletar: ')
                cursor.execute('DELETE FROM STARTUPS WHERE nome = ?', (nome,))
                conexao.commit()
                print(f'A startup {nome} foi deletado!')
            


        elif tipo == 2: #tipo 2 = insvestidor
            with bd.connect('RIW27.bd') as conexao:
                cursor = conexao.cursor()
                leitura(tipo)
                nome = input('Qual investidor(a) você deseja deletar: ')
                cursor.execute('DELETE FROM INVESTIDORES WHERE nome = ?', (nome,))
                conexao.commit()
                print(f'O(a) investidor(a) {nome} foi deletado(a)!')

        else: 
            print('Digite um valor válido') 
    


def main():

    while True:
        opcao = menu()
        if opcao == '1':
            print('Digite 1 para inscrever uma startup e 2 para um investidor!')
            inscrever(tipo = int(input()))
        elif opcao == '2':
            print('Digite 1 para inscrever uma startup e 2 para um investidor!')
            leitura(tipo = int(input()))
        elif opcao == '3':
            print('Digite 1 para inscrever uma startup e 2 para um investidor!')
            (tipo = int(input()))
main()