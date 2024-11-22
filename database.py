import mysql.connector
from mysql.connector import Error

def get_connection():
    """Função para conectar ao banco de dados MySQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Usuário padrão do XAMPP
            password="",  # Senha padrão do XAMPP é vazia
            database="aluguel_carros"  # Nome do banco de dados criado
        )
        if connection.is_connected():
            print("Conexão com o MySQL foi estabelecida.")
        return connection
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        raise

def close_connection(connection):
    """Função para fechar a conexão com o banco."""
    if connection.is_connected():
        connection.close()
        print("Conexão com o MySQL foi encerrada.")
