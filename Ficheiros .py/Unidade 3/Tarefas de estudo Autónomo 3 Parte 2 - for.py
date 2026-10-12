# ==========================================
# TAREFAS DE ESTUDO AUTÓNOMO 3 PARTE 2 - FOR
# ==========================================

# --- 1 ---
"""
1. Síntese Textual: Estruturas de Repetição
As estruturas de repetição (ou ciclos) permitem executar um bloco de código múltiplas vezes de forma automatizada.
Tipos existentes em Python:
- Ciclo 'while': Repete um bloco de código ENQUANTO uma condição lógica for verdadeira. É ideal para quando não sabemos exatamente o número de iterações.
- Ciclo 'for': Itera sobre uma sequência de elementos (como uma lista, uma string ou uma sequência de números gerada pela função range()). É ideal para quando sabemos o número exato de repetições pretendidas.
"""

# --- 2 ---
print("\n--- 2. Pares de 0 a 20 ---")
for i in range(0, 21, 2):
    print(i, end=" ")
print() # Quebra de linha final


# --- 3 ---
print("\n--- 3. Contagem 10 a 0 ---")
for i in range(10, -1, -1):
    print(i, end=" ")
print()


# --- 4 ---
print("\n--- 4. Salta múltiplos de 3 ---")
for i in range(1, 21):
    if i % 3 == 0:
        continue # Ignora o que está abaixo e passa para o próximo número
    print(i, end=" ")
print()


# --- 5 ---
print("\n--- 5. Primeiro múltiplo de 7 (break) ---")
for i in range(1, 51):
    if i % 7 == 0:
        print(f"O primeiro múltiplo de 7 é: {i}")
        break # Interrompe o ciclo imediatamente


# --- 6 ---
print("\n--- 6. Ímpares até 15 ---")
for i in range(1, 16, 2):
    print(i, end=" ")
print()


# --- 7 ---
print("\n--- 7. Soma até encontrar negativo ---")
soma = 0
# NOTA: O ciclo 'for' precisa de um limite máximo, usamos um range gigante (99999)
# mas dependemos do 'break' para forçar a saída assim que surgir o negativo.
for _ in range(99999): 
    num = int(input("Introduza um número positivo (negativo para parar): "))
    if num < 0:
        break
    soma += num
print(f"Soma total apresentada: {soma}")


# --- 8 ---
print("\n--- 8. Multiplicar números de uma lista ---")
lista_numeros = [2, 5, 0, 3, 0, 4]
produto = 1
for num in lista_numeros:
    if num == 0:
        continue # Ignora os zeros
    produto *= num
print(f"O produto dos números da lista {lista_numeros} (ignorando zeros) é: {produto}")


# --- 9 ---
print("\n--- 9. Primeiros N quadrados perfeitos ---")
n = int(input("Introduza o valor de N: "))
for i in range(1, n + 1):
    print(i ** 2, end=" ")
print()


# --- 10 ---
print("\n--- 10. N quadrados perfeitos (sem múltiplos de 4) ---")
n_quadrados = int(input("Introduza o valor de N quadrados pretendidos: "))
encontrados = 0

for i in range(1, 99999): # Range arbitrário grande
    quadrado = i ** 2
    if quadrado % 4 != 0:
        print(quadrado, end=" ")
        encontrados += 1
    
    if encontrados == n_quadrados:
        break # Para o ciclo mal encontre a quantidade de números desejada
print()


# --- 11 ---
print("\n--- 11. Soma entre dois limites ---")
n1 = int(input("Introduza o número menor: "))
n2 = int(input("Introduza o número maior: "))
soma_intervalo = 0
for i in range(n1, n2 + 1):
    soma_intervalo += i
print(f"Soma entre {n1} e {n2}: {soma_intervalo}")


# --- 12 ---
print("\n--- 12. Soma entre dois limites (qualquer ordem) ---")
valor1 = int(input("Introduza o primeiro número: "))
valor2 = int(input("Introduza o segundo número: "))

# A função min() e max() garantem que o range() não falha, independentemente da ordem
menor = min(valor1, valor2)
maior = max(valor1, valor2)

soma_intervalo_seguro = 0
for i in range(menor, maior + 1):
    soma_intervalo_seguro += i
print(f"A soma de todos os inteiros entre {menor} e {maior} é: {soma_intervalo_seguro}")


# --- 13 ---
print("\n--- 13. Primeira posição do 'A' ---")
texto = input("Introduza um texto: ")
posicao = -1 # Começamos com -1 que significa "não encontrado"

for i in range(len(texto)):
    if texto[i] == 'A':
        posicao = i
        break # Mal encontre o primeiro 'A', guarda a posição e para de procurar

if posicao != -1:
    print(f"O caractere 'A' surge pela primeira vez no índice: {posicao}")
else:
    print("Insucesso: O caractere 'A' não foi encontrado no texto.")


# --- 14 ---
print("\n--- 14. Cálculo do Fatorial ---")
numero_fat = int(input("Introduza um número para calcular o fatorial: "))
fatorial = 1

if numero_fat < 0:
    print("Não existe fatorial para números negativos.")
else:
    for i in range(1, numero_fat + 1):
        fatorial *= i
    print(f"O fatorial de {numero_fat}! é: {fatorial}")


# ==========================================
# DESAFIOS
# ==========================================

# --- 15 ---
print("\n--- 15. Padrão Crescente ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() # Imprime uma quebra de linha após cada nível do triângulo


# --- 16 ---
print("\n--- 16. Sequência de Fibonacci ---")
termos = int(input("Quantos termos da sequência de Fibonacci quer ver? "))
a, b = 0, 1

for _ in range(termos):
    print(a, end=" ")
    # O próximo 'a' passa a ser o 'b' atual, e o próximo 'b' é a soma de ambos
    a, b = b, a + b
print()


# --- 17 ---
print("\n--- 17. Padrão Decrescente ---")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# --- 18 ---
print("\n--- 18. Verificador de Números Primos ---")
candidato_primo = int(input("Introduza um número inteiro: "))
is_primo = True

if candidato_primo <= 1:
    is_primo = False
else:
    # Basta testar a divisão de 2 até ao número anterior (candidato_primo - 1)
    for i in range(2, candidato_primo):
        if candidato_primo % i == 0:
            is_primo = False
            break

if is_primo:
    print(f"O número {candidato_primo} É primo.")
else:
    print(f"O número {candidato_primo} NÃO é primo.")