"""
=========================================================
ISCTE - RESUMO AULA 2: Constantes, Variáveis e Tipos
=========================================================
"""

# ==========================================
# 1. CONSTANTES E VARIÁVEIS
# ==========================================
TAXA_IVA = 23      # Constante: Convenção usar MAIÚSCULAS. Valor fixo e não deve mudar.
idade_aluno = 18   # Variável: Minúsculas e descritivas. O valor pode mudar ao longo do código.
# Regra de ouro: Nomes não podem começar por números nem ter caracteres como '@'.


# ==========================================
# 2. TIPOS DE DADOS PRIMITIVOS E type()
# ==========================================
v_int = 42              # int: Número inteiro
v_float = 3.14          # float: Número decimal (usar sempre ponto)
v_complex = 1 + 2j      # complex: Número complexo (parte real + imaginária)
v_bool = True           # bool: Booleano (True ou False - 1ª letra maiúscula)
v_str = "Olá, Python"   # str: Texto (String)

# A função type() serve para descobrir o tipo da variável:
print("Tipo da variável v_complex:", type(v_complex))


# ==========================================
# 3. TIPOS DE DADOS ESTRUTURADOS (COLEÇÕES)
# ==========================================
v_list = [1, 2, 3]                  # list: Lista ordenada e mutável (podes alterar)
v_tuple = (1, 2, 3)                 # tuple: Tuplo ordenado e imutável (não podes alterar)
v_dict = {'nome': 'Alice', 'idade': 30} # dict: Dicionário (pares de chave-valor)
v_set = {1, 2, 3}                   # set: Conjunto desordenado de itens únicos (sem     repetidos)
v_frozenset = frozenset([1, 2, 3])  # frozenset: Conjunto imutável


# ==========================================
# 4. CONVERSÃO DE TIPOS (CASTING)
# ==========================================
c_int = int(3.5)        # Converte para inteiro: Fica 3 (corta a parte decimal)
c_float = float("4.2")  # Converte para decimal: Fica 4.2 (de texto para número)
c_str = str(10)         # Converte para texto: Fica "10"
c_bool = bool(0)        # Converte para booleano: Fica False (0 é False, 1 é True)


# ==========================================
# 5. OPERAÇÕES MATEMÁTICAS
# ==========================================
a = 10
b = 3

print("\n--- Operações Matemáticas ---")
print(f"Adição (+): {a + b}")           # Resultado: 13
print(f"Subtração (-): {a - b}")        # Resultado: 7
print(f"Multiplicação (*): {a * b}")    # Resultado: 30
print(f"Divisão (/): {a / b}")          # Resultado: 3.333... (Devolve sempre um float)
print(f"Divisão Inteira (//): {a // b}") # Resultado: 3 (Devolve o quociente, corta os decimais)
print(f"Módulo/Resto (%): {a % b}")           # Resultado: 1 (Devolve o resto da divisão)
print(f"Exponenciação (**): {a ** b}")  # Resultado: 1000 (10 elevado a 3)


# ==========================================
# 6. OPERADORES RELACIONAIS
# ==========================================
# Servem para comparar valores. Devolvem SEMPRE True ou False.
print("\n--- Operadores Relacionais ---")
print(f"Igual a (==): 5 == 5 -> {5 == 5}")       
print(f"Diferente de (!=): 5 != 3 -> {5 != 3}")  
print(f"Maior que (>): 7 > 5 -> {7 > 5}")       
print(f"Menor que (<): 3 < 6 -> {3 < 6}")       
print(f"Maior ou igual (>=): 8 >= 8 -> {8 >= 8}") 
print(f"Menor ou igual (<=): 4 <= 6 -> {4 <= 6}") 


# ==========================================
# 7. OPERADORES LÓGICOS
# ==========================================
# Combinam múltiplas condições.
print("\n--- Operadores Lógicos ---")
# AND (E): Devolve True SÓ SE ambas as condições forem verdadeiras
print(f"AND: (5 > 3) and (8 > 6) -> {(5 > 3) and (8 > 6)}")

# OR (Ou): Devolve True SE PELO MENOS UMA das condições for verdadeira
print(f"OR: (5 > 3) or (8 < 6) -> {(5 > 3) or (8 < 6)}")

# NOT (Negação): Inverte o resultado (se é True, vira False)
print(f"NOT: not(5 > 3) -> {not(5 > 3)}")