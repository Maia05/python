#Questão01
time1 = (input("nome do seu time: "))
time2 = (input("nome do seu time: "))

print(time1)
print(time2)

golstime1 = int(input("quantos gols seu time fez? "))
golstime2 = int(input("quantos gols seu time fez? "))

if golstime1 > golstime2:
    print(f"time1 ganhou de {golstime1} a {golstime2}")
elif golstime2 > golstime1:
    print(f"time2 ganhou de {golstime2} a {golstime1}")
else:
    print("o jogo saiu empate")

#Questão02

def ask_question(question):
    while True:
        pergunta = input(question + "sim/não: ").lower()
        if pergunta == "sim" or pergunta == "não":
            return pergunta == "sim"
        else:
         print("Por favor, responda 'sim' ou 'não'.")

sintomas = [
   "febre alta",
   "dores de cabeça",
   "dores musculares",
   "manchas vermelhas na pele"
]

nsintomas = sum(ask_question(f"tem {sintomas}?") for sintomas in sintomas)

if nsintomas >= 3:
   print("Você está com dengue e deve procurar um médico imediatamente")
else:
   print("Fique em repouso e continue observando a evolução dos sintomas")