import json
import pandas as pd

def export_to_json(data, filename):
    """Exporta dados para arquivo JSON."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Dados exportados para {filename} com sucesso!")
    except Exception as e:
        print("Erro ao exportar para JSON:", e)

def export_to_excel(data, filename):
    """Exporta dados para arquivo Excel."""
    try:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Dados exportados para {filename} com sucesso!")
    except Exception as e:
        print("Erro ao exportar para Excel:", e)
