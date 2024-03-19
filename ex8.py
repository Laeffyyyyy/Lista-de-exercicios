print("\n---Programa de Eleitores---\n")

n = (input("Insira seu nome: "))
i = int(input("Insira sua idade: "))

if i <= 16:
    print("\nVocê ainda não pode votar !")
elif i > 16 and i < 18 or i > 65:
    print("\nEleitor Facultativo !")
else:
    print("\nEleitor obrigatório !")
   
