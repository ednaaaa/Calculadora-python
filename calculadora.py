# calculadora.py

# Pede o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Pede a operação
operador = input("Digite a operação (+, -, *, /): ")

# Pede o segundo número
num2 = float(input("Digite o segundo número: "))

# Faz o cálculo de acordo com a operação
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 == 0:
        resultado = "Erro! Divisão por zero."
    else:
        resultado = num1 / num2
else:
    resultado = "Operação inválida."

# Mostra o resultado
print("Resultado:", resultado)
