print ("\n---TESTE DE MÉDIA---\n")

f = input("Informe sua faculdade: ")
m = float(input("Informe sua média: "))

if f == 'PUCPR' or 'Pucpr' or 'pucpr':
    if m < 4:
        print("Reprovado")
    elif m > 4 and m <= 7:
        diferenca = 7 - m
        print(f"\nVocê está de Exame Final e precisa de {diferenca:.2f}\n") 
    else:
        print("Aprovado")

elif f == 'UNICAMP' or 'Unicamp' or 'unicamp':
    if m < 5:
        diferenca = 5 - m
        print(f"\nVocê está de Exame Final e precisa de {diferenca:.2f}\n") 
    else:
        print("Aprovado")
    
