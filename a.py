def par():
    num1 = int(input("Digite um número par: "))
    if num1 % 2 == 0:
        num2 = int(input("Digite um número par: "))
        if num2 %2 == 0:
            if num1 > num2:
                print(f"{num1} é maior")
                return num1
            else:
                print(f"{num2} é maior")
                return num2

def impar():
    n1 = int(input("Digite um número ímpar: "))
    if n1 % 2 != 0:
        n2 = int(input("Digite um número ímpar: "))
        if n2 % 2 != 0:
            if n1 > n2:
                print(f"{n1} é maior")
                return n1
            else:
                print(f"{n2} é maior") 
                return n2         
            
calculo = par() + impar()
print(f"essa é a soma dos maior números pares e ímpares: {calculo}")