import random
# --- Ex 1 ---
print("\n--- Ex 1 ---")
lista = random.sample(range(1, 51), 5)

NUM_MAX_TENTATIVAS = 3
num_tentativas = 0
tentativa = int(input(f"Tenta adivinhar um dos 5 numeros da lista (1-50)(num da tentativa = {num_tentativas}/{NUM_MAX_TENTATIVAS}): "))

while num_tentativas <= NUM_MAX_TENTATIVAS:
    if tentativa in lista:
        print("Acertou! A lista era:", lista, "e a sua tentativa foi:", tentativa, "Parabens!")
        break
    else:
        num_tentativas += 1
        if num_tentativas < NUM_MAX_TENTATIVAS:
            tentativa = int(input(f"Tenta adivinhar um dos 5 numeros da lista (1-50) (num da tentativa = {num_tentativas}/{NUM_MAX_TENTATIVAS}): "))
else:
    print("Errou! A lista era:", lista, "boa sorte para a proxima!")


# --- Ex 2 ---
print("\n--- Ex 2 ---")
lista_notas = random.sample(range(1, 21), 15)


print("A nota mais alta:", max(lista_notas))
print("A nota mais baixa:", min(lista_notas))
print("A media das notas:", f"{sum(lista_notas) / len(lista_notas):.1f}")

notas_maiores_10 = 0
for nota in lista_notas:
    if nota > 10:
        notas_maiores_10 += 1
print("O numero de notas maiores que 10:", notas_maiores_10)

lista_notas.sort()
for nota in lista_notas:
    print(nota)


# --- Ex 3 ---
print("\n--- Ex 3 ---")
lista_compras = []

for i in range(5):
    item = input(f"Insira o item {i + 1} da lista de compras: ")
    lista_compras.append(item)

print("\nLista de compras: ", lista_compras)

resposta = input("Queres remover algum item da lista? (sim/nao): ")
try:
    if resposta == "sim":
        item_remover = input("Qual item queres remover? ")
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)
            print(f"{item_remover} foi removido da lista.")
        else:
            print(f"{item_remover} não está na lista.")
    else:
        print("Nenhum item será removido atao chefe.")
except:
    print("Ocorreu um erro ao tentar remover o item.")
finally:
    print("Lista de compras final: ", lista_compras)