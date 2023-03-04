controladora = 100
print("**** Empanadas el machetico ****")
print("********************************")
print("1. Agregar sabor de empanada")
print("2. mostrar sabor de empanada")
print("3. editar y cambiar sabor de empanada")
print("0. SALIR")


while controladora != 0 :
    empanada = None
    controladora = int(input("Digita una opción: "))
    if controladora == 1:
        empanada = input("Cuál es el sabor: ")
    elif controladora == 2:
        print("El sabor es: {empanada}")
    elif controladora == 3:
        empanada = input("Cuál es el sabor: ")
    elif controladora == 0:
        print("Vuelve pronto")
    else:
        print("Opción invalida")
        
        