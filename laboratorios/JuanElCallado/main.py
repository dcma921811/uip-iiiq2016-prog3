
def menu():
    print("***MENU***\n1 Preguntar algo\n2 Salir")

if __name__ == '__main__':
  opcion = 0
  respuesta = 0

while respuesta == 0:

    menu()
    opcion = int(input("Opción: "))

    if opcion == 1:

        pregunta = input("Que quieres preguntarle a Juan?\n")

        b = True

        while b == True:

            if len(pregunta) == 0:
                print("Mmmm")

            elif '?' in pregunta or '¿' in pregunta:
                print("Ofi")

            elif pregunta.isupper():
                print("Chillea")

            else:
                print("Me da igual!")
            b = False
            respuesta = 0

    if opcion == 2:
        respuesta = 1
        pass



