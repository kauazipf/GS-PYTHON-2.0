from datetime import datetime

def validar_entrada(texto, tipo):
    """Valida a entrada do usuário."""
    while True:
        try:
            if tipo == int:
                return int(input(texto))
            elif tipo == str:
                valor = input(texto).strip()
                if valor == "":
                    raise ValueError("A entrada não pode estar vazia.")
                return valor
            elif tipo == datetime:
                return datetime.strptime(input(texto), "%Y-%m-%d")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
