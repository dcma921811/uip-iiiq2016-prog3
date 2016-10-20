
temp = 0
respuesta = ''


def escribirArchivo(var):

    archivo = open('temp.dat', 'a')
    archivo.write(var+"\n")

def cerrarArchivo():
    archivo = open('temp.dat', 'a')
    archivo.close()



b = True

try:

    while b == True:

        temp = input(" Ingresa tu temperatura: ")
        if(float(temp) > 37.5):
            r = 'Fiebre' + ' ' + temp
            escribirArchivo(r)
            cerrarArchivo()
        elif(float(temp) < 30.0):
            r = 'Estas enfermo' + ' ' + temp
            escribirArchivo(r)
            cerrarArchivo()
        elif(float(temp) < 5.0):
            r = 'Estas muerto' + ' ' + temp
            escribirArchivo(r)
            cerrarArchivo()
        else:
            print("Estas bien")

        cerrarArchivo()

except Exception:
    print("Intente de nuevo")
    b = False




