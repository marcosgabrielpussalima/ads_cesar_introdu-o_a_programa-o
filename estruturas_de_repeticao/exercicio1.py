numero1 = 0
numero2 = 0
numero3 = 0 
print("Digite 3 números inteiros")
for i in range(0,3):
    match i:
        case 0:
             numero1 = input("Digite o primeiro número")
             while isinstance(numero1,float) == True or isinstance(numero1,int) == True:
                numero1 = input("Digite somente números")
                float(numero1)
        case 1:
                     numero2 = input("Digite o primeiro número")
                     while isinstance(numero2,float) == True or isinstance(numero2,int) == True:
                        numero2 = input("Digite somente números")
                        float(numero2)
        case 2:
                     numero3 = input("Digite o primeiro número")
                     while isinstance(numero3,float) == True or isinstance(numero3,int):
                        numero3 = input("Digite somente números")
                        float(numero3)
media = (numero1+numero2+numero3)/3
print(f"A média dos números informados é: {media}")
                
             
            
