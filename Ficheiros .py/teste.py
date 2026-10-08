import random
MAX_TENTATIVAS = 10
choice = int(input(f"Escolha um número (Tentativa 1/{MAX_TENTATIVAS}): "))
NUMERO_CERTO = random.randint(1, 100)


tentativas = 1
while choice != NUMERO_CERTO and tentativas < MAX_TENTATIVAS:
    tentativas += 1
    if choice < NUMERO_CERTO:
        print(f"Errado! O número certo é maior que {choice}. (Tentativa {tentativas}/{MAX_TENTATIVAS})")
    else:
        print(f"Errado! O número certo é menor que {choice}. (Tentativa {tentativas}/{MAX_TENTATIVAS})")
    choice = int(input(f"Escolha outro número (Tentativa {tentativas}/{MAX_TENTATIVAS}): "))
if choice == NUMERO_CERTO:
    print("Acertou! O número certo é", NUMERO_CERTO)
if tentativas == MAX_TENTATIVAS:
    if choice == NUMERO_CERTO:
        print("Acertas-te o numero na ultima tentativa!")
    else:
        print(f"Acabaram as tentativas! O número certo era {NUMERO_CERTO}.")
        print("Fim do jogo!")