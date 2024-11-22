from database import get_connection, close_connection

# CREATE
def realizar_aluguel(id_cliente, id_carro, data_inicio, data_fim, valor_total):
    """Realiza um aluguel."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO alugueis (id_cliente, id_carro, data_inicio, data_fim, valor_total)
        VALUES (:id_cliente, :id_carro, :data_inicio, :data_fim, :valor_total)
        """
        cursor.execute(query, {
            'id_cliente': id_cliente, 'id_carro': id_carro,
            'data_inicio': data_inicio, 'data_fim': data_fim, 'valor_total': valor_total
        })

        # Atualizar status do carro
        query_update = "UPDATE carros SET status = 'Indisponível' WHERE id_carro = :id_carro"
        cursor.execute(query_update, {'id_carro': id_carro})

        connection.commit()
        print("Aluguel realizado com sucesso!")
    except Exception as e:
        print("Erro ao realizar aluguel:", e)
    finally:
        close_connection(connection)

# READ
def listar_alugueis():
    """Lista todos os aluguéis realizados."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT alugueis.id_aluguel, clientes.nome, carros.modelo, alugueis.data_inicio, alugueis.data_fim, alugueis.valor_total
        FROM alugueis
        JOIN clientes ON alugueis.id_cliente = clientes.id_cliente
        JOIN carros ON alugueis.id_carro = carros.id_carro
        """
        cursor.execute(query)
        alugueis = cursor.fetchall()
        for aluguel in alugueis:
            print(aluguel)
    except Exception as e:
        print("Erro ao listar aluguéis:", e)
    finally:
        close_connection(connection)

from database import get_connection, close_connection

# UPDATE
def atualizar_aluguel(id_aluguel, data_inicio=None, data_fim=None, valor_total=None):
    """Atualiza informações de um aluguel."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE alugueis
        SET data_inicio = COALESCE(:data_inicio, data_inicio),
            data_fim = COALESCE(:data_fim, data_fim),
            valor_total = COALESCE(:valor_total, valor_total)
        WHERE id_aluguel = :id_aluguel
        """
        cursor.execute(query, {
            'data_inicio': data_inicio, 'data_fim': data_fim, 'valor_total': valor_total, 'id_aluguel': id_aluguel
        })
        connection.commit()
        print("Aluguel atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar aluguel:", e)
    finally:
        close_connection(connection)

# DELETE
def deletar_aluguel(id_aluguel):
    """Remove um aluguel do sistema e atualiza o status do carro para 'Disponível'."""
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Obter ID do carro associado ao aluguel
        query_get_carro = "SELECT id_carro FROM alugueis WHERE id_aluguel = :id_aluguel"
        cursor.execute(query_get_carro, {'id_aluguel': id_aluguel})
        result = cursor.fetchone()
        if not result:
            print("Aluguel não encontrado.")
            return

        id_carro = result[0]

        # Remover aluguel
        query_delete = "DELETE FROM alugueis WHERE id_aluguel = :id_aluguel"
        cursor.execute(query_delete, {'id_aluguel': id_aluguel})

        # Atualizar status do carro para 'Disponível'
        query_update_carro = "UPDATE carros SET status = 'Disponível' WHERE id_carro = :id_carro"
        cursor.execute(query_update_carro, {'id_carro': id_carro})

        connection.commit()
        print("Aluguel removido com sucesso!")
    except Exception as e:
        print("Erro ao remover aluguel:", e)
    finally:
        close_connection(connection)
