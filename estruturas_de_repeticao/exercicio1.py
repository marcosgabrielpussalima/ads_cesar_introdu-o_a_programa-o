numero1 = 0
numero2 = 0
numero3 = 0 
print("Digite 3 números inteiros")
for i in range(0,3):
    match i:
        case 0:
             numero1 = input("Digite o primeiro número: ")
             while type(numero1) == float or type(numero1) == float:
                numero1 = float(input("Digite somente números"))
        case 1:
                     numero2 = input("Digite o primeiro número: ")
                     while type(numero2) == float or type(numero2) == float:
                        numero2 = float(input("Digite somente números"))
        case 2:
                     numero3 = input("Digite o primeiro número: ")
                     while type(numero3) == float or type(numero3) == float:
                        numero3 = float(input("Digite somente números"))

media = (numero1+numero2+numero3)/3
print(f"A média dos números informados é: {media}")
                
             
            
