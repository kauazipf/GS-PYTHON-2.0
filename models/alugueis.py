from database import get_connection, close_connection

# CREATE
def realizar_aluguel(id_cliente, id_carro, data_inicio, data_fim, valor_total):
    try:
        # Conexão com o banco de dados
        conexao = get_connection()
        cursor = conexao.cursor()

        # Query para inserir um aluguel
        query = """
        INSERT INTO alugueis (id_cliente, id_carro, data_inicio, data_fim, valor_total)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        # Executar o comando SQL com os valores
        cursor.execute(query, (id_cliente, id_carro, data_inicio, data_fim, valor_total))
        
        # Commit para salvar as alterações no banco
        conexao.commit()
        
        print("Aluguel cadastrado com sucesso!")
    
    except Exception as erro:
        print(f"Erro ao realizar o aluguel: {erro}")
    finally:
        # Fechar a conexão com o banco
        cursor.close()
        conexao.close()

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
        else:
            print("Nenhum aluguel encontrado.")
    except Exception as e:
        print("Erro ao listar aluguéis:", e)
    finally:
        close_connection(connection)

from database import get_connection, close_connection

# UPDATE
def atualizar_aluguel(id_aluguel, id_cliente=None, id_carro=None, data_inicio=None, data_fim=None, valor_total=None):
    try:
        # Conexão com o banco de dados
        conexao = get_connection()
        cursor = conexao.cursor()

        # Verificar se o id_cliente existe na tabela clientes
        if id_cliente:
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE id_cliente = %s", (id_cliente,))
            if cursor.fetchone()[0] == 0:
                print(f"Erro: O id_cliente {id_cliente} não existe na tabela clientes.")
                return

        # Construção da query de atualização
        query = """
        UPDATE alugueis
        SET
            id_cliente = COALESCE(%s, id_cliente),
            id_carro = COALESCE(%s, id_carro),
            data_inicio = COALESCE(%s, data_inicio),
            data_fim = COALESCE(%s, data_fim),
            valor_total = COALESCE(%s, valor_total)
        WHERE id_aluguel = %s
        """

        # Passando os parâmetros para a execução da query
        parametros = (id_cliente, id_carro, data_inicio, data_fim, valor_total, id_aluguel)
        cursor.execute(query, parametros)

        # Commit para aplicar as alterações no banco de dados
        conexao.commit()

        print("Aluguel atualizado com sucesso!")
    
    except Exception as erro:
        print(f"Erro ao atualizar aluguel: {erro}")
    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()


# DELETE
def deletar_aluguel(id_aluguel):
    try:
        # Conectando ao banco de dados
        conexao = get_connection()
        cursor = conexao.cursor()

        # Query para remover o aluguel
        query = "DELETE FROM alugueis WHERE id_aluguel = %(id_aluguel)s"
        parametros = {"id_aluguel": id_aluguel}

        # Executando a consulta com os parâmetros
        cursor.execute(query, parametros)
        conexao.commit()
        print(f"Aluguel com ID {id_aluguel} removido com sucesso!")

    except Exception as erro:
        print(f"Erro ao remover aluguel: {erro}")

    finally:
        cursor.close()
        conexao.close()
