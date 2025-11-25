
try:
    nota = float(input("Digite a nota do aluno: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    exit()


if nota >= 7:
    print("O aluno está APROVADO.")
else:
    print("O aluno está REPROVADO.")
