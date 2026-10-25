import json
import sys
import urllib.request
from datetime import datetime

def coletar_dados_rpa():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            raw_data = json.loads(response.read().decode())

        resultado = {
            "status": "sucesso",
            "executado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dados": [
                {
                    "moeda": "USD",
                    "nome": raw_data["USDBRL"]["name"],
                    "valor_atual": float(raw_data["USDBRL"]["bid"]),
                    "variacao": float(raw_data["USDBRL"]["varBid"])
                },
                {
                    "moeda": "EUR",
                    "nome": raw_data["EURBRL"]["name"],
                    "valor_atual": float(raw_data["EURBRL"]["bid"]),
                    "variacao": float(raw_data["EURBRL"]["varBid"])
                }
            ]
        }
        return resultado

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e),
            "executado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    output = coletar_dados_rpa()
    # O print do JSON é capturado pelo n8n via stdout
    print(json.dumps(output))