# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    try:
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return "Error: División por cero"
    
#menu 

# Menú de la calculadora
while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Ingresa números válidos.")
        continue

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        result = division(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print("Resultado:", result)
    else:
        print("Opción no válida. Por favor, elige una opción válida.")


