"""
=========================================================
ISCTE - RESUMO AULA 3: Estruturas de Controlo (Decisão)
=========================================================
As estruturas de controlo permitem ramificar o código (criar 
diferentes caminhos) com base em condições lógicas (True/False).
Novas palavras-chave: if, else, elif.
"""

# ==========================================
# 1. ESTRUTURA SIMPLES (if)
# ==========================================
# Executa um bloco de código APENAS SE a condição for verdadeira.
print("--- 1. Estrutura Simples ---")
idade = 18

if idade >= 18:
    # A INDENTAÇÃO (espaço à esquerda) é obrigatória no Python!
    # É ela que diz ao programa que esta linha pertence ao 'if'.
    print("É maior de idade.")


# ==========================================
# 2. ESTRUTURA COMPOSTA (if + else)
# ==========================================
# Executa a instrução A se for verdade, ou a instrução B (else) se for falso.
print("\n--- 2. Estrutura Composta ---")
idade_voto = 16

if idade_voto >= 18:
    print("Já tens idade para votar.")
else:
    # O 'else' é a alternativa automática quando o 'if' falha.
    print("Ainda não tens idade para votar.")


# ==========================================
# 3. MÚLTIPLAS CONDIÇÕES (if + elif + else)
# ==========================================
# O 'elif' (else if) serve para testar novas condições caso a primeira falhe.
print("\n--- 3. Múltiplas Condições (elif) ---")
# Exemplo adaptado do slide 15:
idade_pessoa = 20

if idade_pessoa < 13:
    print("Criança.")
elif 13 <= idade_pessoa < 18:  # O Python permite encadear comparações assim!
    print("Adolescente.")
elif 18 <= idade_pessoa < 65:
    print("Adulto.")
else:
    print("Idoso.")


# ==========================================
# 4. ESTRUTURAS ANINHADAS (if dentro de if)
# ==========================================
# Usado para sucessões lógicas dependentes umas das outras.
# Para chegar ao final, todas as condições anteriores têm de ser verdadeiras.
print("\n--- 4. Estruturas Aninhadas ---")

preco_bananas = 0.90
stock_bananas = 5
bananas_estao_boas = True

# Lógica: Só compro bananas se estiverem baratas, houver stock e estiverem boas.
if preco_bananas <= 0.99:                   # Nível 1
    if stock_bananas > 0:                   # Nível 2
        if bananas_estao_boas == True:      # Nível 3
            print("Vou comprar as bananas!")
        else:
            print("Não compro: as bananas estão estragadas.")
    else:
        print("Não compro: não há stock.")
else:
    print("Não compro: as bananas estão muito caras.")


# ==========================================
# 🔴 REGRA DE OURO: INDENTAÇÃO
# ==========================================
"""
No Python, não usamos chavetas { } para separar blocos de código.
Usamos o avanço da linha (Tabs ou Espaços). 
Todas as instruções dentro do mesmo bloco (por exemplo, dentro do mesmo 'if')
TÊM de ter o mesmo número de espaços alinhados à esquerda, caso contrário 
o código vai dar erro de sintaxe (IndentationError).
"""