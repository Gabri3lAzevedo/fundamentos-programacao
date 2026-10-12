"""
=========================================================
ISCTE - RESUMO AULA 7: Listas e Operações com Listas
=========================================================
As listas são coleções de dados ordenados e mutáveis em Python.
Esta aula foca-se nos métodos (funções) embutidos nos objetos do tipo lista,
que permitem adicionar, remover, pesquisar, modificar e ordenar itens.
"""

# ==========================================
# 1. ADICIONAR ELEMENTOS (append, extend, insert)
# ==========================================
print("--- 1. Adicionar Elementos ---") # --- 1. Adicionar Elementos ---

# .append(x): Adiciona um item ao fim da lista.
lista = ['a', 'b', 'c']
lista.append('d')
print(f"Após append('d'): {lista}") # Após append('d'): ['a', 'b', 'c', 'd']

# .extend(iterable): Prolonga a lista, adicionando no fim todos os elementos de outra sequência/lista.
lista = ['a', 'b', 'c']
lista.extend([1, 2, 3])
print(f"Após extend([1, 2, 3]): {lista}") # Após extend([1, 2, 3]): ['a', 'b', 'c', 1, 2, 3]

# Diferença prática: append vs extend
lista = ['a', 'b', 'c']
lista.append([1, 2])
print(f"Com append de uma lista: {lista}") # Com append de uma lista: ['a', 'b', 'c', [1, 2]]

# .insert(indice, x): Insere um item numa dada posição.
lista = ['a', 'b', 'c']
lista.insert(0, 3)
print(f"Após insert(0, 3): {lista}") # Após insert(0, 3): [3, 'a', 'b', 'c']


# ==========================================
# 2. REMOVER ELEMENTOS (remove, pop, clear)
# ==========================================
print("\n--- 2. Remover Elementos ---") 
# --- 2. Remover Elementos ---

# .remove(x): Remove o primeiro item encontrado cujo valor é x.
lista = ['a', 'b', 'c']
lista.remove('b')
print(f"Após remove('b'): {lista}") # Após remove('b'): ['a', 'c']

# .pop([indice]): Remove e devolve o item. Sem índice, remove o último.
lista = ['a', 'b', 'c']
removido = lista.pop()
print(f"Após pop(): {lista} | Removido: {removido}") # Após pop(): ['a', 'b'] | Removido: c

# .clear(): Remove todos os itens da lista.
lista.clear()
print(f"Após clear(): {lista}") # Após clear(): []


# ==========================================
# 3. PESQUISAR E CONTAR (index, count)
# ==========================================
print("\n--- 3. Pesquisar e Contar ---") 
# --- 3. Pesquisar e Contar ---

# index(x): Devolve o índice do primeiro item com o valor x.
lista = ['a', 'b', 'c', 'b']
indice = lista.index('b')
print(f"Índice do primeiro 'b': {indice}") # Índice do primeiro 'b': 1

# count(x): Devolve o número de vezes que x aparece na lista.
contagem = lista.count('b')
print(f"Vezes que 'b' aparece na lista: {contagem}") # Vezes que 'b' aparece na lista: 2


# ==========================================
# 4. ORDENAR E INVERTER (sort, reverse)
# ==========================================
print("\n--- 4. Ordenar e Inverter ---") 
# --- 4. Ordenar e Inverter ---

# sort(): Ordena os itens da lista (ordem crescente/alfabética).
lista = [3, 2, 1, 5, 4]
lista.sort()
print(f"Após sort(): {lista}") # Após sort(): [1, 2, 3, 4, 5]

# reverse(): Inverte a ordem atual dos elementos na lista.
lista = [3, 2, 1, 5, 4]
lista.reverse()
print(f"Após reverse(): {lista}") # Após reverse(): [4, 5, 1, 2, 3]


# ==========================================
# 💡 DICA DE SUCESSO A RETER
# ==========================================
"""
As listas são estruturas MUTÁVEIS. 
Métodos para decorares:
- Adicionar: append() (1 elemento), extend() (múltiplos elementos), insert() (numa posição específica).
- Remover: remove() (pelo valor), pop() (pelo índice, e guarda o valor), clear() (apaga tudo).
- Organizar: sort() (ordena), reverse() (inverte de trás para a frente).
"""