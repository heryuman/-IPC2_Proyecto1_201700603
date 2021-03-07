from xml.dom import minidom
import ListaCircularSimple
import Matriz


Lmatrices=ListaCircularSimple.ListaCircularSimpl()
LBinarais=ListaCircularSimple.ListaCircularSimpl()
LindicesaSumar=ListaCircularSimple.ListaCircularSimpl()
LMatResult=ListaCircularSimple.ListaCircularSimpl()


class LeerXml(object):
    def __init__(self,ruta):
        self.ruta=ruta

    def getRuta(self):
        return self.ruta

    def readPath(self):
        # doc = minidom.parse("/ruta/datos.xml")

        doc = minidom.parse(self.getRuta())

        #nombre = doc.getElementsByTagName("nombre")[1]
        #print(nombre.firstChild.data)

        CONTMAT = 0
        matrices = doc.getElementsByTagName("matriz")

        for matriz in matrices:

            nombrematriz = matriz.getAttribute("nombre")
            fila= matriz.getAttribute("m")
            columna = matriz.getAttribute("n")
            MatrixN = Matriz.matrix(int(fila),int(columna),nombrematriz)
            Lmatrices.addNodoalFinal(MatrixN)



            datos= matriz.getElementsByTagName("dato")
           # print("nombre:%s " % nombrematriz)
           # print("Filas:%s"% fila)
           # print("columnas:%s" % columna)
           # print()

            for dato in datos:

                posx = dato.getAttribute("x")
                posy = dato.getAttribute("y")
                valor = dato.firstChild.data
                Lmatrices.getLista(CONTMAT).insertMatriz(valor)


               # LMAT[CONTMAT].insertMatriz(valor)
               # print("tam matrix ",MatrixN.getNumFila()," X ",MatrixN.getNumColumna())
                #print("posX:%s" % posx)
                #print("posY:%s" % posy)
               # print("valor:%s" % valor)


            CONTMAT += 1

            #print("Nombre: ",MatrixN.getNombreMatriz(), "m = ", MatrixN.getNumFila(), "n= ",MatrixN.getNumColumna() )
            #MatrixN.mostrarmatriz()
           # print("*/*/*/*/*/*/*FIN DE MATRIZ/*/*/*/*/*/")
            print()

            #Lmatrices.addNodoalFinal(MatrixN)
           # print("contmat",CONTMAT)
        CONTMAT=0
       # print("tamanio Lista matrices ",Lmatrices.tamanio())

    def imprimirLmatrices(self):
        for i in range(Lmatrices.tamanio()):
            print("nombre de La matriz: ",str(Lmatrices.getLista(i).getNombreMatriz()), "tamanio: ",Lmatrices.getLista(i).getNumFila(), " X ",Lmatrices.getLista(i).getNumColumna())
            #if Lmatrices.getLista(i).mostrarmatriz()!= None:
            print(Lmatrices.getLista(i).mostrarmatriz())
            #Lmatrices.DeleteUltimo()
            #print(Lmatrices.getLista(i).mostrarmatriz())
            print()
            print("/*/*/*/*/*/**/*/")
            print()


    def CreandoMatrizBinaria(self):

        for i in range(Lmatrices.tamanio()):

            NuevaMatBinaria=Matriz.matrix(int(Lmatrices.getLista(i).getNumFila()),int(Lmatrices.getLista(i).getNumColumna()),Lmatrices.getLista(i).getNombreMatriz())
            for j in range(Lmatrices.getLista(i).getNumFila()):
                for k in range(Lmatrices.getLista(i).getNumColumna()):
                    #print("mostrando desde Matriz Binaria",Lmatrices.getLista(i).mostrarenfilaycolumna(j, k)," fila: ",j+1, " columna: ", k+1)
                    if int(Lmatrices.getLista(i).mostrarenfilaycolumna(j, k)) > 0:
                        NuevaMatBinaria.insertMatriz(1)
                    else:
                        NuevaMatBinaria.insertMatriz(0)

            LBinarais.addNodoalFinal(NuevaMatBinaria)

    def comparandoBinarias(self):


        for i in range(LBinarais.tamanio()):
            iguales = False
            FilaComparar = []
            it = 0
            NmatrizR = Matriz.matrix(int(LBinarais.getLista(i).getNumFila()),
                                     int(LBinarais.getLista(i).getNumColumna()),
                                     LBinarais.getLista(i).getNombreMatriz())
            for j in range(LBinarais.getLista(i).getNumFila()):

                for k in range(LBinarais.getLista(i).getNumColumna()):
                    FilaComparar.append(LBinarais.getLista(i).mostrarenfilaycolumna(j, k))
                it += 1
                pos = j
                poa2=0
                print(FilaComparar)
                # print("it val",it)

                for m in range(it, LBinarais.getLista(i).getNumFila()):
                    iguales = True
                    for n in range(LBinarais.getLista(i).getNumColumna()):

                        if LBinarais.getLista(i).mostrarenfilaycolumna(m, n) != FilaComparar[n]:
                            iguales = False

                    if iguales == True:
                        print("la fila ",pos+1," y la fila ", m + 1, " son iguales? ", iguales)
                        for s in range(Lmatrices.getLista(i).getNumColumna()):
                            suma = int(Lmatrices.getLista(i).mostrarenfilaycolumna(pos,s))+int(Lmatrices.getLista(i).mostrarenfilaycolumna(m,s))

                FilaComparar.clear()










    def MostrandoMatBinarias(self):
        for i in range (LBinarais.tamanio()):
           print("*/*/*/*/*/*/*/*/*/*/*/*/")
           print("Patron de la matriz: ", Lmatrices.getLista(i).getNombreMatriz())
           print( LBinarais.getLista(i).mostrarmatriz())

           print("*/*/*/*/*/*/*/*/*/*/*/*/")

        #LBinarais.DelLista(0)



    def GetFilas(self,posicion):
        fila= int(Lmatrices.getLista(posicion).getNumFila())
        return fila

    def GetColumnas(self,posicion):
        columna = int(Lmatrices.getLista(posicion).getNumColumna())
        return columna

    def ObteniendoPatrones(self, posicion):
        Lpatrones = []
        patron=""
        for j in range(LBinarais.getLista(posicion).getNumFila()):
            for k in range(LBinarais.getLista(posicion).getNumColumna()):
                patron = patron + str(LBinarais.getLista(posicion).mostrarenfilaycolumna(j, k))

            Lpatrones.append(patron)
            patron = ""


        #Lpatrones.MostrarListaPrimeroaUltimo()
        return Lpatrones


    def comparandoPatrones2(self):
        for i in range(Lmatrices.tamanio()):
            jt=len(self.ObteniendoPatrones(i))
            kt=len(self.ObteniendoPatrones(i))
            kdel=0
            for j in    range(jt):
                val1=0
                val2=0
                lmatch=ListaCircularSimple.ListaCircularSimpl()
                for k in range(kt):
                    if self.ObteniendoPatrones(i)[j]== self.ObteniendoPatrones(i)[k] and j!=k:
                        val1=j
                        val2=k
                        #print("en pat2",self.ObteniendoPatrones(i)[j])
                        if lmatch.existe(val2)== False:
                            lmatch.addNodoalFinal(val2)
                            self.ObteniendoPatrones(i).pop(val2)

                if lmatch.existe(val1) == False:
                    lmatch.addNodoalFinal(val1)
                lmatch.MostrarListaPrimeroaUltimo()
                print("akjsfklasdf")
            self.ObteniendoPatrones(i).pop(val1)
            LindicesaSumar.addNodoalFinal(lmatch)








    def comparandoPatrones(self):
       # print("desdecomparando")

        posk=1
        #self.ObteniendoPatrones(1).MostrarListaPrimeroaUltimo()
        for i in range(Lmatrices.tamanio()):
           NuevaMatrisResulado = Matriz.matrix(4, int(Lmatrices.getLista(i).getNumColumna()),Lmatrices.getLista(i).getNombreMatriz())
           for s in range(Lmatrices.getLista(i).getNumFila()):
               resultado = 0
               val1 = 0
               for m in range(Lmatrices.getLista(i).getNumColumna()):

                   for j in range(self.ObteniendoPatrones(i).tamanio()):
                       for k in range(self.ObteniendoPatrones(i).tamanio()):
                           if self.ObteniendoPatrones(i).iterarhasta(j) == self.ObteniendoPatrones(i).iterarhasta(k) and j != k :
                               val1 = int(Lmatrices.getLista(i).mostrarenfilaycolumna(j, m))
                               val2 = int(Lmatrices.getLista(i).mostrarenfilaycolumna(k, m))
                               resultado = resultado + val2

                   NuevaMatrisResulado.insertMatriz(resultado + val1)
                   resultado=0
                   val1=0

        LMatResult.addNodoalFinal(NuevaMatrisResulado)


    def MostrarLResultados(self):
        for i in range(LMatResult.tamanio()):
            print("tam Lresult ",LMatResult.tamanio())
            print("*/*/*/*/*/*/*/*/*/*/*/*/")
            print("Resultados de la matriz: ", LMatResult.getLista(i).getNombreMatriz())
            print("tamaio de la matriz. filas",LMatResult.getLista(i).tamFila(),"columnas: ",LMatResult.getLista(i).getNumColumna())
            LMatResult.getLista(i).mostrarmatriz()

            print("*/*/*/*/*/*/*/*/*/*/*/*/")

















