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
        print("4. Exportar Arquivo para JSON")
        print("5. Exportar Arquivo para Excel")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        opcao_validada = validar_entrada(opcao, "int")  # Passando o tipo correto
        if opcao_validada is None:
            print("Entrada inválida, tente novamente.")
        else:
            print(f"Você escolheu a opção {opcao_validada}.")
            if opcao == "1":
                menu_clientes()
            elif opcao == "2":
                menu_carros()
            elif opcao == "3":
                menu_alugueis()
            elif opcao == "4":
                menu_exportacao_json()
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
        opcao_validada = validar_entrada(opcao, "int")  # Passando o tipo correto
        if opcao_validada is None:
            print("Entrada inválida, tente novamente.")
        else:
            print(f"Você escolheu a opção {opcao_validada}.")
            if opcao == "1":
                nome = input("Nome do cliente: ")
                nome_validado = validar_entrada(nome, "str")
                if nome_validado is None:
                    print("Nome inválido. Tente novamente.")
                    return

                cpf = input("CPF: ")
                cpf_validado = validar_entrada(cpf, "cpf") 
                if cpf_validado is None:
                    print("CPF inválido. Tente novamente.")
                    return

                telefone = input("Telefone: ")
                telefone_validado = validar_entrada(telefone, "str")
                if telefone_validado is None:
                    print("Telefone inválido. Tente novamente.")
                    return

                email = input("Email: ")
                email_validado = validar_entrada(email, "str")
                if email_validado is None:
                    print("Email inválido. Tente novamente.")
                    return
                # Aqui você pode continuar o processo de cadastro com os dados validados
                print(f"Cliente {nome_validado} cadastrado com sucesso!")
                cadastrar_cliente(nome, cpf, telefone, email)
            elif opcao == "2":
                listar_clientes()
            elif opcao == "3":
                id_cliente = input("ID do Cliente: ")
                id_cliente_validado = validar_entrada(id_cliente, "int")
                if id_cliente_validado is None:
                    print("ID do Cliente inválido. Tente novamente.")
                    return
                
                nome = input("Nome do cliente: ")
                nome_validado = validar_entrada(nome, "str")
                if nome_validado is None:
                    print("Nome inválido. Tente novamente.")
                    return

                cpf = input("CPF: ")
                cpf_validado = validar_entrada(cpf, "cpf") 
                if cpf_validado is None:
                    print("CPF inválido. Tente novamente.")
                    return

                telefone = input("Telefone: ")
                telefone_validado = validar_entrada(telefone, "str")
                if telefone_validado is None:
                    print("Telefone inválido. Tente novamente.")
                    return

                email = input("Email: ")
                email_validado = validar_entrada(email, "str")
                if email_validado is None:
                    print("Email inválido. Tente novamente.")
                    return
                atualizar_cliente(id_cliente, nome or None, cpf or None, telefone or None, email or None)
            elif opcao == "4":
                id_cliente = input("ID do Cliente: ")
                id_cliente_validado = validar_entrada(id_cliente, "int")
                deletar_cliente(id_cliente_validado)
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
        opcao_validada = validar_entrada(opcao, "int")  # Passando o tipo correto
        if opcao_validada is None:
            print("Entrada inválida, tente novamente.")
        else:
            print(f"Você escolheu a opção {opcao_validada}.")
            if opcao == "1":
                modelo = input("Modelo do carro: ")
                modelo_validado = validar_entrada(modelo, "str")
                if modelo_validado is None:
                    print("modelo inválido. Tente novamente.")
                    return

                marca = input("Marca: ")
                marca_validado = validar_entrada(marca, "str") 
                if marca_validado is None:
                    print("Marca inválida. Tente novamente.")
                    return

                ano = input("Ano: ")
                ano_validado = validar_entrada(ano, "int")
                if ano_validado is None:
                    print("Ano inválido. Tente novamente.")
                    return

                cor = input("Cor: ")
                cor_validado = validar_entrada(cor, "str")
                if cor_validado is None:
                    print("Cor inválida. Tente novamente.")
                    return
                # Aqui você pode continuar o processo de cadastro com os dados validados
                print(f"Carro {modelo_validado} cadastrado com sucesso!")
                cadastrar_carro(modelo, marca, ano, cor)
            elif opcao == "2":
                listar_carros()
            elif opcao == "3":
                id_carro = input("ID do Carro: ")
                id_carro_validado = validar_entrada(id_carro, "int")
                if id_carro_validado is None:
                    print("Carro inválido. Tente novamente.")
                    return
                
                modelo = input("Modelo do carro: ")
                modelo_validado = validar_entrada(modelo, "str")
                if modelo_validado is None:
                    print("modelo inválido. Tente novamente.")
                    return

                marca = input("Marca: ")
                marca_validado = validar_entrada(marca, "str") 
                if marca_validado is None:
                    print("Marca inválida. Tente novamente.")
                    return

                ano = input("ano: ")
                ano_validado = validar_entrada(ano, "int")
                if ano_validado is None:
                    print("Ano inválido. Tente novamente.")
                    return

                cor = input("Cor: ")
                cor_validado = validar_entrada(cor, "str")
                if cor_validado is None:
                    print("Cor inválida. Tente novamente.")
                    return
                atualizar_carro(id_carro, modelo or None, marca or None, int(ano) if ano else None, cor or None)
            elif opcao == "4":
                id_carro = input("ID do Carro: ")
                id_carro_validado = validar_entrada(id_carro, "int")
                deletar_carro(id_carro_validado)
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
        opcao_validada = validar_entrada(opcao, "int")  # Passando o tipo correto
        if opcao_validada is None:
            print("Entrada inválida, tente novamente.")
        else:
            print(f"Você escolheu a opção {opcao_validada}.")
            if opcao == "1":
                id_cliente = input("ID do Cliente: ")
                id_cliente_validado = validar_entrada(id_cliente, "int")
                if id_cliente_validado is None:
                    print("ID do Cliente inválido. Tente novamente.")
                    return
                
                id_carro = input("ID do Carro: ")
                id_carro_validado = validar_entrada(id_carro, "int")
                if id_carro_validado is None:
                    print("ID do Carro inválido. Tente novamente.")
                    return
                
                data_inicio = input("Data de Início (YYYY-MM-DD): ")
                
                data_fim = input("Data de Fim (YYYY-MM-DD): ")
                
                valor_total = float(input("Valor Total: "))
                valor_total_validado = validar_entrada(valor_total, "float")
                realizar_aluguel(id_cliente, id_carro, data_inicio, data_fim, valor_total)
            elif opcao == "2":
                listar_alugueis()
            elif opcao == "3":
                id_aluguel = input("ID do Aluguel: ")
                id_aluguel_validado = validar_entrada(id_aluguel, "int")
                if id_aluguel_validado is None:
                    print("ID de Aluguel inválido. Tente novamente.")
                    return
                
                id_cliente = input("ID do Cliente: ")
                id_cliente_validado = validar_entrada(id_cliente, "int")
                if id_cliente_validado is None:
                    print("ID do Cliente inválido. Tente novamente.")
                    return
                
                id_carro = input("ID do Carro: ")
                id_carro_validado = validar_entrada(id_carro, "int")
                if id_carro_validado is None:
                    print("ID do Carro inválido. Tente novamente.")
                    return
                
                data_inicio = input("Data de Início (YYYY-MM-DD): ")
                
                data_fim = input("Data de Fim (YYYY-MM-DD): ")
                
                valor_total = input("Digite o valor total do aluguel: ")
                valor_total_validado = validar_entrada(valor_total, "float")
                if valor_total_validado is None:
                    print("Valor inválido. Tente novamente.")
                    return
                atualizar_aluguel(id_aluguel, id_cliente, id_carro, data_inicio or None, data_fim or None, float(valor_total) if valor_total else None)
            elif opcao == "4":
                id_aluguel = input("ID do Aluguel: ")
                id_aluguel_validado = validar_entrada(id_aluguel, "int")
                deletar_aluguel(id_aluguel_validado)
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
            
