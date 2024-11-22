from database import get_connection, close_connection

# CREATE
def cadastrar_carro(modelo, marca, ano, cor):
    """Cadastra um novo carro."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO carros (modelo, marca, ano, cor)
        VALUES (:modelo, :marca, :ano, :cor)
        """
        cursor.execute(query, {'modelo': modelo, 'marca': marca, 'ano': ano, 'cor': cor})
        connection.commit()
        print("Carro cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar carro:", e)
    finally:
        close_connection(connection)

# READ
def listar_carros(disponivel=True):
    """Lista carros, filtrando pela disponibilidade."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        status = 'Disponível' if disponivel else 'Indisponível'
        query = "SELECT * FROM carros WHERE status = :status"
        cursor.execute(query, {'status': status})
        carros = cursor.fetchall()
        for carro in carros:
            print(carro)
    except Exception as e:
        print("Erro ao listar carros:", e)
    finally:
        close_connection(connection)

# UPDATE
def atualizar_carro(id_carro, modelo=None, marca=None, ano=None, cor=None):
    """Atualiza informações de um carro."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE carros
        SET modelo = COALESCE(:modelo, modelo),
            marca = COALESCE(:marca, marca),
            ano = COALESCE(:ano, ano),
            cor = COALESCE(:cor, cor)
        WHERE id_carro = :id_carro
        """
        cursor.execute(query, {
            'modelo': modelo, 'marca': marca, 'ano': ano, 'cor': cor, 'id_carro': id_carro
        })
        connection.commit()
        print("Carro atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar carro:", e)
    finally:
        close_connection(connection)

# DELETE
def deletar_carro(id_carro):
    """Remove um carro do sistema."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM carros WHERE id_carro = :id_carro"
        cursor.execute(query, {'id_carro': id_carro})
        connection.commit()
        print("Carro removido com sucesso!")
    except Exception as e:
        print("Erro ao deletar carro:", e)
    finally:
        close_connection(connection)
