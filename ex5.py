print("\n---PESO IDEAL---\n")

s = input("Insira seu sexo: ")
h = float(input("\nInsira sua altura em m: "))

if s == "masculino" or "Masculino":
    pi = (72.7 * h) - 58

elif s == "feminino" or "Feminino":
    pi = (62.1 * h) - 44.7

else:
    print("Sexo inválido, favor insirir: 'Masculino' ou 'Feminino'")

if pi:
    print(f"\nO peso ideal para uma pessoa de {h} metro de altura e sexo {s} é {pi:.2f} kg.")


