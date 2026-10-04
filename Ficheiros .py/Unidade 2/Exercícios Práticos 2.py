# --- 1 ---
print("\n--- 1 ---")
PI = 3.14159
VELOCIDADE_DA_LUZ = 299792458 # em metros por segundo

print(f"- Valor de PI: {PI}")
print(f"- Velocidade da luz: {VELOCIDADE_DA_LUZ} m/s")

# --- 2 ---
print("\n--- 2 ---")
x = 10
nome = "Ana"
altura = 1.65
ativo = True

print(f"- x: {x}")
print(f"- nome: {nome}")
print(f"- altura: {altura}")
print(f"- ativo: {ativo}")

# --- 3 ---
print("\n--- 3 ---")
print(f"PI = {PI} tem o tipo {type(PI)}")
print(f"VELOCIDADE DA LUZ = {VELOCIDADE_DA_LUZ} tem o tipo {type(VELOCIDADE_DA_LUZ)}")
print(f"x = {x} tem o tipo {type(x)}")
print(f"nome = {nome} tem o tipo {type(nome)}")
print(f"altura = {altura} tem o tipo {type(altura)}")
print(f"ativo = {ativo} tem o tipo {type(ativo)}")

# --- 4 ---
print("\n--- 4 ---")
a = "123"
b = int(a) # Conversão explícita de string para inteiro

print(f"A variavel a tem o valor {a} e é do tipo {type(a)}")
print(f"A variavel b tem o valor {b} e é do tipo {type(b)}")

# --- 5 ---
print("\n--- 5 ---")
a = 4
b = 8

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

# --- 6 ---
print("\n--- 6 ---")
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b

print(f"soma = {soma} tem o tipo {type(soma)}")
print(f"subtração = {subtracao} tem o tipo {type(subtracao)}")
print(f"multiplicação = {multiplicacao} tem o tipo {type(multiplicacao)}")
print(f"divisão = {divisao} tem o tipo {type(divisao)}")
print(f"divisão inteira = {divisao_inteira} tem o tipo {type(divisao_inteira)}")
print(f"módulo = {modulo} tem o tipo {type(modulo)}")
print(f"exponenciação = {exponenciacao} tem o tipo {type(exponenciacao)}")

# --- 7 ---
print("\n--- 7 ---")
print(f"a == b {a == b} tem o tipo {type(a == b)}")
print(f"a != b {a != b} tem o tipo {type(a != b)}")
print(f"a > b {a > b} tem o tipo {type(a > b)}")
print(f"a < b {a < b} tem o tipo {type(a < b)}")
print(f"a >= b {a >= b} tem o tipo {type(a >= b)}")
print(f"a <= b {a <= b} tem o tipo {type(a <= b)}")

# --- 8 ---
print("\n--- 8 ---")
a = True
b = False

print(a and b) # Só é True se ambos forem True
print(a or b)  # É True se pelo menos um for True
print(not a)   # Inverte a
print(not b)   # Inverte b