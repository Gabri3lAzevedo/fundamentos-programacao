"""
=========================================================
ISCTE - RESUMO AULA 8: Outras Estruturas de Dados
=========================================================
Para além das listas e strings, o Python possui estruturas avançadas para
diferentes necessidades:
- Tuples: Sequências ordenadas e IMUTÁVEIS.
- Conjuntos (Sets): Coleções não ordenadas SEM elementos repetidos.
- Dicionários: Estruturas associativas baseadas em pares CHAVE: VALOR.
"""

# ==========================================
# 1. TUPLES (Tuplos)
# ==========================================
# São como listas, mas não podem ser alterados depois de criados (Imutáveis).
print("--- 1. Tuples ---") 
# --- 1. Tuples ---

# Criação (parênteses são opcionais, mas recomendados)
t1 = 1, 2, 3, "abc"
t2 = (True, 12.5, 10)
t3 = (12.5,) # ATENÇÃO: Um tuple de 1 elemento OBRIGA ao uso de vírgula!

print("Aceder por índice t1[3]:", t1[3]) # Aceder por índice t1[3]: abc

# t1[2] = 4 -> ISTO DARIA ERRO! (Tuples não suportam atribuição)

# Desempacotamento (Unpacking)
x, y, z = t2
print(f"Desempacotamento de t2: x={x}, y={y}, z={z}") 
# Desempacotamento de t2: x=True, y=12.5, z=10


# ==========================================
# 2. CONJUNTOS (Sets)
# ==========================================
# Não ordenados, não indexáveis, mutáveis, e ignoram elementos repetidos.
print("\n--- 2. Conjuntos (Sets) ---") 
# --- 2. Conjuntos (Sets) ---

frutas = {'Maçã', 'Laranja', 'Banana', 'Maçã'}
cores = {'Azul', 'Vermelho', 'Laranja', 'Azul'}

print("Conjunto de frutas (ignora a 2ª Maçã):", frutas) 
# Conjunto de frutas: {'Laranja', 'Banana', 'Maçã'} (a ordem pode variar)

# Operações Matemáticas
print("União (frutas | cores):", frutas | cores) # Junta tudo sem repetir
print("Intersecção (frutas & cores):", frutas & cores) # Apenas o que está em ambos: {'Laranja'}
print("Diferença (frutas - cores):", frutas - cores) # Apenas nas frutas: {'Maçã', 'Banana'}

# Inserção e Remoção
frutas.add('Uva')
frutas.discard('Banana') # discard() não dá erro se o elemento não existir, ao contrário do remove()
print("Conjunto após add e discard:", frutas) 
# Conjunto após add e discard: {'Laranja', 'Maçã', 'Uva'}


# ==========================================
# 3. DICIONÁRIOS
# ==========================================
# Mutáveis, dinâmicos e acedidos através de uma Chave Única (não por índice numérico).
print("\n--- 3. Dicionários ---") 
# --- 3. Dicionários ---

dias_do_mes = {'Janeiro': 31, 'Fevereiro': 28, 'Março': 31}

# Acesso e Modificação
print("Dias de Janeiro:", dias_do_mes['Janeiro']) # Dias de Janeiro: 31
# print(dias_do_mes['Abril']) -> ISTO DARIA ERRO! (Chave não existe)
print("Uso do get() seguro:", dias_do_mes.get('Abril')) # Uso do get() seguro: None

dias_do_mes['Fevereiro'] = 29 # Modifica um valor existente
dias_do_mes['Abril'] = 30     # Adiciona um novo par chave:valor
del dias_do_mes['Março']      # Apaga um par do dicionário

print("Dicionário atualizado:", dias_do_mes) 
# Dicionário atualizado: {'Janeiro': 31, 'Fevereiro': 29, 'Abril': 30}

# Iteração com ciclos For
print("\nIterar Dicionários:")
for nome, num in dias_do_mes.items(): # O .items() devolve a chave e o valor em simultâneo
    print(f"{nome} tem {num} dias")
# Janeiro tem 31 dias
# Fevereiro tem 29 dias
# Abril tem 30 dias


# ==========================================
# 4. PERTENÇA, COMPRIMENTO E CÓPIAS (Aliasing)
# ==========================================
print("\n--- 4. Operações Comuns e Cópias ---") 
# --- 4. Operações Comuns e Cópias ---

# Pertença (in / not in)
myList = ["a", "b", "c"]
print("O elemento 'a' está na lista?", "a" in myList) # True

# ATENÇÃO AOS ALIASES (Cópias de estruturas mutáveis)
lista_original = ["a", "b", "c"]
lista_copia = lista_original # ISTO NÃO CRIA UM FICHEIRO NOVO, É APENAS UM ATALHO!

lista_original.append("d")
print("Lista cópia também foi alterada:", lista_copia) 
# Lista cópia também foi alterada: ['a', 'b', 'c', 'd']


# ==========================================
# 💡 DICA DE SUCESSO A RETER
# ==========================================
"""
1. Usa [Listas] quando precisares de ordem e alterações.
2. Usa (Tuples) quando tens um conjunto de dados que NUNCA deve mudar no código.
3. Usa {Sets} quando a ordem não importa mas não podes ter duplicados.
4. Usa {Dicionários: Valores} quando precisas de mapear identificadores (chaves) para dados.
5. CUIDADO com o sinal '=' ao copiar Listas, Sets ou Dicionários. Se alterares um, alteras o outro!
"""