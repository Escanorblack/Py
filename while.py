n1 = float(input("Digite sua nota : "))
n2 = float(input("Digite sua segunda nota: "))

while n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    if (n1 < 0 or n1 > 10):
        n1 = float(input("Nota inválida. Digite sua nota novamente: "))
    elif (n2 < 0 or n2 > 10):
        n2 = float(input("Nota inválida. Digite sua segunda nota novamente: "))

else:
    media = (n1 + n2) / 2
    print(f"Sua média é: {media:.2f}")