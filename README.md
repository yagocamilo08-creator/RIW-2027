RIW 2027 — Sistema de Matchmaking entre Startups e Investidores

Projeto desenvolvido em Python para a Rio Innovation Week (RIW) 2027, com o objetivo de conectar automaticamente startups a investidores durante as rodadas de negócios do evento.

O programa cruza duas bases de dados — startups e investidores — e identifica combinações com alta probabilidade de sucesso, considerando setor de atuação e capacidade financeira.

Sobre o projeto

O sistema compara os dados cadastrados com base em dois critérios:

Setor de atuação: o setor da startup precisa estar entre os setores de interesse do investidor.
Capacidade financeira: o capital disponível do investidor precisa ser igual ou maior que o investimento necessário pela startup.

Os dados são armazenados em um banco de dados SQLite (RIW27.bd), com tabelas separadas para startups e investidores. O usuário interage com o sistema por meio de um menu no terminal.

Este projeto foi feito com fins de estudo, aplicando conceitos de lógica de programação, manipulação de banco de dados relacional e organização de código em módulos.

Funcionalidades
Inscrever: cadastra uma nova startup ou um novo investidor.
Listar: exibe todas as startups e/ou investidores cadastrados.
Deletar: remove uma startup ou investidor cadastrado.
Atualizar: edita informações de um registro já existente.
Cruzar dados: executa o algoritmo de matchmaking, comparando setor e capital disponível.
Sair do programa.
Tecnologias utilizadas
Python 3
SQLite3 (biblioteca nativa do Python)

Ao iniciar, o sistema cria automaticamente o banco RIW27.bd, caso ele ainda não exista, e exibe o menu de opções.

Exemplo de uso
Opção 1: Inscrever
Opção 2: Listar
Opção 3: Deletar
Opção 4: Atualizar
Opção 5: Cruzar dados
Opção 6: Sair do programa
Digite sua opção (apenas número): 5

Match: EcoTech (Sustentabilidade, precisa de 150000) com Venture Rio (capital de 600000)
Status do projeto

Concluído. As funcionalidades principais (inscrever, listar, deletar, atualizar e cruzar dados) estão implementadas e o código está organizado em módulos.

Projeto desenvolvido por Yago Camilo, como parte de estudos em Python.
