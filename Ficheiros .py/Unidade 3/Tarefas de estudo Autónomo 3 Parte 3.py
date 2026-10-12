# ==========================================
# TAREFAS DE ESTUDO AUTÓNOMO 3 PARTE 3 - TRY/EXCEPT (VERSÃO SIMPLIFICADA)
# ==========================================

# --- 2 ---
print("\n--- 2. Pares de 0 a 20 (com validação) ---")
try:
    maximo = int(input("Introduza o limite máximo (ex: 20): "))
    for i in range(0, maximo + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()
except ValueError:
    print("Erro: Deve introduzir um número inteiro válido!!")


# --- 3 ---
print("\n--- 3. Contagem regressiva (com if no zero) ---")
try:
    inicio = int(input("Introduza o número de início (ex: 10): "))
    for i in range(inicio, -1, -1):
        if i == 0:
            print("0! Contagem terminada.")
        else:
            print(i, end=" ")
    print()
except ValueError:
    print("Erro: Deve introduzir um valor numérico!!")


# --- 4 ---
print("\n--- 4. Salta múltiplos de 3 ---")
try:
    limite = int(input("Introduza o intervalo máximo (ex: 20): "))
    for i in range(1, limite + 1):
        if i % 3 == 0:
            continue
        print(i, end=" ")
    print()
except ValueError:
    print("Erro: Deve introduzir um valor numérico!!")


# --- 5 ---
print("\n--- 5. Primeiro múltiplo de 7 (break) ---")
try:
    lim_sup = int(input("Introduza o limite superior (ex: 50): "))
    for i in range(1, lim_sup + 1):
        if i % 7 == 0:
            print("Primeiro múltiplo de 7 encontrado:", i)
            break
except ValueError:
    print("Erro: Valor inválido!!")


# --- 6 ---
print("\n--- 6. Ímpares de 1 a 15 ---")
try:
    max_impar = int(input("Introduza o limite máximo (ex: 15): "))
    for i in range(1, max_impar + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()
except ValueError:
    print("Erro: Valor introduzido não é numérico!!")


# --- 7 ---
print("\n--- 7. Soma de positivos até negativo ---")
soma = 0
while True:
    try:
        num = int(input("Introduza um número positivo (negativo para parar): "))
        if num < 0:
            break
        soma = soma + num
    except ValueError:
        print("Erro: Deve introduzir um valor numérico!! Tente novamente.")
print("Soma total:", soma)


# --- 8 ---
print("\n--- 8. Multiplicação de lista ignorando zeros ---")
entradas = ["2", "5", "abc", "0", "3", "4"]
produto = 1
for item in entradas:
    try:
        num = float(item)
        if num == 0:
            continue
        produto = produto * num
    except ValueError:
        print("Aviso: Valor ignorado (não é número).")
print("Produto final:", produto)


# --- 9 ---
print("\n--- 9. Primeiros N quadrados perfeitos ---")
while True:
    try:
        n = int(input("Introduza N quadrados perfeitos: "))
        for i in range(1, n + 1):
            print(i * i, end=" ")
        print()
        break
    except ValueError:
        print("Erro: Valor inválido!! Tente novamente.")


# --- 10 ---
print("\n--- 10. N quadrados perfeitos sem múltiplos de 4 ---")
while True:
    try:
        n = int(input("Introduza N quadrados perfeitos: "))
        encontrados = 0
        i = 1
        while encontrados < n:
            quadrado = i * i
            if quadrado % 4 != 0:
                print(quadrado, end=" ")
                encontrados = encontrados + 1
            i = i + 1
        print()
        break
    except ValueError:
        print("Erro: Valor inválido!!")


# --- 11 e 12 ---
print("\n--- 11 e 12. Soma de intervalo (com troca de valores) ---")
while True:
    try:
        n1 = int(input("Introduza o primeiro número: "))
        n2 = int(input("Introduza o segundo número: "))

        # Estrutura If para trocar a ordem se o utilizador colocar o maior primeiro
        if n1 > n2:
            temporario = n1
            n1 = n2
            n2 = temporario

        soma_int = 0
        for i in range(n1, n2 + 1):
            soma_int = soma_int + i
        print("Soma dos números entre limites:", soma_int)
        break
    except ValueError:
        print("Erro: Deve introduzir um valor numérico!! Tente novamente.")


# --- 13 ---
print("\n--- 13. Primeira posição da letra 'A' ---")
while True:
    texto = input("Introduza um texto: ")
    try:
        # Truque com a matéria da aula: forçamos um erro matemático para testar se o texto está vazio
        # Se o utilizador der apenas "Enter", o len(texto) é 0, causando um ZeroDivisionError!
        teste_vazio = 1 / len(texto)

        posicao = -1
        for i in range(len(texto)):
            if texto[i] == 'A' or texto[i] == 'a':
                posicao = i
                break

        if posicao != -1:
            print("A primeira letra 'A' encontra-se na posição:", posicao)
        else:
            print("O texto não contém a letra 'A'.")
        break
    except ZeroDivisionError:
        print("Erro: Não introduziu nenhum texto!!")


# --- 14 ---
print("\n--- 14. Cálculo de Fatorial ---")
while True:
    try:
        n = int(input("Introduza um número para calcular o fatorial: "))
        if n < 0:
            print("Não é possível calcular fatorial de números negativos.")
        else:
            fat = 1
            for i in range(1, n + 1):
                fat = fat * i
            print("Resultado:", fat)
            break
    except ValueError:
        print("Erro: Valor inválido!! Tente novamente.")


# ==========================================
# DESAFIOS
# ==========================================

# --- 15 ---
print("\n--- 15. Padrão Crescente ---")
while True:
    try:
        linhas = int(input("Introduza o número de linhas (ex: 5): "))
        for i in range(1, linhas + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
        break
    except ValueError:
        print("Erro: Deve introduzir um valor numérico!!")


# --- 16 ---
print("\n--- 16. Fibonacci ---")
while True:
    try:
        termos = int(input("Quantos termos de Fibonacci quer apresentar? "))
        a = 0
        b = 1
        for i in range(termos):
            print(a, end=" ")
            proximo = a + b
            a = b
            b = proximo
        print()
        break
    except ValueError:
        print("Erro: Valor numérico inválido!!")


# --- 17 ---
print("\n--- 17. Padrão Decrescente ---")
while True:
    try:
        linhas = int(input("Introduza o número inicial (ex: 5): "))
        for i in range(linhas, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
        break
    except ValueError:
        print("Erro: Deve introduzir um valor numérico!!")


# --- 18 ---
print("\n--- 18. Verificador de Primos contínuo ---")
while True:
    entrada = input("Introduza um número para testar (ou escreva 'sair'): ")
    if entrada.lower() == "sair":
        print("A encerrar...")
        break

    try:
        num = int(entrada)
        is_primo = True

        if num <= 1:
            is_primo = False
        else:
            for i in range(2, num):
                if num % i == 0:
                    is_primo = False
                    break

        if is_primo:
            print("O número", num, "É primo.")
        else:
            print("O número", num, "NÃO é primo.")

    except ValueError:
        print("Erro: Deve introduzir um valor numérico!!")