from datetime import datetime

def validar_entrada(texto, tipo):
    """Valida a entrada do usuário."""
    while True:
        try:
            if tipo == "int":
                try:
                    return int(texto)
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
                    return None
            elif tipo == "str":
                if texto.strip() != "":  # Valida que a string não é vazia
                    return texto
                else:
                    print("Por favor, insira uma string válida.")
                    return None
            elif tipo == "cpf":
                # Validação específica para CPF
                if len(texto) == 11 and texto.isdigit():
                    return texto
                else:
                    print("CPF inválido. Deve conter 11 dígitos numéricos.")
                    return None
            elif tipo == "float":
                return float(texto)  # Converter para float
            elif tipo == datetime:
                return datetime.strptime(input(texto), "%Y-%m-%d")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
