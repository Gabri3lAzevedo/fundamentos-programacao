"""
=========================================================
ISCTE - RESUMO AULA 4: Estruturas de Repetição (while)
=========================================================
A estrutura de repetição 'while' (enquanto) repete um conjunto 
de instruções enquanto uma determinada condição for verdadeira.
Novas palavras-chave: while, break, continue, else.
"""

# ==========================================
# 1. CICLO BÁSICO (INCREMENTO E DECREMENTO)
# ==========================================
# O ciclo repete o código enquanto a condição for True.
print("--- 1. Ciclo Básico ---")

print("A contar para cima (Incremento):")
i = 0
while i <= 10:
    print(i, end=", ")
    i = i + 1  # MUITO IMPORTANTE: atualizar a variável para o ciclo não ser infinito!
print("Fim!")

print("\nA contar para baixo (Decremento):")
i = 10
while i >= 0:
    print(i, end=", ")
    i = i - 1  # Retira 1 a cada volta
print("Fim!")


# ==========================================
# 2. SINTAXE COMPACTA
# ==========================================
# Quando há poucas instruções no ciclo, podemos escrevê-las na mesma 
# linha usando o ponto e vírgula (;) para separar os comandos.
print("\n--- 2. Sintaxe Compacta ---")
i = 0
while i < 42: print(i, end=", "); i = i + 10
print("Fim do programa!")


# ==========================================
# 3. A INSTRUÇÃO BREAK
# ==========================================
# A instrução 'break' termina o ciclo abruptamente (estilhaça o ciclo), 
# sem sequer voltar a avaliar a condição inicial.
print("\n--- 3. Instrução Break ---")
i = 0
while i < 42:
    if i > 25:
        break # Para o ciclo imediatamente (no 30, ignora o resto)
    print(i, end=", ")
    i = i + 10
print("Fim do programa!")


# ==========================================
# 4. A INSTRUÇÃO CONTINUE
# ==========================================
# O 'continue' "ultrapassa" o resto das instruções daquela volta específica 
# e regressa imediatamente ao topo do ciclo para avaliar a condição de novo.
print("\n--- 4. Instrução Continue ---")
i = 0
while i < 42:
    i = i + 10
    if i == 20:
        continue # Quando i é 20, salta o print e avança logo para a próxima volta (30)
    print(i, end=", ")
print("Fim do programa!")

# 🔴 ATENÇÃO (Slide 11): 
# Se o incremento (i = i + 10) estivesse DEPOIS do 'continue' no código acima, 
# o programa ficaria preso num CICLO INFINITO quando chegasse ao 20, 
# porque saltava o incremento e o 'i' nunca mais saía do 20!


# ==========================================
# 5. O BLOCO ELSE (COM E SEM BREAK)
# ==========================================
# O bloco 'else' permite executar instruções alternativas QUANDO A CONDIÇÃO 
# DO CICLO DEIXA DE SE VERIFICAR (termina de forma "natural").
print("\n--- 5. Bloco Else ---")

print("Exemplo SEM break (o else corre):")
i = 0
while i < 42:
    print(i, end=", ")
    i = i + 10
else:
    print("42!!") # Corre porque a condição (i < 42) passou a ser Falsa naturalmente

print("\nExemplo COM break (o else NÃO corre):")
i = 0
while i < 42:
    if i > 25:
        break
    print(i, end=", ")
    i = i + 10
else:
    print("42!!") # NUNCA vai ser executado porque o 'break' estragou o fim natural do ciclo.

print("Fim do programa!")