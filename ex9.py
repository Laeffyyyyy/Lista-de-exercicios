print("\n---Programa de aposentadoria---\n")

i = int(input("Informe sua idade: "))
t = int(input("Informe seu tempo de trabalho em anos: "))

if i >= 65 or t >= 35:
    print("\nSua aposentadoria ja está disponível")
elif i >= 60 and t >= 25:
    print("\nSua aposentadoria ja está disponível")
else:
    print("\nVocê ainda não pode se aposentar !")