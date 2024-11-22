from clientes import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente
from carros import cadastrar_carro, listar_carros, atualizar_carro, deletar_carro
from alugueis import realizar_aluguel, listar_alugueis, atualizar_aluguel, deletar_aluguel

def menu():
    while True:
        print("\n--- Sistema de Gestão de Aluguéis de Carros ---")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Carros")
        print("3. Gerenciar Aluguéis")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_carros()
        elif opcao == "3":
            menu_alugueis()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\n--- Gerenciamento de Clientes ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cadastrar_cliente(nome, cpf, telefone, email)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            id_cliente = int(input("ID do Cliente: "))
            nome = input("Novo Nome (ou pressione Enter para manter): ")
            cpf = input("Novo CPF (ou pressione Enter para manter): ")
            telefone = input("Novo Telefone (ou pressione Enter para manter): ")
            email = input("Novo Email (ou pressione Enter para manter): ")
            atualizar_cliente(id_cliente, nome or None, cpf or None, telefone or None, email or None)
        elif opcao == "4":
            id_cliente = int(input("ID do Cliente: "))
            deletar_cliente(id_cliente)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_carros():
    while True:
        print("\n--- Gerenciamento de Carros ---")
        print("1. Cadastrar Carro")
        print("2. Listar Carros")
        print("3. Atualizar Carro")
        print("4. Deletar Carro")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            ano = int(input("Ano: "))
            cor = input("Cor: ")
            cadastrar_carro(modelo, marca, ano, cor)
        elif opcao == "2":
            listar_carros()
        elif opcao == "3":
            id_carro = int(input("ID do Carro: "))
            modelo = input("Novo Modelo (ou pressione Enter para manter): ")
            marca = input("Nova Marca (ou pressione Enter para manter): ")
            ano = input("Novo Ano (ou pressione Enter para manter): ")
            cor = input("Nova Cor (ou pressione Enter para manter): ")
            atualizar_carro(id_carro, modelo or None, marca or None, int(ano) if ano else None, cor or None)
        elif opcao == "4":
            id_carro = int(input("ID do Carro: "))
            deletar_carro(id_carro)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alugueis():
    while True:
        print("\n--- Gerenciamento de Aluguéis ---")
        print("1. Realizar Aluguel")
        print("2. Listar Aluguéis")
        print("3. Atualizar Aluguel")
        print("4. Deletar Aluguel")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_cliente = int(input("ID do Cliente: "))
            id_carro = int(input("ID do Carro: "))
            data_inicio = input("Data de Início (YYYY-MM-DD): ")
            data_fim = input("Data de Fim (YYYY-MM-DD): ")
            valor_total = float(input("Valor Total: "))
            realizar_aluguel(id_cliente, id_carro, data_inicio, data_fim, valor_total)
        elif opcao == "2":
            listar_alugueis()
        elif opcao == "3":
            id_aluguel = int(input("ID do Aluguel: "))
            data_inicio = input("Nova Data de Início (YYYY-MM-DD ou Enter para manter): ")
            data_fim = input("Nova Data de Fim (YYYY-MM-DD ou Enter para manter): ")
            valor_total = input("Novo Valor Total (ou Enter para manter): ")
            atualizar_aluguel(id_aluguel, data_inicio or None, data_fim or None, float(valor_total) if valor_total else None)
        elif opcao == "4":
            id_aluguel = int(input("ID do Aluguel: "))
            deletar_aluguel(id_aluguel)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
