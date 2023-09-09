nome_funcionario = input()
H = int(input())
V = float(input())
salario = H * V

print(nome_funcionario)
print("R$", "{:.2f}".format(salario))