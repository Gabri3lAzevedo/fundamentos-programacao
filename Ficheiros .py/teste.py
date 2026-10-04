idades = [8, 12, 17, 18, 64, 65]

for idade in idades:
    # Finge o input do utilizador no terminal
    print(f"Qual é a sua idade? {idade}")
    
    # Lógica do programa
    if idade < 12:
        print("Entrada gratuita")
    elif idade <= 17:
        print("Bilhete jovem")
    elif idade <= 64:
        print("Bilhete normal")
    else:
        print("Bilhete sénior")
    
    # Dá um espaço em branco para separar cada "teste" e parecer mais real
    print()