from collections import deque

class Aeroporto:
    def __init__(self):
        # Fila (Queue) para a Pista: Primeiro a chegar, primeiro a sair (FIFO)
        self.pista_decolagem = deque()

        # Pilha (Stack) para o Hangar: Último a entrar, primeiro a sair (LIFO)
        self.hangar_manutencao = []

    # === OPERAÇÕES DE FILA (PISTA) ===
    def entrar_pista(self, voo: str):
        self.pista_decolagem.append(voo) # Entra no final da fila
        print(f"[PISTA] Voo {voo} aguardando autorização para decolagem.")

    def autorizar_decolagem(self):
        if self.pista_decolagem:
            # popleft() remove do INÍCIO da fila (O(1))
            voo = self.pista_decolagem.popleft()
            print(f"[PISTA] Voo {voo} decolou com sucesso!")
        else:
            print("[PISTA] Pista vazia.")

    # === OPERAÇÕES DE PILHA (HANGAR) ===
    def guardar_no_hangar(self, voo: str):
        self.hangar_manutencao.append(voo) # Entra no topo da pilha
        print(f"[HANGAR] Voo {voo} entrou para manutenção.")

    def retirar_do_hangar(self):
        if self.hangar_manutencao:
            # pop() remove do FINAL da lista/topo da pilha (O(1))
            voo = self.hangar_manutencao.pop()
            print(f"[HANGAR] Voo {voo} saiu da manutenção e está liberado.")
        else:
            print("[HANGAR] Hangar vazio.")

# Simulador Executável
if __name__ == "__main__":
    print("=== SIMULADOR DE AEROPORTO (PYTHON) ===\n")
    meu_aeroporto = Aeroporto()

    # Testando a Fila (Pista)
    meu_aeroporto.entrar_pista("GOL123")
    meu_aeroporto.entrar_pista("LATAM456")
    meu_aeroporto.entrar_pista("AZUL789")

    meu_aeroporto.autorizar_decolagem() # Sai GOL123
    meu_aeroporto.autorizar_decolagem() # Sai LATAM456

    print("-" * 30)

    # Testando a Pilha (Hangar)
    meu_aeroporto.guardar_no_hangar("GOL_QUEBRADO_1")
    meu_aeroporto.guardar_no_hangar("LATAM_QUEBRADO_2")

    # Sai o LATAM_QUEBRADO_2 primeiro, pois está na frente da porta (LIFO)
    meu_aeroporto.retirar_do_hangar()