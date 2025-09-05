numero = 10
palpite = input("digite um valor: ")
palpite = int(palpite)
diferenca = numero - palpite


if diferenca == 0:
    print("vc acertou.")
elif diferenca > 0:
    print("Vc erro o numero e maior")

else:
    print("vc errou o numero e maior")