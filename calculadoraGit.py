def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

while True:
    print("Menu:")

    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    
    operation = input("")

    match operation:
        case "1":
            print("Suma")
            n1 = int(input("Primer numero: "))
            n2 = int(input("Segundo numero: "))
            print(f"La suma de {n1 + n2} = ",suma(n1,n2))

        case "2":
            print("Resta")
            n1 = int(input("Primer numero: "))
            n2 = int(input("Segundo numero: "))
            print(f"La suma de {n1 + n2} = ",resta(n1,n2))

        case "3":
            print("Adios!")
            break

        case _:
            print("No es una opcion")


