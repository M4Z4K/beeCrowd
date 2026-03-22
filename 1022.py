# Passos para calcular Máximo Divisor Comum
# 1. Divida os números por fatores primos (2, 3, 5, 7)
# 2. Se o número primo divide os fatores e o resto da divisão é 1, então guarde-o e siga para o próximo número primo
# 3.
def MDC():


expressao = "1 / 2 + 3 / 4"

n1 = int(expressao[0])
n2 = int(expressao[8])
d1 = int(expressao[4])
d2 = int(expressao[12])
operacao = expressao[6]

numerador = 0
denominador = 0

if operacao == "+":
    numerador = (n1*d2 + n2*d1)
    denominador = (d1*d2)
if operacao == "-":
    numerador = (n1*d2 - n2*d1)
    denominador = (d1*d2)
if operacao == "*":
    numerador = (n1*n2)
    denominador = (d1*d2)
if operacao == "/":
    numerador = (n1*d2)
    denominador = (n2*d1)

(numeradoSimplificado, denominadorSimplificado, mdc) = MDC(numerador, denominador, 0)

print(f"{numerador}/{denominador} = {numeradoSimplificado}/{denominadorSimplificado}")

