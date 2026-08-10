# Algoritmo de Matchmaking: Rio Innovation Week 2026
# A Rio Innovation Week (RIW) 2027 está se aproximando e a organização precisa de um sistema inteligente para otimizar as rodadas de negócios. Como engenheiro de software do evento, você foi encarregado de criar um sistema que conecte automaticamente startups a potenciais investidores. O sistema deve analisar os setores de atuação e cruzar os dados financeiros para recomendar negócios com alta probabilidade de sucesso.

# Objetivo
# Desenvolver um algoritmo em Python que processe duas estruturas de dados (Startups e Investidores) e retorne as combinações válidas com base no setor de interesse e na capacidade de investimento.
# fazer uma função com as duas lista e os investidores tem q tem o mesmo setor igual das startups e um capital maior que os investimentos 

# fazer uma lista de dicionarios de startups
# exemplo: startups = [{'nome': 'EcoTech', 'setor': 'Sustentabilidade', 'investimento_necessario': 150000}]
# investidores_riw = [{'nome': 'Venture Rio', 'setores_interesse': ['Fintech', 'Agritech'], 'capital_disponivel': 600000}]

import sqlite3 as bd


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
        cursor.commit()
        return conexao

def menu():
    print('Opção 1: Inscrever ')
    print('Opção 3: Atualizar ')
    print('Opção 4: Deletar ')
    print('Opção 5: Listar ')
    print('Opção 6: Analisar todos ')
    print('Opção 7: Cruzar dados ')
    opcao = input('Digite sua opção(apenas número): ')
    return opcao
































def main(opcao):

    while True:
        opcao = menu()
        if opcao == '1':
            print('Você deseja inscrever uma startup / investidor?')
            opcao_1 = input()
            if opcao_1 == 'startup':
                pass
                # colocar a função de criação
            else:
                pass
                # colocar a função de criação