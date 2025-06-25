numeros = []

def insertar():
    try:
        numero = int(input("Ingrese un número entero a insertar: "))
        numeros.append(numero)
        print(f"Número {numero} insertado correctamente.")
        print("Lista actualizada: ", numeros)  # Mostrar la lista actualizada
    except ValueError:
        print("Por favor, ingrese un valor numerico válido.")

def modificar():
    if len(numeros) == 0:
        print("La lista está vacía, no puedes modificar nada.")
        return

    print("Lista actual:", numeros)
    try:
        index = int(input("Ingrese el índice del número a modificar: "))
        if index < 0 or index >= len(numeros):
            print("Índice fuera de rango.")
            return
        nuevo_numero = int(input("Ingrese el nuevo valor para el número: "))
        numeros[index] = nuevo_numero
        print(f"Número en el índice {index} modificado a {nuevo_numero}.")
        print("Lista actualizada:", numeros)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

def eliminar():
    if len(numeros) == 0:
        print("La lista está vacía, no puedes eliminar nada.")
        return

    try:
        print("Lista actual:", numeros)
        numero = int(input("Ingrese el número a eliminar: "))
        if numero in numeros:
            numeros.remove(numero)
            print(f"Número {numero} eliminado correctamente.")
            print("Lista actualizada:", numeros)  # Mostrar la lista actualizada
        else:
            print(f"El número {numero} no está en la lista.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

def buscar():
    if len(numeros) == 0:
        print("La lista esta vacía.")
        return

    try:
        numero = int(input("Ingrese el número a buscar: "))
        if numero in numeros:
            print(f"El número {numero} se encuentra en la lista.")
        else:
            print(f"El número {numero} no se encuentra en la lista.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

def menor():
    if len(numeros) == 0:
        print("La lista está vacía.")
        return
    print(f"El menor número en la lista es: {min(numeros)}")

def mayor():
    if len(numeros) == 0:
        print("La lista está vacía.")
        return
    print(f"El mayor número en la lista es: {max(numeros)}")

def main():
    while True:
        print("\nMenu:")
        print("[1]. Insertar")
        print("[2]. Modificar")
        print("[3]. Eliminar")
        print("[4]. Buscar elemento")
        print("[5]. Menor")
        print("[6]. Mayor")
        print("[7]. Salir")

        opciones = {
            1: insertar,
            2: modificar,
            3: eliminar,
            4: buscar,
            5: menor,
            6: mayor,
            7: exit
        }

        try:
            opcion = int(input("Seleccione una opción: "))
            accion = opciones.get(opcion)
            if accion:
                accion()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la opción.")

if __name__ == "__main__":
    main()
