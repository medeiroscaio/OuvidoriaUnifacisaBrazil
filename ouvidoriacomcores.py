'''
Caio Victor Bezerra de Medeiros Souto
Jonildo Pereira Araújo Júnior
João Matheus de Figueiredo Tavares
Larissa Alcântara Sipião
Saniel Martins Nóbrega


BIBLIOTECA COLORAMA IMPORTADA, É SÓ BAIXAR
'''


from colorama import Fore, Style

reclamacoes = []
opcao = 0
print(Fore.CYAN + "BEM VINDO A OUVIDORIA UNIFACISA" + Style.RESET_ALL)
while opcao != 6:
    print(36 * "=")
    print("[1] " + Fore.GREEN + "Listar" + Style.RESET_ALL)
    print("[2] " + Fore.GREEN + "Adicionar" + Style.RESET_ALL)
    print("[3] " + Fore.GREEN + "Deletar" + Style.RESET_ALL)
    print("[4] " + Fore.GREEN + "Procurar" + Style.RESET_ALL)
    print("[5] " + Fore.GREEN + "Editar" + Style.RESET_ALL)
    print("[6] " + Fore.RED + "Sair" + Style.RESET_ALL)
    print(36 * "=")
    opcao = int(input("Escolha sua opção: "))
    if opcao == 1:
        if len(reclamacoes) == 0:
            print("Não há reclamações cadastradas")
        else:
            print("Lista de reclamações cadastradas")
            for temp in range(len(reclamacoes)):
                print(str(temp + 1) + 'º Reclamação: ' + reclamacoes[temp])
    elif opcao == 2:
        reclamacao = input("Digite a reclamação a ser cadastrada: ")
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
        print(Fore.RED + "Saindo, obrigado por usar nosso sistema de ouvidoria" + Style.RESET_ALL)
    elif opcao != 6:
        print("Opção inválida")
