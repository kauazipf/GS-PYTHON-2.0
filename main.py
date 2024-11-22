from models.clientes import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente
from models.carros import cadastrar_carro, listar_carros, atualizar_carro, deletar_carro
from models.alugueis import realizar_aluguel, listar_alugueis, atualizar_aluguel, deletar_aluguel
from utils.input_validation import validar_entrada
from utils.export_utils import export_to_json, export_to_excel

def menu():
    while True:
        print("\n--- Sistema de Gestão de Aluguéis de Carros ---")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Carros")
        print("3. Gerenciar Aluguéis")
        print("0. Sair")

        opcao = validar_entrada("Escolha uma opção: ")

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
        print("5. Exportar Consulta para JSON/Excel")
        print("0. Voltar")

        opcao = validar_entrada("Escolha uma opção: ")

        if opcao == "1":
            nome = validar_entrada("Nome: ")
            cpf = validar_entrada("CPF: ")
            telefone = validar_entrada("Telefone: ")
            email = validar_entrada("Email: ")
            cadastrar_cliente(nome, cpf, telefone, email)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            id_cliente = validar_entrada("ID do Cliente: ")
            nome = validar_entrada("Novo Nome (ou pressione Enter para manter): ")
            cpf = validar_entrada("Novo CPF (ou pressione Enter para manter): ")
            telefone = validar_entrada("Novo Telefone (ou pressione Enter para manter): ")
            email = validar_entrada("Novo Email (ou pressione Enter para manter): ")
            atualizar_cliente(id_cliente, nome or None, cpf or None, telefone or None, email or None)
        elif opcao == "4":
            id_cliente = validar_entrada("ID do Cliente: ")
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

        opcao = validar_entrada("Escolha uma opção: ")

        if opcao == "1":
            modelo = validar_entrada("Modelo: ")
            marca = validar_entrada("Marca: ")
            ano = validar_entrada("Ano: ")
            cor = validar_entrada("Cor: ")
            cadastrar_carro(modelo, marca, ano, cor)
        elif opcao == "2":
            listar_carros()
        elif opcao == "3":
            id_carro = validar_entrada("ID do Carro: ")
            modelo = validar_entrada("Novo Modelo (ou pressione Enter para manter): ")
            marca = validar_entrada("Nova Marca (ou pressione Enter para manter): ")
            ano = validar_entrada("Novo Ano (ou pressione Enter para manter): ")
            cor = validar_entrada("Nova Cor (ou pressione Enter para manter): ")
            atualizar_carro(id_carro, modelo or None, marca or None, int(ano) if ano else None, cor or None)
        elif opcao == "4":
            id_carro = validar_entrada("ID do Carro: ")
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

        opcao = validar_entrada("Escolha uma opção: ")

        if opcao == "1":
            id_cliente = validar_entrada("ID do Cliente: ")
            id_carro = validar_entrada("ID do Carro: ")
            data_inicio = validar_entrada("Data de Início (YYYY-MM-DD): ")
            data_fim = validar_entrada("Data de Fim (YYYY-MM-DD): ")
            valor_total = float(input("Valor Total: "))
            realizar_aluguel(id_cliente, id_carro, data_inicio, data_fim, valor_total)
        elif opcao == "2":
            listar_alugueis()
        elif opcao == "3":
            id_aluguel = validar_entrada("ID do Aluguel: ")
            data_inicio = validar_entrada("Nova Data de Início (YYYY-MM-DD ou Enter para manter): ")
            data_fim = validar_entrada("Nova Data de Fim (YYYY-MM-DD ou Enter para manter): ")
            valor_total = validar_entrada("Novo Valor Total (ou Enter para manter): ")
            atualizar_aluguel(id_aluguel, data_inicio or None, data_fim or None, float(valor_total) if valor_total else None)
        elif opcao == "4":
            id_aluguel = validar_entrada("ID do Aluguel: ")
            deletar_aluguel(id_aluguel)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_exportacao():
    while True:
        print("\n--- Exportar para JSON ou Excel ---")
        print("1. Exportar para JSON")
        print("2. Exportar para Excel")
        print("0. Voltar")
        
        opcao = validar_entrada("Escolha uma opção: ")
        
        if opcao == "1":
            export_to_json()
        elif opcao == "2":
            export_to_excel()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
