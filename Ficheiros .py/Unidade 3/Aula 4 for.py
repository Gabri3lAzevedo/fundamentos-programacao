"""
=========================================================
ISCTE - RESUMO AULA 4: Estruturas de Repetição (for)
=========================================================
Enquanto o 'while' repete consoante uma condição (True/False),
o ciclo 'for' é usado para percorrer uma sequência (um texto, 
uma lista, ou uma sequência de números definida).
Novas palavras-chave: for, in, range.
"""

# ==========================================
# 1. CICLO FOR COM TEXTOS (STRINGS)
# ==========================================
# O ciclo percorre letra a letra de uma string.
print("--- 1. Ciclo for com texto ---")
palavra = "Abracadabra"

for letra in palavra:
    if letra == 'A' or letra == 'a':
        print('Encontrei um "a"!')
print('Fim da procura!')


# ==========================================
# 2. CICLO FOR COM LISTAS
# ==========================================
# O ciclo percorre elemento a elemento de uma lista.
print("\n--- 2. Ciclo for com listas ---")
lista_de_fruta = ['Banana', 'Maçã', 'Laranja']

for fruta in lista_de_fruta:
    nletras = len(fruta) # A função len() conta quantos caracteres a palavra tem
    print(f"{fruta} tem {nletras} letras.")


# ==========================================
# 3. A INSTRUÇÃO RANGE()
# ==========================================
# O range() gera sequências numéricas muito úteis para usar com o 'for'.
# Sintaxe: range(início, fim_exclusivo, passo)
print("\n--- 3. A instrução range() ---")

print("range(10):", end=" ")
# Apenas 1 argumento: vai de 0 até ao número-1
for n in range(10):
    print(n, end=" ")
print() # Quebra de linha para ficar arrumado

print("range(1, 11, 2):", end=" ")
# 3 argumentos: começa no 1, vai até 10, e salta de 2 em 2
for n in range(1, 11, 2):
    print(n, end=" ")
print()

print("range(5, -5, -2):", end=" ")
# Contagem decrescente: começa no 5, vai até -4, saltando -2
for n in range(5, -5, -2):
    print(n, end=" ")
print()


# ==========================================
# 4. BREAK, CONTINUE E ELSE NOS CICLOS
# ==========================================
# O comportamento é exatamente igual ao que vimos no 'while'.
print("\n--- 4. Break, Continue e Else ---")
print("Quadrados perfeitos ímpares até 200:")

for n in range(1, 100):
    k = n**2
    if k % 2 == 0: 
        # Resto da divisão por 2 é zero? Então é PAR.
        continue # O 'continue' ignora o resto do código e passa para o próximo 'n'.
    elif k > 200:
        break    # Se passar de 200, o 'break' estilhaça o ciclo imediatamente.
    print(k, end=" ")
else:
    # Atenção: O 'else' num ciclo for/while SÓ CORRE se o ciclo terminar normalmente
    # (ou seja, se NUNCA bater num 'break'). Neste exemplo, o texto abaixo não aparece.
    print("Ciclo terminou")
print()


# ==========================================
# 5. CICLOS ANINHADOS (FOR DENTRO DE FOR)
# ==========================================
# Muito útil para trabalhar com tabelas ou matrizes.
# Por cada volta do ciclo de "fora", o ciclo de "dentro" faz as suas voltas todas.
print("\n--- 5. Ciclos Aninhados (Tabuadas) ---")

print("Tabuadas até 4:")
for n in range(1, 5):         # Ciclo das linhas (1 a 4)
    for m in range(1, 5):     # Ciclo das colunas (1 a 4)
        print(n * m, end=" ") # Calcula e imprime na mesma linha
    print("") # No final de cada linha, fazemos print vazio para descer a linha