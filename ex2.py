print("\n---MENU---\n")

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

equa = b**2 - 4*a*c

if equa > 0:
        print("\nExistem duas raízes reais distintas.")
elif equa == 0:
        print("\nExistem duas raízes reais iguais.")
else:
        print("\nExistem duas raízes imaginárias conjugadas.")