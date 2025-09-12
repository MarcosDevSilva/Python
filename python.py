contador = 0
while contador < 5:
    numero = 10
    palpite = input("digite um valor (1 a 100): ")
    palpite = int(palpite)
    diferenca = numero - palpite


    if diferenca == 0:
        print("vc acertou.")
        break
    elif diferenca > 0:
        if diferenca <= 10:
            print("Vc erro o numero e maior (esta quente)")
        else: 
            print("Vc erro o numero e maior (esta frio)")

    else:
        if abs(diferenca) <=10:
            print("vc errou o numero e maior (esta quente)")
        else: 
            print("vc errou o numero e maior (esta frio)")
    contador = contador +1