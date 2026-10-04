# --- 1 ---
"""
Estruturas de Repetição (Ciclos): Permitem executar um bloco de código 
                                  várias vezes consoante uma condição.
Tipos:  
    - while: Repete enquanto uma condição lógica for verdadeira (True).
    - for: Repete um número predefinido de vezes, percorrendo uma sequência (ex: range).
Keywords importantes: 
    - continue: Salta a volta atual e passa imediatamente para a próxima.
    - break: Interrompe e sai imediatamente do ciclo.
"""

# --- 2 ---
print("\n--- 2 ---")
soma = 0
i = 1
while i <= 100:
    soma = soma + i
    i = i + 1
print(f"- A soma dos números de 1 a 100 é: {soma}")

# --- 3 ---
print("\n--- 3 ---")
