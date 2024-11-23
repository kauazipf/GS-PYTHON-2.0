from database import get_connection, close_connection

# CREATE
def cadastrar_carro(modelo, marca, ano, cor):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()

        query = """
        INSERT INTO carros (modelo, marca, ano, cor)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (modelo, marca, ano, cor))
        conexao.commit()

        print("Carro cadastrado com sucesso!")
    except Exception as erro:
        print(f"Erro ao cadastrar carro: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o MySQL foi encerrada.")



# READ
def listar_carros(status=None):
    try:
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        # Consulta SQL corrigida
        if status is not None:
            query = "SELECT * FROM carros WHERE status = %s"
            cursor.execute(query, (status,))
        else:
            query = "SELECT * FROM carros"
            cursor.execute(query)

        carros = cursor.fetchall()
        
        if carros:
            print("Lista de carros:")
            for carro in carros:
                print(carro)
        else:
            print("Nenhum carro encontrado.")

        return carros

    except Exception as erro:
        print(f"Erro ao listar carros: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o MySQL foi encerrada.")


# UPDATE
def atualizar_carro(id_carro, modelo=None, marca=None, ano=None, cor=None):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()

        # Atualizando os valores utilizando COALESCE para lidar com valores nulos
        query = """
        UPDATE carros
        SET 
            modelo = COALESCE(%s, modelo),
            marca = COALESCE(%s, marca),
            ano = COALESCE(%s, ano),
            cor = COALESCE(%s, cor)
        WHERE id_carro = %s  -- Certifique-se de que o campo 'id' está presente na tabela
        """
        parametros = (modelo, marca, ano, cor, id_carro)

        cursor.execute(query, parametros)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Carro atualizado com sucesso!")
        else:
            print("Nenhum carro encontrado com o ID fornecido.")

    except Exception as erro:
        print(f"Erro ao atualizar carro: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o MySQL foi encerrada.")

# DELETE
def deletar_carro(id_carro):
    try:
        # Conectando ao banco de dados
        conexao = get_connection()
        cursor = conexao.cursor()

        # Query para deletar o carro
        query = "DELETE FROM carros WHERE id_carro = %(id_carro)s"
        parametros = {"id_carro": id_carro}

        # Executando a consulta com os parâmetros
        cursor.execute(query, parametros)
        conexao.commit()
        print(f"Carro com ID {id_carro} deletado com sucesso!")

    except Exception as erro:
        print(f"Erro ao deletar carro: {erro}")

    finally:
        cursor.close()
        conexao.close()
