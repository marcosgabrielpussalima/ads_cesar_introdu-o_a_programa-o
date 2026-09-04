# if
idade = 18

if idade >= 18:
    print("Maior de idade")

#identação: em estruturas condicionais e de repetição em python sempre deve ter o espaço de um tab
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = nota1+nota2+nota3
if media >= 7:
    print(f"Aprovado com a média: {media}")
else:
    print("Reprovado")