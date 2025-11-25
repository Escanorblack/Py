
try:
    idade = int(input("Digite a idade do nadador: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
    exit()

if idade < 5:
    print("Idade mínima para classificação é 5 anos.")
    exit()

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 11:
    categoria = "Infantil B"
elif 12 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Adultos"
else:
    categoria = "Não classificado (idade fora do intervalo esperado)"

print(f"O nadador de {idade} anos pertence à categoria: {categoria}")
