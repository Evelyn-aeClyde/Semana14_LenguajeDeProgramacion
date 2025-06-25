import sys

def insertar_datos():
    nombre = input("Introduce el nombre de la persona: ")
    habilidades = input("Introduce las habilidades: ").split(",")
    intereses = input("Introduce los intereses: ").split(",")
    documentos = input("Introduce los documentos: ").split(",")
    
    persona = {
        'nombre': nombre,
        'habilidades': habilidades,
        'intereses': intereses,
        'documentos': documentos
    }
    
    return persona

def modificar_datos(persona):
    print("\n¿Qué deseas modificar?")
    print("1. Habilidades")
    print("2. Intereses")
    print("3. Documentos")
    eleccion = input("Elige una opción (1/2/3): ")
    
    if eleccion == '1':
        habilidades = input("Introduce las nuevas habilidades: ").split(",")
        persona['habilidades'] = habilidades
    elif eleccion == '2':
        intereses = input("Introduce los nuevos intereses: ").split(",")
        persona['intereses'] = intereses
    elif eleccion == '3':
        documentos = input("Introduce los nuevos documentos: ").split(",")
        persona['documentos'] = documentos
    else:
        print("Opción no válida.")
    
    return persona

def eliminar_datos(persona):
    confirmacion = input(f"¿Estás seguro de que quieres eliminar los datos de {persona['nombre']}? (s/n): ").lower()
    if confirmacion == 's':
        return None
    else:
        print("Eliminación cancelada.")
        return persona

def mostrar_datos(persona):
    if persona is None:
        print("\nNo hay datos para mostrar.")
    else:
        print("\nDatos actuales de la persona:")
        print(f"Nombre: {persona['nombre']}")
        print(f"Habilidades: {', '.join(persona['habilidades'])}")
        print(f"Intereses: {', '.join(persona['intereses'])}")
        print(f"Documentos: {', '.join(persona['documentos'])}")

def mostrar_menu():
    persona = None
    while True:
        print("\nMenú de opciones:")
        print("[1]. Insertar")
        print("[2]. Modificar")
        print("[3]. Eliminar")
        print("[4]. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            persona = insertar_datos()
            print(f"\nDatos de {persona['nombre']} ingresados correctamente.")
            mostrar_datos(persona)
        elif opcion == '2':
            if persona is None:
                print("\nNo hay datos disponibles para modificar.")
            else:
                persona = modificar_datos(persona)
                print("\nDatos modificados correctamente.")
                mostrar_datos(persona) 
        elif opcion == '3':
            if persona is None:
                print("\nNo hay datos disponibles para eliminar.")
            else:
                persona = eliminar_datos(persona)
                if persona is None:
                    print("\nDatos eliminados.")
                else:
                    print("\nDatos no eliminados.")
                mostrar_datos(persona)
        elif opcion == '4':
            sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()
