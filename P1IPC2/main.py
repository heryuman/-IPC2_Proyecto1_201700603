
import LeerXml
import crearXML
import ListaCircularSimple
def menu():
    opcion=0
    print("PROYECTO_1 IPC2 SECCION  A")
    print("Eliga una Opcion")
    print()
    print("1. Cargar Archivo")
    print("2. Procesar Arcchivo")
    print("3. Escribir Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Grafica")
    print("6. Salir")


def menu2():

    opcion=""


    while opcion != "6":
        menu()
        opcion = input()
        if opcion == "1":
            print("ingrese la Ruata del XML a cargar")
            ops=input()
            lector = LeerXml.LeerXml(ops)
            lector.readPath()
            lector.imprimirLmatrices()
            print("Se han cargado los datos correctamente")


        elif opcion == "2":
            print("Se esta procesando el archivo...")
            lector.CreandoMatrizBinaria()
            lector.MostrandoMatBinarias()
            lector.comparandoBinarias()
            print("Se ha procesado los datos correctamente")
            print()
        elif opcion == "3":
            print("Se esta escribiendo el archivo de salida")
            lector.salidaxml()
        elif opcion == "4":
            print("Los datos del estudiante son:")
            print("Selvin Orlando Hernandez Yuman")
            print("201700603")
            print("Introduccion a la programacin y computacion 2 Seccion A")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")
            print()
        elif opcion == "5":
            print("se Esta generando la grafia...")
            print("Elija una Opcion:")
            print()
            print("a. Graficar todas las Matrices")
            print("b. Graficar una Matriz Especifica")
            op=input()
            if op== "a":
                lector.CrearGrafo()
            elif op=="b":
                lector.ListaDematricesaDibujar()
            else:
                print("Opcion Invalida")


        else:
            print("Opcion incorrecta, ingrese una opcion valida")





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
   lector = LeerXml.LeerXml("C:/Users/ASUS/Documents/ProyectosIPCPS2021/matrixami.xml")
   lector.readPath()
   lector.imprimirLmatrices()
   #lector.CrearGrafo()
   lector.CreandoMatrizBinaria()
   lector.MostrandoMatBinarias()
   lector.comparandoBinarias()
   #lector.mostrarMatresult()
   lector.salidaxml()
   #lector.prettify()
   #lector.MostrarLResultados()
   #lector.ListaDematricesaDibujar()
   #print( lector.)





if __name__ == '__main__':
   #print_hi('PyCharm')
    menu2()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
