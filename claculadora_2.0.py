import time
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Restar")
    print("2. Sumar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numeros():
    try:
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        return numero1, numero2
    except ValueError:
        print("Error: se deben ingresar una opcion valida.")
        time.sleep(3)
        return None, None

def sumar():
    numero1, numero2 = pedir_numeros()
    if numero1 is not None:
        print(f"La suma es {numero1 + numero2}")

def restar():
    numero1, numero2 = pedir_numeros()
    if numero1 is not None:
        print(f"La resta es {numero1 - numero2}")

def multiplicar():
    numero1, numero2 = pedir_numeros()
    if numero1 is not None:
        print(f"La multiplicación es {numero1 * numero2}")

def dividir():
    numero1, numero2 = pedir_numeros()
    if numero1 is not None:
        try:
            resultado = numero1 / numero2
            print(f"La división es {resultado}")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
            time.sleep(3)

def main():
    while True:
        mostrar_menu()
        try:
            op = int(input("Seleccione una opción: "))
            if op == 1:
                restar()
            elif op == 2:
                sumar()
            elif op == 3:
                multiplicar()
            elif op == 4:
                dividir()
            elif op == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")
            time.sleep(3)


main()
