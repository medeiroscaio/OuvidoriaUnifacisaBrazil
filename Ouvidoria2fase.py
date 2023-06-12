'''create table manifestacao(
  codigo int auto_increment,
  titulo varchar(100),
  descricao varchar(500),
  autor varchar(100),
  tipo int,
  primary key(codigo)
  );'''

from operacoesbd import *

listaReclamacoes = [ ]

conexao = abrirBancoDados('127.0.0.1','root','root','ouvidoriajr')

opcao = 0

while opcao != 8:
    print()
    print('Menu')
    print('1 Listagem das manifestações')
    print('2 Listagem de manifestações por tipo')
    print('3 Criar uma nova manifestação')
    print('4 Exibir quantidade de manifestações')
    print('5 Pesquisar uma manifestação por código')
    print('6 Alterar o título e uma descrição de uma manifestação')
    print('7 Excluir uma manifestação pelo código')
    print('8 sair do sistema')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        consultaTipo = 'select * from manifestacao'

        listaReclamacoes = listarBancoDados(conexao, consultaListagem)
        if len(listaReclamacoes) == 0:
            print('Lista vazia!')
        else:
            for elemento in listaReclamacoes:
                print('codigo:', elemento[0], 'titulo:', elemento[1], 'descrição:', elemento[2], 'autor:', elemento[3], 'tipo:', elemento[4])
    elif opcao == 2:
        tipo = int(input('1 - Reclamação 2 - sugestão 3 - elogio: '))
        sqlTipo = 'select * from manifestacao where tipo = %s'
        valores = [tipo]

    elif opcao == 3:
        titulo = input('Digite a manifestação: ')
        descricao = input('Digite uma descrição: ')
        autor = input('Digite seu nome : ')
        tipo = int(input('1 - Reclamação 2 - sugestão 3 - elogio: '))

        sqlInsercao = 'insert into manifestacao (titulo,descricao,autor,tipo) values(%s,%s,%s,%s)'
        valores = [titulo, descricao, autor, tipo]

        insertNoBancoDados(conexao, sqlInsercao, valores)
    elif opcao == 4:
        consultarQuantidade = 'select count(*) from manifestacao'
        resultado = listarBancoDados(conexao,consultarQuantidade)
        quantidade = resultado[0][0]
        print(quantidade)

    elif opcao == 5:
        codigo = input('Digite o codigo da manifestação: ')
        consultaListagem = 'select * from manifestacao where codigo = ' + codigo

        listaReclamacoes = listarBancoDados(conexao, consultaListagem)
        print(listaReclamacoes)

        for elemento in listaReclamacoes:
            print('codigo', elemento[0], 'titulo', elemento[1], 'descrição', elemento[2], 'autor', elemento[3], 'tipo',
                  elemento[4])

    elif opcao == 6:
        codigo = input('Digite o codigo da manifestação: ')
        novoTitulo = input('Digite o novo titulo da manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')

        sqlAtualizar = 'update manifestacao set titulo = %s  where codigo = %s'
        valores = [novoTitulo, codigo]
        sqlAtualizar = 'update manifestacao set descricao = %s where codigo = %s'
        valores = [novaDescricao,codigo]


        atualizarBancoDados(conexao, sqlAtualizar, valores)
        print('Atualizado com sucesso!')

    elif opcao == 7:
        codigo = input('Digite o codigo da manifestação: ')
        consultaListagem = 'delete from manifestacao where codigo = %s '
        dados = [codigo]
        print('Excluido com sucesso!')

        excluirBancoDados(conexao, consultaListagem, dados)




encerrarBancoDados(conexao)
print('Obrigado por participar!')