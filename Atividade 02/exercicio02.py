from exercicio01 import Lista

class Processo:
    def __init__(self, nome: str, tempo: float):
        self.nome = nome
        self.tempo = tempo
        self.tempo_restante = tempo
        self.tempo_retorno = 0
        self.tempo_espera = 0

lista_circular = Lista()

def inserir_processo(lista: Lista) -> None:
    qtd_processo = int(input("Digite a qtd de processos: "))

    for i in range(qtd_processo):
        nome = input("Digite o nome do processo:  ")
        tempo = int(input("Digite o tempo do processo: "))

        while nome == "":
            nome = input("Nome invalido, Digite o nome do processo:  ")
        while tempo <= 0:
            tempo = int(input("Tempo invalido, Digite o tempo do processo: "))

        lista.inserir(Processo(nome, tempo))

def executar_aria(lista: Lista) -> list:
    processos_concluidos = []
    tempo_global = 0

    quantum = int(input("Digite o quantum: "))
    while quantum <= 0:
        quantum = int(input("Digite o quantum: "))

    aux = lista.inicio

    while lista.tamanho > 0:
        processo = aux.dado
        proximo_no = aux.dir

        if processo.tempo_restante > quantum:
            tempo_global += quantum
            processo.tempo_restante -= quantum
        else:
            tempo_global += processo.tempo_restante
            processo.tempo_restante = 0
            processo.tempo_retorno = tempo_global
            processos_concluidos.append(processo)
            lista.remover(processo)

            if lista.tamanho == 0:
                break

        aux = proximo_no

    return processos_concluidos

def relatorio(processos_concluidos: list):

    for p in processos_concluidos:
        p.tempo_espera = p.tempo_retorno - p.tempo

    print("\nRelatório: \n")
    soma_retorno = 0
    soma_espera = 0

    for i in processos_concluidos:
        print(f"{i.nome} - Tempo Total: {i.tempo}u - Espera: {i.tempo_espera}u  - Retorno: {i.tempo_retorno}u")

        soma_retorno += i.tempo_retorno
        soma_espera += i.tempo_espera

    media_retorno = soma_retorno / len(processos_concluidos)
    media_espera = soma_espera / len(processos_concluidos)

    print(f"\nMédia| Espera: {media_espera:.2f}u - Retorno: {media_retorno:.2f}u")
    
    if media_espera <16 :
        print("ARIA reativada com sucesso.")
        print(f"Tempo médio de espera ({media_espera}) abaixo do limite crítico (16u). Synthetica está salva.")
    else: 
        print("Falha crítica confirmada. Iniciando protocolo de desligamento de emergência.")

inserir_processo(lista_circular)

processos_concluidos = executar_aria(lista_circular)

relatorio(processos_concluidos)