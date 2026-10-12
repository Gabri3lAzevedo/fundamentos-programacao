import random
# --- Ex 1 ---
print("\n--- Ex 1 ---")
lista_frutas = ["maçã", "banana", "laranja", "maçã"]

quantidade_de_frutas = 0
for fruta in lista_frutas:
    quantidade_de_frutas += 1
print("A quantidade de frutas na lista é:", quantidade_de_frutas)

print("A quantidade de frutas na lista é:", len(lista_frutas))

# --- Ex 2 ---
print("\n--- Ex 2 ---")
lista_numeros = [1, 2, 3, 4, 5]
lista_numeros.append(6)
print("A lista de números é:", lista_numeros)

# --- Ex 3 ---
print("\n--- Ex 3 ---")
lista_animais = ["gato", "cao", "pássaro"]
lista_animais.extend(["peixe", "tartaruga"])
print("A lista de animais é:", lista_animais)

# --- Ex 4 ---
print("\n--- Ex 4 ---")
lista_cidades = ["Lisboa", "Porto", "Coimbra", "Faro"]
lista_cidades.insert(2, "Braga")
print("A lista de cidades é:", lista_cidades)

# --- Ex 5 ---
print("\n--- Ex 5 ---")
lista_números = [10, 20, 30, 40, 50]
lista_números.remove(30)
print("A lista de números é:", lista_números)

# --- Ex 6 ---
print("\n--- Ex 6 ---")
lista_cores = ["vermelho", "azul", "verde", "amarelo"]
lista_cores.pop()
print("A lista de cores é:", lista_cores)

# --- Ex 7 ---
print("\n--- Ex 7 ---")
lista_alfabeto = ["a", "d", "c", "b", "e"]
lista_alfabeto.sort()
lista_alfabeto.reverse()
print("A lista do alfabeto é:", lista_alfabeto)

# --- Ex 8 ---
print("\n--- Ex 8 ---")
lista_notas = [8, 6, 9, 7, 8, 10, 8]
lista_notas.count(8)
print("A quantidade de notas 8 na lista é:", lista_notas.count(8))
while 8 in lista_notas:
    lista_notas.remove(8)
print("A lista de notas é:", lista_notas)

# --- Ex 9 ---
print("\n--- Ex 9 ---")
lista_itens = [1, 2, 3, 4, 5, 6]
lista_itens.clear()
lista_itens.append(10)
lista_itens.append(20)
lista_itens.append(30)
lista_itens.extend([10, 20, 30])
index_20 = lista_itens.index(20)
print("A lista de itens é:", lista_itens)
print("O índice do elemento 20 é:", index_20)