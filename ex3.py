print("\n---INDICADOR DE TEMPERATURA---\n")

temp = int(input("Digite aqui a temperatura em ºC de hoje: "))

if temp < 15:
    print("\nEstá Frio!!")
elif temp > 25:
    print("\nEstá calor!")
else:
    print("\nTemperatura agradável!")