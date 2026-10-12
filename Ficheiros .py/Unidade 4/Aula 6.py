"""
=========================================================
ISCTE - RESUMO AULA 6: Listas e Operações com Listas
=========================================================
As listas são coleções de dados ordenados e mutáveis em Python.
Permitem guardar uma sequência de objetos separados por vírgulas entre parêntesis retos [].
Novos conceitos: Índices, Mutabilidade, Slicing, Aninhamento e o módulo random.
"""

# ==========================================
# 1. DEFINIÇÃO E CARACTERÍSTICAS PRINCIPAIS
# ==========================================
# 1. Ordenadas (a ordem importa)
# 2. Arbitrárias (aceitam qualquer tipo de dados)
# 3. Mutáveis (podem ser alteradas após a criação)
print("--- 1. Definição e Características ---") # --- 1. Definição e Características ---

lista_a = ["Bué", "Ya", "Cota"]
lista_b = ["Cota", "Bué", "Ya"]
print(f"As listas são iguais? {lista_a == lista_b}") # As listas são iguais? False, porque a ordem importa

lista_mista = ["iscte", 1, 9.5, True]
print(f"Lista com múltiplos tipos: {lista_mista}") # Lista com múltiplos tipos: ['iscte', 1, 9.5, True]


# ==========================================
# 2. ACESSO POR ÍNDICE E ANINHAMENTO
# ==========================================
# O primeiro elemento está no índice 0. Índices negativos começam de trás para a frente (-1).
print("\n--- 2. Índices e Aninhamento ---") 
# --- 2. Índices e Aninhamento ---

elementos = ["bazar", "cota", "ya", "chill", "moca", "fixe"]
print("Primeiro elemento (índice 0):", elementos[0]) # Primeiro elemento (índice 0): bazar
print("Último elemento (índice -1):", elementos[-1]) # Último elemento (índice -1): fixe

# Listas aninhadas (listas dentro de listas) em profundidades arbitrárias
lista_aninhada = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g"]
print("Aceder à sublista:", lista_aninhada[1]) # Aceder à sublista: ['bb', ['ccc', 'ddd'], 'ee', 'ff']
print("Aceder a uma sub-sublista:", lista_aninhada[1][1][0]) # Aceder a uma sub-sublista: ccc


# ==========================================
# 3. FATIAMENTO (SLICING) E TAMANHO (LEN)
# ==========================================
# Sintaxe de slicing: lista[inicio : fim] -> o índice "fim" é EXCLUÍDO!
print("\n--- 3. Slicing e Tamanho (len) ---") 
# --- 3. Slicing e Tamanho (len) ---

numeros = [1, 2, 3, 4, 5]
print(f"Tamanho da lista com len(): {len(numeros)} elementos") # Tamanho da lista com len(): 5 elementos
print("Slicing do índice 0 ao 3 (excluído):", numeros[0:3]) # Slicing do índice 0 ao 3 (excluído): [1, 2, 3]
print("Slicing omitindo tudo (cópia completa):", numeros[:]) # Slicing omitindo tudo (cópia completa): [1, 2, 3, 4, 5]
print("Slicing do índice 2 até ao fim:", numeros[2:]) # Slicing do índice 2 até ao fim: [3, 4, 5]


# ==========================================
# 4. MÓDULO RANDOM
# ==========================================
# Módulo que gera números/escolhas pseudoaleatórias (simulações, baralhar listas).
print("\n--- 4. Módulo random ---") 
# --- 4. Módulo random ---

import random

# Números Inteiros aleatórios
num_aleatorio = random.randint(1, 10)
print(f"Número inteiro aleatório (randint): {num_aleatorio}") # Número inteiro aleatório (randint): 7 (Exemplo)

# Números Decimais aleatórios
decimal_aleatorio = random.uniform(1.0, 5.0)
print(f"Número decimal aleatório (uniform): {decimal_aleatorio:.2f}") # Número decimal aleatório (uniform): 3.14 (Exemplo)

# Escolher um elemento aleatório de uma lista
opcoes = ["Pedra", "Papel", "Tesoura"]
escolha = random.choice(opcoes)
print(f"Elemento escolhido (choice): {escolha}") # Elemento escolhido (choice): Pedra (Exemplo)

# Baralhar os elementos de uma lista diretamente
cartas = ["Ás", "Rei", "Dama", "Valete"]
random.shuffle(cartas)
print(f"Lista baralhada (shuffle): {cartas}") # Lista baralhada (shuffle): ['Dama', 'Ás', 'Valete', 'Rei'] (Exemplo)


# ==========================================
# 💡 DICA DE SUCESSO A RETER
# ==========================================
"""
1. A indexação começa SEMPRE em 0.
2. No Slicing [inicio:fim], o elemento final NUNCA é incluído.
3. As listas são coleções MUTÁVEIS (ao contrário das strings), o que significa
   que é possível percorrer, modificar, adicionar e remover itens diretamente nelas.
"""