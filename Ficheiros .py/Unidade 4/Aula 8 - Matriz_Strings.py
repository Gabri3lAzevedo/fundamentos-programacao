"""
=========================================================
ISCTE - RESUMO AULA 8: Matrizes e Strings
=========================================================
Matrizes são ideais para dados organizados em 2 dimensões (linhas e colunas). 
Em Python, implementam-se usando Listas de Listas.
Strings são sequências de caracteres que partilham características com as listas
(como a indexação e o fatiamento), mas com uma diferença crucial: são IMUTÁVEIS.
"""

# ==========================================
# 1. MATRIZES (Listas de Listas)
# ==========================================
# Acedemos a uma matriz utilizando a sintaxe matriz[linha][coluna].
print("--- 1. Matrizes ---") 
# --- 1. Matrizes ---

# Exemplo de um tabuleiro do Jogo do Galo (matriz 3x3)
jGalo = [['O', 'X', ' '], 
         ['X', ' ', 'O'], 
         [' ', 'O', 'X']]

print("Imprimir a matriz completa:", jGalo) 
# Imprimir a matriz completa: [['O', 'X', ' '], ['X', ' ', 'O'], [' ', 'O', 'X']]

print("Imprimir toda a linha de índice 1:", jGalo[1]) 
# Imprimir toda a linha de índice 1: ['X', ' ', 'O']

print("Aceder à linha 1, coluna 2:", jGalo[1][2]) 
# Aceder à linha 1, coluna 2: O

# As matrizes são mutáveis (podemos alterar os seus elementos)
jGalo[0] = [' ', ' ', ' '] # Substituir a linha inteira
jGalo[1][1] = 'O'          # Modificar um elemento específico
print("Matriz modificada:", jGalo) 
# Matriz modificada: [[' ', ' ', ' '], ['X', 'O', 'O'], [' ', 'O', 'X']]


# ==========================================
# 2. STRINGS: ACESSO, SLICING E IMUTABILIDADE
# ==========================================
# Partilham lógicas com as listas, mas NÃO podemos alterar um caractere isolado.
print("\n--- 2. Strings: Acesso e Imutabilidade ---") 
# --- 2. Strings: Acesso e Imutabilidade ---

palavra = "Bailarina Capuccina"
print("Comprimento da string:", len(palavra)) # Comprimento da string: 19
print("Caractere no índice 2:", palavra[2]) # Caractere no índice 2: i
print("Slicing [3:]: ", palavra[3:]) # Slicing [3:]: larina Capuccina

# palavra[2] = "T" -> ISTO DARIA ERRO! (TypeError: 'str' object does not support item assignment)

# Concatenação e Repetição
texto = "Crocodilo"
print("Repetição (* 3):", texto * 3) # Repetição (* 3): CrocodiloCrocodiloCrocodilo
print("Concatenação (+):", "Bombardino" + " " + texto) # Concatenação (+): Bombardino Crocodilo


# ==========================================
# 3. CARACTERES ESPECIAIS E MÚLTIPLAS LINHAS
# ==========================================
print("\n--- 3. Caracteres Especiais ---") 
# --- 3. Caracteres Especiais ---

# \n (Nova linha), \t (Tabulação), \" e \' (Aspas dentro de strings)
print("abc\"D\"eF\'gh\n123\t456")
# abc"D"eF'gh
# 123     456

# Aspas triplas permitem criar strings com várias linhas sem precisar do \n
print("""Coisas a fazer esta semana:
- Estudar Python
- Estudar Python (outra vez)""")
# Coisas a fazer esta semana:
# - Estudar Python
# - Estudar Python (outra vez)


# ==========================================
# 4. MÉTODOS DE STRINGS
# ==========================================
# Como as strings são imutáveis, estes métodos DEVOLVEM UMA NOVA STRING!
print("\n--- 4. Métodos de Strings ---") 
# --- 4. Métodos de Strings ---

string_ex = "abc DEF 123"

print("find('c DE'):", string_ex.find("c DE")) # find('c DE'): 2 (devolve o índice inicial)
print("lower():", string_ex.lower())           # lower(): abc def 123
print("upper():", string_ex.upper())           # upper(): ABC DEF 123
print("capitalize():", string_ex.capitalize()) # capitalize(): Abc def 123
print("title():", string_ex.title())           # title(): Abc Def 123

# Métodos de verificação (devolvem True ou False)
print("isnumeric() em '123':", "123".isnumeric()) # isnumeric() em '123': True
print("isalpha() em 'abcDEF':", "abcDEF".isalpha()) # isalpha() em 'abcDEF': True
print("isalpha() em 'abc DEF 123':", string_ex.isalpha()) # isalpha() em 'abc DEF 123': False (contém espaços e números)


# ==========================================
# 💡 DICA DE SUCESSO A RETER
# ==========================================
"""
1. matriz[i][j] lê-se: aceder à linha 'i', e depois à coluna 'j'.
2. Trabalhar com "matrizes" numéricas grandes em Python nativo não é ideal. 
   No futuro, usar-se-á uma biblioteca chamada NumPy.
3. Listas são MUTÁVEIS. Strings são IMUTÁVEIS (qualquer modificação numa string
   obriga a gravar o resultado numa nova variável).
"""