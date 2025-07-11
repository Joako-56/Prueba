catalogo = {
  'S23ULTRA': ['Samsung', '6.8"', '12GB', '512GB', 'Snapdragon 8 Gen 2'],
  'IP14PRO': ['Apple', '6.1"', '6GB', '256GB', 'A16 Bionic'],
  'RN11': ['Xiaomi', '6.4"', '4GB', '128GB', 'Snapdragon 680'],
  'MOTOG22': ['Motorola', '6.5"', '4GB', '64GB', 'Helio G37'],
  'A34': ['Samsung', '6.6"', '6GB', '128GB', 'Dimensity 1080'],
}

inventario = {
  'S23ULTRA': [999990, 3],
  'IP14PRO': [1399990, 2],
  'RN11': [199990, 10],
  'MOTOG22': [129990, 0],
  'A34': [299990, 6],
}


def stock_marca(marca):
    total = 0 # Guarda el stock disponible por marca
    encontrada = False
    for modelo in catalogo:
        if catalogo[modelo][0].lower() == marca.lower():
            total += inventario[modelo][1]
            encontrada = True
    if encontrada:
        print("Stock disponible: ", total)
    else:
        print("Marca ingresada no entontrada.")

def buscar_por_precio (pmin, pmax):
    lista = []
    for modelo in inventario: 
        precio, stock = inventario[modelo]
        if stock > 0 and pmin <= precio <= pmax: 
            marca = catalogo[modelo][0]
            lista.append(marca + " - " + modelo) # Metodo para agregar valores a una lista
    lista.sort() # Metodo para ordenar los valores alfabeticamente de una lista
    if lista: 
        print("celulares disponibles: ", lista)
    else: 
        print("No hay celulares en ese rango de precios.")

def modificar_precio(modelo, nuevo_precio):
    if modelo in  inventario:
        inventario[modelo][0] = nuevo_precio
        print("Precio actualizado!!")
        print("Modelo: ",modelo," Nuevo precio: ", inventario[modelo][0])
    else: 
        print("El modelo NO existe!!")

while True: 
    print("*** MENU CELLPRO ***")
    print("1.- Ver stock por marca.\n2.- Buscar celulares por precio.\n3.- Modificar precio de un celular.\n4.- Salir.")
    opcion = input("Ingrese su opcion: ")

    if opcion == "1": # Ver stock por marca
        marca = input("Ingrese marca de la marca: ")
        stock_marca(marca)
        # Marcas disponibles :
        # Samsung, Apple, Xiaomi y Motorola

    elif opcion == "2": # Buscar celulares por precio
        while True:
            try:
                pmin = int(input("Ingrese precio minimo: "))
                pmax = int(input("Ingrese precio maximo: "))
                buscar_por_precio(pmin, pmax)
                break
            except ValueError:
                print("Debe ingresar valores enteros!!")

    elif opcion == "3": # Modificar precio de un celular
        modelo = input("Ingrese modelo: ").upper()
        while True:
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                modificar_precio(modelo, nuevo_precio)
                break
            except ValueError:
                print("Debe ingresar un numero entero!!")

    elif opcion == "4": # Salir
        print("Programa finalizado.\nGracias por usar CellPro.")
        break
    else:
        print("Debe seleccionar una opcion valida!!")


#Trabajo Terminado