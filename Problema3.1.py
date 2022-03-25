entrada = input("Digite um numero que deseja saber se é PAR ou IMPAR")

num = int(entrada)

resto = num %2

if resto == 0:
    print(num, "É par")
else:
    print(num, "É impar")