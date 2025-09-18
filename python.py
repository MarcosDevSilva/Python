import random
contador = 0
while contador < 5:
    numero = random.randint(1,100)
    palpite = input("digite um valor (1 a 100): ")
    palpite = int(palpite)
    diferenca = numero - palpite


    if diferenca == 0:
        print("vc acertou.")
        break
    elif diferenca > 0:
        if diferenca <= 10:
            print("Vc erro o numero e maior (esta quente1)")
        else:
            print("Vc erro o numero e maior (esta frio2)")

    else:
        if abs(diferenca) <=10:
            print("vc errou o numero e menor (esta quente3)")
        else: 
            print("vc errou o numero e menor (esta frio4)")
    contador = contador +1
    print("O numero é %s"% numero)
print("O numero é %s"% numero)