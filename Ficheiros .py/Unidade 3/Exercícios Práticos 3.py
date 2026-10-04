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
print("\n--- 12 ---")
