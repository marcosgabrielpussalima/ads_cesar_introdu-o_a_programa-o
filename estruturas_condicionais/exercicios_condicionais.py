'''
nome = input("digite o seu número")
idade = input("digite o sua idade")
if(idade>18):
    print("Menor de idade")
else: 
    print("Maior de idade")
'''
'''
#exercico 2
numero = int(input("digite um número: "))
if numero % 2 == 1:
    print("Seu número é impar")
else:
   print("Seu número é par")
   '''
#exercicio3
salario = float(input("Digite seu salário:"))
if(salario<1500):
    aumento = 15
    valorAumento = (salario*aumento)/100
    novoSalario = (salario+valorAumento)
    print(f"Seu salário inicial é {salario}, seu aumento foi de {aumento} porcento, de {valorAumento} reais, e seu novo salário é: {novoSalario} p")
    salario = float(input("Digite seu salário:"))
if(salario>1500 and salario<=3000):
    aumento = 10
    valorAumento = (salario*aumento)/100
    novoSalario = (salario+valorAumento)
    print(f"Seu salário inicial é {salario}, seu aumento foi de {aumento} porcento, de {valorAumento} reais, e seu novo salário é: {novoSalario} p")
    salario = float(input("Digite seu salário:"))
if(salario>3000 and salario<=5000):
    aumento = 7
    valorAumento = (salario*aumento)/100
    novoSalario = (salario+valorAumento)
    print(f"Seu salário inicial é {salario}, seu aumento foi de {aumento} porcento, de {valorAumento} reais, e seu novo salário é: {novoSalario} p")

if(salario>5000):
    aumento = 5
    valorAumento = (salario*aumento)/100
    novoSalario = (salario+valorAumento)
    print(f"Seu salário inicial é {salario}, seu aumento foi de {aumento} porcento, de {valorAumento} reais, e seu novo salário é: {novoSalario} p")
    