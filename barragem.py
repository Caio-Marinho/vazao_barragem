import random
from time import sleep
barragem = 0
while True:
    agua = random.randint(300, 800)
    barragem += agua
    print(f"Está enchendo {agua} Litros a barragem tem agora {barragem} Litros.")
    sleep(1)
    while barragem >= 50000:
        if barragem >= 100000:
            print('Barragem cheia, abrindo comportas')
            if barragem >= 120000:
                vazao = random.randint(500, 1000)
                barragem -= (vazao + 300)
                print(f'Sistema emergencial acionado : Vazão de {barragem} litros\nBarragem secando...')
                sleep(1)
            else:
                vazao = random.randint(500, 1000)
                barragem -= vazao
                print(f"Está secando...\n{vazao} Litros a barragem tem agora {barragem} Litros.")
                sleep(1)
        agua = random.randint(300, 800)
        barragem += agua
        print(f"Está enchendo {agua} Litros a barragem tem agora {barragem} Litros.")
        sleep(1)
    if barragem < 50000:
        print("Barragem a baixo dos 50 mil litros...\nPreparando para encher")
