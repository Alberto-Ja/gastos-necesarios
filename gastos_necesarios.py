print("Bienbenido al resgistros de gastos diarios")

print("\nMenu")

print("1 Añadir un nuevo gasto")
print("2 Ver todos los gastos")
print("3 Calcular el gasto total y promedio.")
print("4 Borrar todos los gastos")
print("Salir")

gastos = []

while True:

    eleccion = input()

    if eleccion == "1":
       cantidad = float(input())
       gastos .append(cantidad)
       print("¡Gasto añadido con éxito!")

    elif eleccion == "2":
        if len(gastos) == 0:
            print("Sin gastos registrados") 

        else:
            print("Tus gastos:")
            for i in range(len(gastos)):
                print(f"{i + 1}. {gastos[i]}")  

    elif eleccion == "3":
        if len(gastos) == 0:
            print("Aún no se ha registrado ningún gasto.")          

        else:
            total = 0
            for gasto in gastos:
                total += gasto
            promedio = total / len(gastos)
            print(f"Gasto Total: {total}")
            print(f"Gasto Promedio: {promedio}")    

    elif eleccion == "4":
        gastos = []   
        print("Todos los gastos liquidados")         

    elif eleccion == "5": 
        print("Saliendo del registro de gastos diarios. ¡Adiós!")
        break

    else:
        print("Opción no válida. Por favor, inténtelo de nuevo.")