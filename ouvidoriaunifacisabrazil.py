reclamacoes=[]
opcao=0
print("BEM VINDO A OUVIDORIA UNIFACISA")
while opcao !=6:
    print(36*"=")
    print("[1] Listar")
    print("[2] Adicionar")
    print("[3] Deletar")
    print("[4] Procurar")
    print("[5] Editar")
    print("[6] Sair")
    print(36 * "=")
    opcao=int(input("Escolha sua opção: "))
    if opcao == 1:
        if len(reclamacoes) == 0:
            print("Não há reclamações cadastradas")
        else:
            print("Lista de reclamações cadastradas")
            for temp in range(len(reclamacoes)):
                print( str(temp+1) + 'º Reclamacao: '+ reclamacoes[temp])
    elif opcao == 2:
        reclamacao=input("Digite a reclamação a ser cadastrada: ")
        reclamacoes.append(reclamacao)
        print("Reclamação adicionada com sucesso")
    elif opcao == 3:
        numero_reclamacao = int(input("\nQual posição da reclamação que você deseja remover: "))
        if numero_reclamacao > 0 and numero_reclamacao <= len(reclamacoes):
            reclamacao_removida = reclamacoes.pop(numero_reclamacao - 1)
            print("A reclamação", reclamacao_removida, "foi removida com sucesso")
        else:
            print("Posição inválida")
    elif opcao == 4:
        numero_reclamacao = int(input("\nQual posição da reclamação que você deseja pesquisar: "))
        if numero_reclamacao > 0 and numero_reclamacao <= len(reclamacoes):
            reclamacao_pesquisada = reclamacoes[numero_reclamacao - 1]
            print("A reclamação pesquisada foi:", reclamacao_pesquisada)
        else:
            print("Posição inválida")
    elif opcao == 5:
        numero_reclamacao = int(input("\nQual posição da reclamação que você deseja editar: "))
        if numero_reclamacao > 0 and numero_reclamacao <= len(reclamacoes):
            nova_reclamacao = input("Digite a nova reclamação: ")
            reclamacoes[numero_reclamacao - 1] = nova_reclamacao
            print("A reclamação foi atualizada com sucesso")
        else:
            print("Posição inválida")
    elif opcao == 6:
        print("Saindo, obrigado por usar nosso sistema de ouvidoria")
    elif opcao !=6:
        print("Opção inválida")











