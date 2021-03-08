from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment
import os
from ElementTree_pretty import prettify
from  graphviz import Digraph
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
        if Lmatrices.getVacio()==False:
            Lmatrices.VaciarLista()
            LBinarais.VaciarLista()
<<<<<<< HEAD
            LMatResult.VaciarLista()
=======


            LMatResult.VaciarLista()

>>>>>>> Release4




        CONTMAT = 0
        matrices = doc.getElementsByTagName("matriz")

        for matriz in matrices:

            nombrematriz = matriz.getAttribute("nombre")
            columna= matriz.getAttribute("m")
            fila = matriz.getAttribute("n")
            MatrixN = Matriz.matrix(int(fila),int(columna),nombrematriz)
            Lmatrices.addNodoalFinal(MatrixN)



            datos= matriz.getElementsByTagName("dato")


            for dato in datos:

                posx = dato.getAttribute("x")
                posy = dato.getAttribute("y")
                valor = dato.firstChild.data
                Lmatrices.getLista(CONTMAT).insertMatriz(valor)

            CONTMAT += 1


            print()


        CONTMAT=0


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





    def MostrandoMatBinarias(self):
        for i in range (LBinarais.tamanio()):
           print("*/*/*/*/*/*/*/*/*/*/*/*/")
           print("Patron de la matriz: ", Lmatrices.getLista(i).getNombreMatriz())
           print( LBinarais.getLista(i).mostrarmatriz())

           print("*/*/*/*/*/*/*/*/*/*/*/*/")




    def comparandoBinarias(self):


        for i in range(LBinarais.tamanio()):
            iguales = False


            FilaComparar = []
            flags=[]
            lparecidos = ListaCircularSimple.ListaCircularSimpl()
            ldiferentes=ListaCircularSimple.ListaCircularSimpl()
            it = 0
            seusoPos = None
            NmatrizR = Matriz.matrix(int(LBinarais.getLista(i).getNumFila()),int(LBinarais.getLista(i).getNumColumna()),LBinarais.getLista(i).getNombreMatriz())
            for f in range(LBinarais.getLista(i).getNumFila()):
                flags.append(False)
            for j in range(LBinarais.getLista(i).getNumFila()):

                if flags[j]==False:
                    for k in range(LBinarais.getLista(i).getNumColumna()):

                        FilaComparar.append(LBinarais.getLista(i).mostrarenfilaycolumna(j, k))
                else:
                    ldiferentes.addNodoalFinal(j)




                it += 1
                pos = j
                poa2=0

                # print("it val",it)
                seusoPos = None
                #print(len(FilaComparar))
                if len(FilaComparar)>0:
                    for m in range(it, LBinarais.getLista(i).getNumFila()):
                        iguales = True

                        for n in range(LBinarais.getLista(i).getNumColumna()):

                            if LBinarais.getLista(i).mostrarenfilaycolumna(m, n) != FilaComparar[n]:
                                iguales = False

                        if iguales == True :
                           # print("la fila ", pos + 1, " y la fila ", m + 1, " son iguales? ", iguales)
                            flags[m]=True
                            flags[pos]=True
                            if lparecidos.existe(str(m))==False:
                                lparecidos.addNodoalFinal(m)
                                if lparecidos.existe(str(pos))== False:
                                    lparecidos.addNodoalFinal(pos)
                                else:
                                    print("el pos ya existe")



                lparecidos.MostrarListaPrimeroaUltimo()
                #print("tamLparecidos",lparecidos.tamanio())
                if lparecidos.tamanio()>0:
                    for f in range(Lmatrices.getLista(i).getNumColumna()):
                        suma=0
                        for l in range(lparecidos.tamanio()):
                            suma= suma + int(Lmatrices.getLista(i).mostrarenfilaycolumna(int(lparecidos.iterarhasta(l)),f))
                        #print("suma de la columna",f,"es ",suma)
                        NmatrizR.insertMatriz(suma)

                lparecidos.VaciarLista()
                ldiferentes.VaciarLista()
                FilaComparar.clear()

            for h in range(len(flags)):
                #print("verficando flags")
                if flags[h] == False:

                    for r in range(Lmatrices.getLista(i).getNumColumna()):
                        #print(h)
                        vaal = Lmatrices.getLista(i).mostrarenfilaycolumna(h, r)
                        NmatrizR.insertMatriz(vaal)




            LMatResult.addNodoalFinal(NmatrizR)
            #print("tamMatResul",LMatResult.tamanio())
















    def mostrarMatresult(self):
        for i in range(LMatResult.tamanio()):
            print("Reduccion de la matri",LMatResult.getLista(i).getNombreMatriz(),"filas= ",LMatResult.getLista(i).tamFila(),"columnas ",LMatResult.getLista(i).getNumColumna())
            for j in range(LMatResult.getLista(i).tamFila()):
                for k in range(LMatResult.getLista(i).getNumColumna()):
                            print(LMatResult.getLista(i).mostrarenfilaycolumna(j,k))



