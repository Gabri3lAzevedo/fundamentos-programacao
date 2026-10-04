"""
=========================================================
ISCTE - RESUMO AULA 5: Controlo de Erros (try except)
=========================================================
Em Python, os erros que ocorrem durante a execução chamam-se EXCEÇÕES.
Sem tratamento, uma exceção faz o programa "crashar" (parar).
O tratamento de exceções impede a paragem e avisa o utilizador.
Novas palavras-chave: try, except, else, finally.
"""

# ==========================================
# 1. SINTAXE BÁSICA (try / except genérico)
# ==========================================
# Se não usarmos 'try', escrever "abc" num input de 'int' quebra o programa.
print("--- 1. Sintaxe Básica ---")

try:
    # Colocamos no 'try' o código que desconfiamos que pode dar erro
    numero = int(input("Introduza um número: "))
    print("O dobro é:", numero * 2)
except:
    # O 'except' diz o que fazer se OCORRER UM ERRO no bloco de cima
    print("Erro: Deve introduzir um valor numérico!!")


# ==========================================
# 2. TRATAMENTO ESPECÍFICO DE ERROS
# ==========================================
# É boa prática apanhar os erros pelo seu nome específico.
# Os mais comuns: ValueError (tipo errado) e ZeroDivisionError (divisão por zero)
print("\n--- 2. Tratamento Específico ---")

try:
    numero = int(input("Introduza um número para dividir 10: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
    
except ValueError:
    print("Erro: Deve introduzir um valor numérico!!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")


# ==========================================
# 3. OS BLOCOS ELSE E FINALLY
# ==========================================
# Podemos expandir a estrutura para termos ainda mais controlo.
print("\n--- 3. Else e Finally ---")

try:
    numero = int(input("Introduza um número inteiro: "))
except ValueError:
    # Corre APENAS se houver erro (se escreveres texto)
    print("Erro: Valor inválido!!")
else:
    # Corre APENAS se NÃO houver nenhum erro
    print(f"Valor introduzido com sucesso: {numero}")
finally:
    # Corre SEMPRE, independentemente de dar erro ou não.
    # (É muito usado por programadores para fechar ficheiros ou bases de dados abertas)
    print("Fim da execução deste bloco.")


# ==========================================
# 4. ATIVIDADE PRÁTICA 2 (Ciclo com Validação)
# ==========================================
# Juntando o que aprendemos na Aula 4 (while) com a Aula 5 (try/except)
print("\n--- 4. Atividade Prática 2 (Validação de Inputs) ---")

while True:
    entrada1 = input("\nIntroduza o primeiro número (ou 'Sair'): ")
    if entrada1.lower() == "sair":
        print("A encerrar o programa...")
        break
        
    entrada2 = input("Introduza o segundo número (ou 'Sair'): ")
    if entrada2.lower() == "sair":
        print("A encerrar o programa...")
        break
        
    try:
        # Tenta converter os textos para números e dividir
        num1 = float(entrada1)
        num2 = float(entrada2)
        resultado = num1 / num2
        
    except ValueError:
        print("Erro: Deve introduzir valores numéricos válidos. Tente novamente!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Tente novamente!")
    else:
        # Só mostra o resultado se as duas conversões e a divisão correrem bem
        print(f"O resultado da divisão é: {resultado}")
    finally:
        print("-> Fim desta tentativa.")


# ==========================================
# 💡 DICA DE SUCESSO A RETER
# ==========================================
"""
O 'Exception' é o "pai" de quase todos os erros comuns em Python.
Deves tratar os erros sempre que o teu programa dependa de fatores externos:
1. Quando o utilizador tem de introduzir dados (inputs).
2. Quando abres ficheiros do computador.
3. Quando fazes operações de rede / internet.
"""