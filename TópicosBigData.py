#01
print("ola mundo")

#02
numero = int(input("digite um número: "))
print(f"seu número é {numero}")

#03
n1 = int(input("Digite sua nota: "))
n2 = int(input("Digite sua nota: "))
n3 = int(input("Digite sua nota: "))
n4 = int(input("Digite sua nota: "))

media = (n1+n2+n3+n4)/4

print(f"sua nota é {media}")

if media >= 6:
    print("aprovado")
else:
    print("reprovado")

#04
metros = int(input("digite quantos metros: "))

calculo = metros*100

print(f"você tem {calculo} centimetros")

#05

raio = float(input("Digite o raio do círculo: "))

area = 3.14 * (raio**2)

print(f"a área do círculo é {area}")

#06

comprimento = float(input("Digite o comprimento do quadrado: "))

area = comprimento**2

print(f"A área do quadrado é {area}")

#07

valorPorHora = float(input("Quanto você ganha por hora? "))
HorasTrabalhadas = float(input("Quantas horas você trabalha? "))

sálario = valorPorHora*HorasTrabalhadas*30

print(f"eu ganho isso por hora: {valorPorHora}reias e trabalho: {HorasTrabalhadas}horas, e Ganho {sálario} reais")

#08

fahrenheit = float(input("Quantos graus fahrenheit? "))

celsius = 5 * ((fahrenheit-32)/9)

print(celsius)

#09

p = int(input("Digite um número inteiro: "))
s = int(input("Digite um número inteiro: "))
t = float(input("Digite um número real: "))

#A
a = p * 2 * (s/2)
print(f"o produto do dobro do primeiro com metade do segundo é: {a}")

#B
b = p * 3 + t
print(f"a soma do triplo do primeiro com o terceiro é: {b} ")

#C
c = t ** 3
print(f"o terceiro elevado ao cubo é: {c}")

#10

altura = float(input("Digite sua altura: "))

pesoideal = (72.7*altura) - 58

print(f"O seu peso ideal é: {pesoideal}kg")