#####################SECCION QUE GENERA EL GRAFO ##################

    def CrearGrafo(self):
        lNomMatrix=[]
        d = Digraph(filename='Matrices.gv')
        d.node("MATRICES")
        filas=""
        columnas=""

        for i in range(Lmatrices.tamanio()):
            with d.subgraph() as s:
                s.attr(rank='same')
                nombres=str(Lmatrices.getLista(i).getNombreMatriz())

                s.node(nombres)
                lNomMatrix.append(nombres)
        for i in range (len(lNomMatrix)):
            d.edge("MATRICES",lNomMatrix[i])

        for i in range(len(lNomMatrix)):
            for j in range(Lmatrices.tamanio()):
                filas = str(Lmatrices.getLista(i).getNumFila())
                columnas = str(Lmatrices.getLista(i).getNumColumna())
            d.edge(lNomMatrix[i],"m_"+str(i)+"= "+filas)
            d.edge(lNomMatrix[i],"n_"+str(i)+"= "+columnas)

        for j in range(Lmatrices.tamanio()):
            m2=0
            for k in range(1):#fila
                for m in range(Lmatrices.getLista(j).getNumColumna()):#columna

                        m2=m2+1

                        etiqueta=Lmatrices.getLista(j).mostrarenfilaycolumna(k, m)
                        d.node(str(m2)+Lmatrices.getLista(j).getNombreMatriz(),etiqueta)

        for i in range(Lmatrices.tamanio()):
            m2 = 0
            for k in range(1):
                for m in range(Lmatrices.getLista(i).getNumColumna()):
                    m2 = m2 + 1
                    d.edge(str(lNomMatrix[i]), str(m2)+Lmatrices.getLista(i).getNombreMatriz())

        for i in range (Lmatrices.tamanio()):
            m2=0
            for j in range(Lmatrices.getLista(i).getNumFila()):
                for k in range(Lmatrices.getLista(i).getNumColumna()):
                    m2=m2+1
                    label=Lmatrices.getLista(i).mostrarenfilaycolumna(j, k)
                    d.node(str(m2)+str(Lmatrices.getLista(i).getNombreMatriz()),label)

        for i in range(Lmatrices.tamanio()):
            inicio=1
            m2=0
            for j in range(Lmatrices.getLista(i). getNumFila()-1):
                for k in range(Lmatrices.getLista(i).getNumColumna()):
                    m2=m2+1
                    inicio=str(m2)+Lmatrices.getLista(i).getNombreMatriz()
                    f =m2+Lmatrices.getLista(i).getNumColumna()
                    fin=str(f)+Lmatrices.getLista(i).getNombreMatriz()
                    d.edge(inicio,fin)




        d.view()

    def ListaDematricesaDibujar(self):
        lNomMatrix=[]
        d = Digraph(filename='Matrices.gv')
        d.node("MATRICES")
        filas=""
        columnas=""
        print("Ingrese el Numero de la matriz a Dibujar")

        for i in range(Lmatrices.tamanio()):
            print(i+1,"_ ",Lmatrices.getLista(i).getNombreMatriz())

        op=input()
        self.CrearGrafo2(int(op)-1)

    def CrearGrafo2(self,pos):
        lNomMatrix=[]
        d = Digraph(filename='Matrices.gv')
        d.node("MATRICES")
        filas=""
        columnas=""
        nombre=""


        with d.subgraph() as s:
            s.attr(rank='same')
            nombre=str(Lmatrices.getLista(pos).getNombreMatriz())

            s.node(nombre)

        d.edge("MATRICES", nombre)

        with d.subgraph() as sb:
            sb.attr(rank='same')
            filas = str(Lmatrices.getLista(pos).getNumFila())
            columnas = str(Lmatrices.getLista(pos).getNumColumna())

            sb.node("idF","m= "+filas)
            sb.node("idC","n= "+columnas)
        d.edge(nombre,"idF")
        d.edge(nombre,"idC")

        m2 = 0
        for k in range(Lmatrices.getLista(pos).getNumFila()):  # fila
            for m in range(Lmatrices.getLista(pos).getNumColumna()):  # columna

                m2 = m2 + 1

                etiqueta = Lmatrices.getLista(pos).mostrarenfilaycolumna(k, m)
                d.node(str(m2) + Lmatrices.getLista(pos).getNombreMatriz(), etiqueta)

        m2=0
        for j in range(1):
            for k in range(Lmatrices.getLista(pos).getNumColumna()):
                m2 = m2 + 1
                f = str(m2 )+ Lmatrices.getLista(pos).getNombreMatriz()

                d.edge(nombre, f)

        inicio = 1
        m2 = 0
        for j in range(Lmatrices.getLista(pos).getNumFila() - 1):
            for k in range(Lmatrices.getLista(pos).getNumColumna()):
                m2 = m2 + 1
                inicio = str(m2) + Lmatrices.getLista(pos).getNombreMatriz()
                f = m2 + Lmatrices.getLista(pos).getNumColumna()
                fin = str(f) + Lmatrices.getLista(pos).getNombreMatriz()
                d.edge(inicio, fin)

        d.view()

    def salidaxml(self):

        top = Element('Matrices')

        comment = Comment('Generado por Selvin')
        top.append(comment)
        """
        child = SubElement(top, 'Matriz', nombre="loquesea", m="1", n="2")
        child2 = SubElement(child, 'dato', x="1", y="2")
        child2.text = '5' """



        for i in range(LMatResult.tamanio()):
            child=SubElement(top,'matriz',nombre=str(LMatResult.getLista(i).getNombreMatriz())+'_salida',n=str(LMatResult.getLista(i).tamFila()),m=str(LMatResult.getLista(i).getNumColumna()),g=str(LMatResult.getLista(i).tamFila()))
            for j in range(LMatResult.getLista(i).tamFila()):
                for k in range(LMatResult.getLista(i).getNumColumna()):
                    child2= SubElement(child,'dato',x=str(j+1),y=str(k+1))
                    child2.text = str(LMatResult.getLista(i).mostrarenfilaycolumna(j,k))

        file = open("salida.xml", "w")
        file.write(str((prettify(top))))

        file.close()




