def menu_exportacao_json():
    print("Escolha uma opção de exportação:")
    print("1. Exportar clientes para JSON")
    print("2. Exportar carros para JSON")
    print("3. Exportar alugueis para JSON")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clientes = listar_clientes()  # Substitua com a função que retorna os clientes
        export_to_json(clientes, "clientes.json")
    elif opcao == "2":
        carros = listar_carros()  # Substitua com a função que retorna os carros
        export_to_json(carros, "carros.json")
    elif opcao == "3":
        alugueis = listar_alugueis()  # Substitua com a função que retorna os alugueis
        export_to_json(alugueis, "alugueis.json")
    else:
        print("Opção inválida.")
        
def menu_exportacao_excel():
    print("Escolha uma opção de exportação:")
    print("1. Exportar clientes para Excel")
    print("2. Exportar carros para Excel")
    print("3. Exportar alugueis para Excel")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clientes = listar_clientes()  # Substitua com a função que retorna os clientes
        export_to_excel(clientes, "clientes.xlsx")
    elif opcao == "2":
        carros = listar_carros()  # Substitua com a função que retorna os carros
        export_to_excel(carros, "carros.xlsx")
    elif opcao == "3":
        alugueis = listar_alugueis()  # Substitua com a função que retorna os alugueis
        export_to_excel(alugueis, "alugueis.xlsx")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
