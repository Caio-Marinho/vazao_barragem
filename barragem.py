import random
from time import sleep


def enchendo_barragem(barragem: int) -> int:
    """Adiciona entre 300 a 800 litros de água oriundas da chuva na barragem."""
    agua = random.randint(300, 800)
    barragem += agua
    print(f"Está enchendo {agua} litros. A barragem tem agora {barragem} litros.")
    return barragem


def abrir_comportas(barragem: int) -> int:
    """Elimina entre 500 a 1000 litros de água por minuto ao abrir as comportas."""
    vazao = random.randint(500, 1000)
    barragem -= vazao
    print(f"Comportas abertas: eliminando {vazao} litros. A barragem tem agora {barragem} litros.")
    return barragem


def sistema_emergencial(barragem: int) -> int:
    """Aciona o sistema emergencial, eliminando 300 litros extras além das comportas."""
    barragem -= 300
    print(f'Sistema emergencial acionado: eliminando 300 litros extras. '
          f'A barragem tem agora {barragem} litros.')
    return barragem


def gerar_relatorio(barragem: int, tempo: int) -> None:
    """Gera um relatório a cada 30 minutos com o nível atual da barragem."""
    print(f"\n--- Relatório após {tempo // 60} minutos ---")
    print(f"Nível atual da barragem: {barragem} litros.\n")


# Simulação da barragem
barragem = 0
tempo = 0
intervalo_relatorio = 30 * 60  # 30 minutos em segundos

while True:
    # A cada minuto, a barragem recebe água
    barragem = enchendo_barragem(barragem)
    sleep(1)
    tempo += 1

    # Se a barragem estiver com 100.000 litros ou mais, as comportas são abertas
    if barragem >= 100000:
        print('Barragem cheia, abrindo comportas.')
        while barragem >= 50000:  # As comportas permanecem abertas até a barragem baixar para 50.000 litros
            barragem = enchendo_barragem(barragem)  # Continua recebendo água da chuva enquanto esvazia

            if barragem >= 120000:  # Aciona o sistema emergencial se passar de 120.000 litros
                barragem = sistema_emergencial(barragem)

            # Comportas eliminam água
            barragem = abrir_comportas(barragem)

            sleep(1)
            tempo += 1

            if tempo % intervalo_relatorio == 0:  # Relatório a cada 30 minutos
                gerar_relatorio(barragem, tempo)

    # Relatório a cada 30 minutos
    if tempo % intervalo_relatorio == 0:
        gerar_relatorio(barragem, tempo)

    # Se a barragem estiver abaixo de 50.000 litros, ela começa a encher novamente
    if barragem < 50000:
        print("Barragem abaixo dos 50.000 litros...\nPreparando para encher.")
