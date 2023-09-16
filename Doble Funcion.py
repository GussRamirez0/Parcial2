def calcular_cuadrado():
    num = int(input("Ingrese un número entero: "))
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es: {cuadrado}")

def calcular_producto():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es: {producto}")

if __name__ == "__main__":
    print("1)Calcular el cuadrado de un número.")
    print("2)Calcular el producto de dos números.")
    opcion = int(input("Seleccione una opción (1 o 2): "))

    if opcion == 1:
        calcular_cuadrado()
    elif opcion == 2:
        calcular_producto()
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
