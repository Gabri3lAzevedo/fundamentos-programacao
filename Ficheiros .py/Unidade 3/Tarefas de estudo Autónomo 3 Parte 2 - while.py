# ==========================================
# TAREFAS DE ESTUDO AUTÓNOMO 3 PARTE 2 - WHILE
# ==========================================

# --- 1 ---
"""
1. Síntese Textual: Estruturas de Repetição (Aula 4)
As estruturas de repetição permitem executar um bloco de instruções de forma iterativa.
- Ciclo 'while': Avalia uma condição lógica antes de cada iteração. Executa o código repetidamente ENQUANTO a condição for verdadeira (True). Exige que inicializemos variáveis de controlo antes do ciclo e as atualizemos dentro do bloco para evitar ciclos infinitos.
- Ciclo 'for': Itera sobre os itens de uma sequência (listas, strings, range).
"""

# --- 2 ---
print("\n--- 2. Soma de 1 a 100 ---")
i = 1
soma_100 = 0
while i <= 100:
    soma_100 += i
    i += 1
print(f"A soma dos números de 1 a 100 é: {soma_100}")


# --- 3 ---
print("\n--- 3. Contagem 10 até 0 (com range e while) ---")
# Para usar range() num while, criamos uma lista a partir do range
numeros_regressivos = list(range(10, -1, -1))
i = 0
while i < len(numeros_regressivos):
    print(numeros_regressivos[i], end=" ")
    i += 1
print()


# --- 4 ---
print("\n--- 4. Salta múltiplos de 3 (com continue) ---")
i = 0
while i < 20:
    i += 1
    # Se o incremento estivesse depois do continue, o ciclo ficaria infinito no número 3!
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


# --- 5 ---
print("\n--- 5. Primeiro múltiplo de 7 (com break) ---")
i = 1
while i <= 50:
    if i % 7 == 0:
        print(f"O primeiro múltiplo de 7 entre 1 e 50 é: {i}")
        break
    i += 1


# --- 6 ---
print("\n--- 6. Interromper quando o número é 8 ---")
i = 1
while i <= 10:
    if i == 8:
        print("\n(Ciclo interrompido no 8)")
        break
    print(i, end=" ")
    i += 1
print()


# --- 7 ---
print("\n--- 7. Contar os dígitos de um número ---")
num_original = int(input("Introduza um número inteiro: "))
# Converter para absoluto para não falhar com números negativos
num_temp = abs(num_original)
contador_digitos = 0

if num_temp == 0:
    contador_digitos = 1
else:
    while num_temp > 0:
        contador_digitos += 1
        # Divisão inteira por 10 "corta" o último dígito a cada iteração
        num_temp //= 10
        
print(f"O número {num_original} tem {contador_digitos} dígito(s).")


# --- 8 ---
print("\n--- 8. Somar até introduzir negativo ---")
soma_positivos = 0
while True:
    num = int(input("Introduza um número positivo (negativo para parar): "))
    if num < 0:
        break
    soma_positivos += num
print(f"Soma total: {soma_positivos}")


# --- 9 ---
print("\n--- 9. Já chegámos? ---")
while True:
    resposta = input("Já chegámos? ")
    if resposta.upper() == "SIM":
        print("Finalmente!")
        break


# --- 10 ---
print("\n--- 10. Primeiros N quadrados perfeitos ---")
n = int(input("Quantos quadrados perfeitos quer ver? "))
i = 1
contagem = 0
while contagem < n:
    print(i ** 2, end=" ")
    contagem += 1
    i += 1
print()


# --- 11 ---
print("\n--- 11. N quadrados perfeitos (sem múltiplos de 4) ---")
n_quadrados = int(input("Quantos quadrados perfeitos quer (excluindo múltiplos de 4)? "))
i = 1
contagem = 0
while contagem < n_quadrados:
    quadrado = i ** 2
    if quadrado % 4 != 0:
        print(quadrado, end=" ")
        contagem += 1
    i += 1
print()


# --- 12 ---
print("\n--- 12. Soma de intervalo (menor primeiro) ---")
n_menor = int(input("Introduza o número menor: "))
n_maior = int(input("Introduza o número maior: "))

soma_int = 0
i = n_menor
while i <= n_maior:
    soma_int += i
    i += 1
print(f"Soma entre {n_menor} e {n_maior}: {soma_int}")


# --- 13 ---
print("\n--- 13. Soma de intervalo (ordem arbitrária) ---")
val1 = int(input("Introduza o primeiro número: "))
val2 = int(input("Introduza o segundo número: "))

minimo = min(val1, val2)
maximo = max(val1, val2)

soma_arbitraria = 0
i = minimo
while i <= maximo:
    soma_arbitraria += i
    i += 1
print(f"Soma entre {minimo} e {maximo}: {soma_arbitraria}")


# ==========================================
# DESAFIOS
# ==========================================

# --- 14 ---
print("\n--- 14. Padrão Crescente ---")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# --- 15 ---
print("\n--- 15. Sequência de Fibonacci ---")
termos_fibo = int(input("Quantos termos da sequência de Fibonacci quer ver? "))
a, b = 0, 1
contador_fibo = 0

while contador_fibo < termos_fibo:
    print(a, end=" ")
    a, b = b, a + b
    contador_fibo += 1
print()


# --- 16 ---
print("\n--- 16. Padrão Decrescente ---")
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1


# --- 17 ---
print("\n--- 17. Verificador de Números Primos ---")
cand_primo = int(input("Introduza um número inteiro para verificar se é primo: "))
e_primo = True

if cand_primo <= 1:
    e_primo = False
else:
    i = 2
    while i < cand_primo:
        if cand_primo % i == 0:
            e_primo = False
            break
        i += 1

if e_primo:
    print(f"O número {cand_primo} É primo.")
else:
    print(f"O número {cand_primo} NÃO é primo.")