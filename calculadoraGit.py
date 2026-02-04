def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a/b


while True:
    print("\nMenu:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    operation = input("Elige una opción: ")

    match operation:
        case "1":
            n1 = int(input("Primer número: "))
            n2 = int(input("Segundo número: "))
            print("Resultado:", suma(n1, n2))

        case "2":
            n1 = int(input("Primer número: "))
            n2 = int(input("Segundo número: "))
            print("Resultado:", resta(n1, n2))

        case "3":
            n1 = int(input("Primer número: "))
            n2 = int(input("Segundo número: "))
            print("Resultado:", multiplicar(n1, n2))

        case "4":
            n1 = int(input("Primer número: "))
            n2 = int(input("Segundo número: "))
            print("Resultado:", dividir(n1, n2))

        case "5":
            print("¡Adiós!")
            break

        case _:
            print("No es una opción válida")
