print("\n---Par ou ímpar---\n")

p = []
i = []

while True:
    n = int(input("\nInsira um número inteiro: "))

    if n % 2 == 0:
        p.append(n)

    else:
        i.append(n)

    print("\nPar: ",p)
    print("\nÍmpar: ",i)




