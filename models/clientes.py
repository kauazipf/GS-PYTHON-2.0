from database import get_connection, close_connection

# CREATE
def cadastrar_cliente(nome, cpf, telefone, email):
    """Cadastra um novo cliente no sistema."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO clientes (nome, cpf, telefone, email)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nome, cpf, telefone, email))
        connection.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar cliente:", e)
    finally:
        close_connection(connection)

# READ
def listar_clientes():
    """Lista todos os clientes cadastrados."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM clientes"
        cursor.execute(query)
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)
    except Exception as e:
        print("Erro ao listar clientes:", e)
    finally:
        close_connection(connection)

# UPDATE
def atualizar_cliente(id_cliente, nome=None, cpf=None, telefone=None, email=None):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()

        # SQL corrigido com COALESCE e usando o nome da coluna "id_cliente" (ajuste conforme necessário)
        query = """
        UPDATE clientes
        SET 
            nome = COALESCE(%s, nome),
            cpf = COALESCE(%s, cpf),
            telefone = COALESCE(%s, telefone),
            email = COALESCE(%s, email)
        WHERE id_cliente = %s
        """

        # Montando os parâmetros como uma tupla
        parametros = (nome, cpf, telefone, email, id_cliente)

        cursor.execute(query, parametros)
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Cliente com ID {id_cliente} atualizado com sucesso!")
        else:
            print(f"Nenhum cliente encontrado com ID {id_cliente}. Nenhuma alteração realizada.")

    except Exception as erro:
        print(f"Erro ao atualizar cliente: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o MySQL foi encerrada.")




# DELETE
def deletar_cliente(id_cliente):
    try:
        # Conectando ao banco de dados
        conexao = get_connection()
        cursor = conexao.cursor()

        # Query para deletar o cliente
        query = "DELETE FROM clientes WHERE id_cliente = %(id_cliente)s"
        parametros = {"id_cliente": id_cliente}

        cursor.execute(query, parametros)
        conexao.commit()
        print(f"Cliente com ID {id_cliente} deletado com sucesso!")

    except Exception as erro:
        print(f"Erro ao deletar cliente: {erro}")

    finally:
        cursor.close()
        conexao.close()
