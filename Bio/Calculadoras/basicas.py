import re

def calcular(expressao):
    expressao = expressao.replace(" ", "")
    if not re.fullmatch(r"[0-9+\-*/%.()**]+", expressao):
        print("Expressão inválida: apenas números e operadores básicos são permitidos.")
        return

    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        return resultado
    except Exception as e:
        print("Erro ao calcular:", e)

# Exemplo de uso direto

