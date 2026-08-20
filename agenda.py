contatos = []


def cadastrar_contato():
    pass


def listar_contatos():
    pass


def buscar_contato():
    pass


def remover_contato():
    pass


while True:
    print("==== Agenda de Contatos ====")
    print(
        "1 - Cadastrar contato\n2 - Listar contatos\n3 - Buscar contato\n4 - Remover contato\n5 - Sair"
    )
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("Opção incorreta")
        continue
    if opcao not in (1, 2, 3, 4, 5):
        print("Opção inválida")
        continue
    match opcao:
        case 1:
            cadastrar_contato()
        case 2:
            listar_contatos()
        case 3:
            buscar_contato()
        case 4:
            remover_contato()
        case 5:
            break
