# --- 1 e 2---
print("\n--- 1 ---")
idade = int(input("Introduza a sua idade: "))

if idade >= 18:
    print("É maior de idade.")
else:
    print("É menor de idade.")


# --- 3 ---
print("\n--- 3 ---")
stock_bananas = 10
preco_bananas = 0.90
bananas_estao_boas = True

if stock_bananas > 0:
    if preco_bananas < 1.00:
        if bananas_estao_boas:
            print("Comprar bananas pois há stock, o preço é acessível e estão boas.")
        else:
            print("Não comprar bananas: não estão boas.")
    else:
        print("Não comprar bananas: preço elevado.")
else:
    print("Não comprar bananas: sem stock.")


# --- 4 ---
print("\n--- 4 ---")
idade_pessoa = int(input("Introduza a idade: "))

if idade_pessoa < 13:
    print("Estás na categoria Criança")
elif 13 <= idade_pessoa < 18:
    print("Estás na categoria Adolescente")
elif 18 <= idade_pessoa < 50:
    print("Estás na categoria Adulto")
elif 50 <= idade_pessoa < 65:
    print("Estás na categoria Adulto Premium")
else:
    print("Estás na categoria Idoso")


# --- 5 ---
print("\n--- 5 ---")
fez_exame = input("Fez exame? (sim/não): ")
if fez_exame == "sim":
    nota = float(input("Qual foi a nota? "))
    if nota >= 9.5:
        print("Aprovado na UC")
    else:
        print("Fazer recurso")
        nota_recurso = float(input("Qual foi a nota do recurso? "))
        if nota_recurso >= 9.5:
            print("Aprovado na UC")
        else:
            print("Reprovado na UC")
else:
    print("Reprovado na UC")


# --- 6 ---
print("\n--- 6 ---")
i = 1
while i <= 10:
    print(i)
    i = i + 1
print("Fim")


# --- 7 ---
print("\n--- 7 ---")
i = 10
while i >= 0:
    print(i)
    i = i - 1
print("Fim")


# --- 8 ---
print("\n--- 8 ---")
i = 2
while i <= 10:
    print(i)
    i = i + 2
print("Fim")


# --- 9 ---
print("\n--- 9 ---")
i = 0
while i < 10:
    i = i + 2
    if i == 4:
        continue
    print(i)
print("Fim")


# --- 10 ---
print("\n--- 10 ---")
i = 2
while i <= 10:
    print(i)
    if i == 6:
        break
    i = i + 2
print("Fim")


# --- 11 ---
print("\n--- 11 ---")
i = 2
while i <= 10:
    print(i)
    i = i + 2 
else:
    print("Concluiu todas as iterações")


# --- 12 ---
print("\n--- 12 ---")  # Exercício 6 com For
print("Ex. 6 com For:")
for i in range(1, 11):
    print(i)
print("Fim")

# Exercício 7 com For (Ao contrário)
print("\nEx. 7 com For:")
for i in range(10, -1, -1):
    print(i)
print("Fim")

# Exercício 8 com For (Pares)
print("\nEx. 8 com For:")
for i in range(2, 11, 2):
    print(i)
print("Fim")

# Exercício 9 com For (Pares sem o 4)
print("\nEx. 9 com For:")
for i in range(2, 11, 2):
    if i == 4:
        continue
    print(i)
print("Fim")

# Exercício 10 com For (Pares até ao 6)
print("\nEx. 10 com For:")
for i in range(2, 11, 2):
    print(i)
    if i == 6:
        break
print("Fim")

# Exercício 11 com For (Else + For)
print("\nEx. 11 com For:")
for i in range(2, 11, 2):
    print(i)
else:
    print("Concluiu todas as iterações")


# --- 13 ---
print("\n--- 13 ---")
# a. Com entrada 10 o esperado era 20. O obtido seria 20.
# b. Com entrada "abc" o esperado era um erro. O obtido é um crash (ValueError).
try:
    numero = int(input("Introduza um número: "))
    print("O dobro é:", numero * 2)
except ValueError:
    print("Erro: Deve introduzir um valor numérico.")


# --- 14 ---
print("\n--- 14 ---")
# a. Com 10 esperado 1. Obtido 1.0.
# b. Com "abc" crash (ValueError).
# c. Com 0 crash (ZeroDivisionError).
try:
    numero = int(input("Introduza um número para dividir 10: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Deve introduzir um valor numérico.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")


# --- 15 ---
print("\n--- 15 ---")
try:
    numero = int(input("Introduza um número para dividir 10: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Deve introduzir um valor numérico.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    # Só apresenta o resultado se não ocorrerem exceções
    print(f"Resultado: {resultado}")
finally:
    # Apresenta a mensagem sempre
    print("Fim da execução")


# --- 16 ---
print("\n--- 16 ---")
while True:
    entrada1 = input("\nIntroduza o primeiro número (ou 'Sair'): ")
    if entrada1.lower() == "sair":
        break
        
    entrada2 = input("Introduza o segundo número (ou 'Sair'): ")
    if entrada2.lower() == "sair":
        break
        
    try:
        num1 = float(entrada1)
        num2 = float(entrada2)
        resultado = num1 / num2
    except ValueError:
        print("Erro: Deve introduzir valores numéricos válidos. Tente novamente!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Tente novamente!")
    else:
        print(f"Resultado: {resultado}")
        break # Opcional: Sai do loop se a divisão for bem-sucedida, conforme lógica de validação
    finally:
        print("Fim da execução da iteração atual.")