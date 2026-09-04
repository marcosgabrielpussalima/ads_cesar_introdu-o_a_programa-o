# if
idade = 18

if idade >= 18:
    print("Maior de idade")

#identação: em estruturas condicionais e de repetição em python sempre deve ter o espaço de um tab
#desafio 1
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"Aprovado com a média: {media}")
else:
    print("Reprovado")
#desafio2
nome = input("digite seu nome")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"O aluno {nome} foi aprovado com média:{media}")

elif(media<7 and media>3):
    print(f"O aluno {nome} está em recuperação com média:{media}") 
elif(media<=3):
    print(f"O aluno {nome} está em recuperação com média:{media}") 
