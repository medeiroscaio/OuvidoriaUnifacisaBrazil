'''
CAIO VICTOR BEZERRA DE MEDEIROS SOUTO
CAIO MOURA PORTELA SOUSA
LARISSA ALCANTARA SIPIAO
SANIEL MARTINS NOBREGA
JONILFO PEREIRA ARAUJO JUNIOR
JOAO MATHEUS DE FIGUEIREDO TAVARES

COLOQUEI O OPERACOES BD AQUI DENTRO
SÓ COLOCAR AS INFORMACOES DO BANCO DE DADOS

criterio tabela

create table manifestacao(
  codigo int auto_increment,
  titulo varchar(100),
  descricao varchar(500),
  autor varchar(100),
  tipo int,
  primary key(codigo)
  );'''

import mysql.connector
from colorama import Fore, Style

def abrirBancoDados(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def encerrarBancoDados(connection):
    connection.close()

def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

def listarBancoDados(connection, sql, dados=None):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    results = cursor.fetchall()
    cursor.close()
    return results


def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas

def excluirBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas

listaReclamacoes = []
conexao = abrirBancoDados('', '', '', '')

opcao = 0

while opcao != 8:
    print('Menu')
    print("=" * 40 + Style.RESET_ALL)
    print('1-' + Fore.CYAN + 'Listagem das manifestações' + Style.RESET_ALL)
    print('2-' + Fore.CYAN + 'Listagem de manifestações por tipo' + Style.RESET_ALL)
    print('3-' + Fore.CYAN + 'Criar uma nova manifestação' + Style.RESET_ALL)
    print('4-' + Fore.CYAN + 'Exibir quantidade de manifestações' + Style.RESET_ALL)
    print('5-' + Fore.CYAN + 'Pesquisar uma manifestação por código' + Style.RESET_ALL)
    print('6-' + Fore.CYAN + 'Alterar o título e uma descrição de uma manifestação' + Style.RESET_ALL)
    print('7-' + Fore.CYAN + 'Excluir uma manifestação pelo código' + Style.RESET_ALL)
    print('8-' + Fore.CYAN + 'Sair do sistema' + Style.RESET_ALL)
    print("=" * 40 + Style.RESET_ALL)
    print()
    opcao = int(input('Digite uma opção: '))
    print()

    if opcao == 1:
        consultaTipo = 'SELECT * FROM manifestacao'
        listaReclamacoes = listarBancoDados(conexao, consultaTipo)

        if len(listaReclamacoes) == 0:
            print('Lista vazia!')
        else:
            for elemento in listaReclamacoes:
                print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4])
                print()

    elif opcao == 2:
        tipo = int(input('1 - Reclamação 2 - Sugestão 3 - Elogio: '))

        if tipo in [1, 2, 3]:
            sqlTipo = 'SELECT * FROM manifestacao WHERE tipo = %s'
            valores = [tipo]
            listaReclamacoes = listarBancoDados(conexao, sqlTipo, valores)

            if len(listaReclamacoes) == 0:
                print('Lista vazia!')
            else:
                for elemento in listaReclamacoes:
                    print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4])
                    print()
        else:
            print('Opção inválida!')

    elif opcao == 3:
        titulo = input('Digite a manifestação: ')
        descricao = input('Digite uma descrição: ')
        autor = input('Digite seu nome: ')
        tipo = int(input('1 - Reclamação 2 - Sugestão 3 - Elogio: '))

        sqlInsercao = 'INSERT INTO manifestacao (titulo, descricao, autor, tipo) VALUES (%s, %s, %s, %s)'
        valores = [titulo, descricao, autor, tipo]

        insertNoBancoDados(conexao, sqlInsercao, valores)

    elif opcao == 4:
        consultarQuantidadeReclamacoes = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 1'
        consultarQuantidadeSugestoes = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 2'
        consultarQuantidadeElogios = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 3'

        resultadoReclamacoes = listarBancoDados(conexao, consultarQuantidadeReclamacoes)
        resultadoSugestoes = listarBancoDados(conexao, consultarQuantidadeSugestoes)
        resultadoElogios = listarBancoDados(conexao, consultarQuantidadeElogios)

        quantidadeReclamacoes = resultadoReclamacoes[0][0]
        quantidadeSugestoes = resultadoSugestoes[0][0]
        quantidadeElogios = resultadoElogios[0][0]

        print('Quantidade de reclamações:', quantidadeReclamacoes)
        print('Quantidade de sugestões:', quantidadeSugestoes)
        print('Quantidade de elogios:', quantidadeElogios)

    elif opcao == 5:
        codigo = input('Digite o código da manifestação: ')
        consultaListagem = 'SELECT * FROM manifestacao WHERE codigo = ' + codigo

        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Nenhuma manifestação encontrada com o código fornecido.')
        else:
            for elemento in listaReclamacoes:
                print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4])
                print()

    elif opcao == 6:
        codigo = input('Digite o código da manifestação: ')
        novoTitulo = input('Digite o novo título da manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')

        sqlAtualizar = 'UPDATE manifestacao SET titulo = %s, descricao = %s WHERE codigo = %s'
        valores = [novoTitulo, novaDescricao, codigo]

        linhasAfetadas = atualizarBancoDados(conexao, sqlAtualizar, valores)

        if linhasAfetadas > 0:
            print('Atualizado com sucesso!')
        else:
            print('Nenhuma manifestação encontrada com o código fornecido.')

    elif opcao == 7:
        codigo = input('Digite o código da manifestação: ')
        consultaListagem = 'DELETE FROM manifestacao WHERE codigo = %s'
        dados = [codigo]
        linhasAfetadas = excluirBancoDados(conexao, consultaListagem, dados)

        if linhasAfetadas > 0:
            print('Manifestação excluída com sucesso!')
        else:
            print('Nenhuma manifestação encontrada com o código fornecido.')

    elif opcao == 8:
        break

    else:
        print('Opção inválida!')

encerrarBancoDados(conexao)
print('Obrigado por participar!')
