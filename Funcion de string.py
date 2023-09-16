def contar_letras_a(cadena):
    
    contador_a = 0

    for letra in cadena:
        if letra.lower() == 'a':
            contador_a += 1
    
    return contador_a
cadena = "Una vez me tocaba jugar futbol pero no jugue por que me lesione"
cantidad = contar_letras_a(cadena)
print(f"La cantidad de letras 'a' en la cadena es: {cantidad}")
