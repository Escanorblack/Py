
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))


operador = input("Digite o operador (+, -, *, /): \n + para soma \n - para subtração \n * para multiplicação \n / para divisão \n")


resultado = None

if operador == "+":
    resultado = n1 + n2
    print(f"O resultado da soma é: {resultado}")

elif operador == "-":
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")

elif operador == "*":
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")

elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Erro: Operador inválido. Por favor, use +, -, * ou /.")
