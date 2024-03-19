print ("\n---TESTE DE MÉDIA---\n")

m = float(input("Insira aqui a sua Média: "))
if m < 4:
    print("Reprovado")
elif m > 4 and m < 7:
    diferenca = 7 - m
    print(f"\nVocê está de Exame Final e precisa de {diferenca:.2f}\n") #.2f pega somente 2 casas decimais 
else:
    print("Aprovado")