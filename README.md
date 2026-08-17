# RIW 2027
Sistema de matchmaking desenvolvido para a Rio Innovation Week (RIW) 2027, com o objetivo de conectar automaticamente startups a investidores durante as rodadas de negócios do evento.  O programa cruza duas bases de dados — startups e investidores — e recomenda combinações com alta probabilidade de sucesso, considerando dois critérios principais:  Setor de atuação: o setor da startup precisa constar entre os setores de interesse do investidor. Capacidade financeira: o capital disponível do investidor precisa ser igual ou maior que o investimento necessário pela startup.  Os dados são persistidos em um banco de dados SQLite (RIW27.bd), com tabelas separadas para startups e investidores, e o usuário interage com o sistema por meio de um menu no terminal.

O programa cruza duas bases de dados — startups e investidores — e recomenda combinações com alta probabilidade de sucesso, considerando dois critérios principais:

Setor de atuação: o setor da startup precisa constar entre os setores de interesse do investidor.
Capacidade financeira: o capital disponível do investidor precisa ser igual ou maior que o investimento necessário pela startup.

Os dados são persistidos em um banco de dados SQLite (RIW27.bd), com tabelas separadas para startups e investidores, e o usuário interage com o sistema por meio de um menu no terminal.

Funcionalidades previstas
Inscrever: cadastrar uma nova startup ou um novo investidor no banco de dados.
Atualizar: editar informações de um registro já existente.
Deletar: remover uma startup ou investidor cadastrado.
Listar: exibir todas as startups e/ou investidores cadastrados.
Analisar todos: exibir um panorama geral dos dados cadastrados.
Cruzar dados: executar o algoritmo de matchmaking, comparando setor e capital disponível para gerar as combinações válidas entre startups e investidores.
Estrutura de dados

O menu apresentará as opções numeradas (1 a 7) para inscrever, atualizar, deletar, listar, analisar e cruzar os dados.

Status

🚧 Em desenvolvimento — as funções de criação (INSERT), atualização, exclusão, listagem e cruzamento de dados ainda precisam ser implementadas dentro do menu principal.
