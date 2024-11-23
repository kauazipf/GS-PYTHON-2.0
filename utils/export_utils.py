import json
import pandas as pd

def export_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dados exportados com sucesso para {filename}")
    except Exception as e:
        print(f"Erro ao exportar para JSON: {e}")

def export_to_excel(data, filename):
    try:
        # Convertendo os dados para um DataFrame
        df = pd.DataFrame(data)
        
        # Salvando o DataFrame em um arquivo Excel
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"Dados exportados com sucesso para {filename}")
    except Exception as e:
        print(f"Erro ao exportar para Excel: {e}")
