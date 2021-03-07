
import LeerXml
import ListaCircularSimple



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
   lector = LeerXml.LeerXml("C:/Users/ASUS/Documents/ProyectosIPCPS2021/matrices.xml")
   lector.readPath()
   lector.imprimirLmatrices()
   lector.CreandoMatrizBinaria()
   lector.MostrandoMatBinarias()
   #lector.comparandoPatrones()
   #lector.MostrarLResultados()
   print( lector.comparandoBinarias())




""" 
matriz1= Matriz.matrix(4,6,"prueba")
   i = 0
   j = 0
   cont =1
   while i < matriz1.getNumFila():
       while j < matriz1.getNumColumna():
          # print("insertando ",cont)
           #print("en fila",i,"col ",j)
           matriz1.insertMatriz(cont)
           j+=1
           cont += 1

       i+=1
       j=0
 #  print("nuevo tam de i ",i)
   matriz1.mostrarmatriz()

   matriz2 = Matriz.matrix(6, 4, "prueba2")

   ix = 0
   jx = 0
   cont2 = 1
   while ix < matriz2.getNumFila():
        while jx < matriz1.getNumColumna():
            # print("insertando ",cont)
            # print("en fila",i,"col ",j)
            matriz2.insertMatriz(cont2)
            jx += 1
            cont2 += 1

        ix += 1
        jx = 0
   print()
   print("nom: ",matriz2.getNombreMatriz())
   matriz2.mostrarmatriz()

   lista=ListaCircularSimple.ListaCircularSimpl()
   lista.addNodoalFinal(4)
   lista.addNodoalFinal("c")
   lista.addNodoalFinal(5)
   lista.addNodoalFinal(8)
   lista.addNodoalFinal("d")

   lista2 = ListaCircularSimple.ListaCircularSimpl()
   lista2.addNodoalFinal("l")
   lista2.addNodoalFinal("s")
   lista2.addNodoalFinal("k")

   lista3=ListaCircularSimple.ListaCircularSimpl()
   lista3.addNodoalFinal(lista)
   lista3.addNodoalFinal(lista2)
   print()
   print()
   print(lista3.getLista(0).MostrarListaPrimeroaUltimo())



    columna.addNodoalFinal(9)
    columna.addNodoalFinal(8)
    columna.addNodoalFinal(7)
    fila.addNodoalFinal(45)
    columna2.addNodoalFinal(fila)
    columna2.addNodoalFinal(9)
    columna2.addNodoalFinal(8)
    columna2.addNodoalFinal(7)

    #print ("imprimiendo en la posicion 2")
    columna.iterarhasta(2)
    columna.getLista(3).MostrarListaPrimeroaUltimo()
    Lfila.getLista(i).
"""


if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
