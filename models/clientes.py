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
    """Atualiza informações de um cliente."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE clientes
        SET nome = COALESCE(:nome, nome),
            cpf = COALESCE(:cpf, cpf),
            telefone = COALESCE(:telefone, telefone),
            email = COALESCE(:email, email)
        WHERE id_cliente = :id_cliente
        """
        cursor.execute(query, {
            'nome': nome, 'cpf': cpf, 'telefone': telefone, 'email': email, 'id_cliente': id_cliente
        })
        connection.commit()
        print("Cliente atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar cliente:", e)
    finally:
        close_connection(connection)

# DELETE
def deletar_cliente(id_cliente):
    """Remove um cliente do sistema."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM clientes WHERE id_cliente = :id_cliente"
        cursor.execute(query, {'id_cliente': id_cliente})
        connection.commit()
        print("Cliente removido com sucesso!")
    except Exception as e:
        print("Erro ao deletar cliente:", e)
    finally:
        close_connection(connection)
