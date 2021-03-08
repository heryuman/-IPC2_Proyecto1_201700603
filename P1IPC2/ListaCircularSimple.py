import Nodo

class ListaCircularSimpl(object):
    def __init__(self):
        self.contador=0
        self.primero = None
        self.ultimo = None



    def getVacio(self):
        if self.primero == None:
            return True
        else:
            return False

    def VaciarLista(self):
        self.primero=None
        self.ultimo=None
        self.contador=0




    def addNodoalFinal(self,elemento):
        nuevo = Nodo.Node(elemento)
        if self.getVacio()== True:
            self.primero =self.ultimo = nuevo
            self.ultimo.pSig = self.primero
        else:
            #el ultimo siguiente apunta al nodo nuevo
            self.ultimo.pSig =nuevo
            #la etiqueta ultimo deja de apuntar al
            # nodo que apuntaba para apuntar al nuevo nodo
            self.ultimo = nuevo
            #el nuevo ultimo reconocido como ultimo deja de apuntar a null
            #apunta al primero
            self.ultimo.pSig = self.primero
        self.contador+=1


    def DeleteUltimo(self,limite):
        print("deleteulti")
        if self.getVacio() == True:
            print ("Lista Vacia imposible eliminar")

        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
            print ("Elemento Eliminado. La lista esta Vacia")
        else:
            i=0
            validar = True
            temp = self.primero
            if limite< self.contador:
                while (i < limite-1):
                    if i < limite:
                        """temp2 = self.ultimo
                        self.ultimo = temp
                        self.ultimo.pSig = self.primero
                        temp2 =None
                        validar = False
                        print ("Elemento Eliminado")
                        """
                        print("siireta")
                        temp = temp.pSig
                        i += 1
                temp.pSig=temp.pSig



                print("elemento Eliminado")




    def tamanio(self):
        return self.contador



    def MostrarListaPrimeroaUltimo(self):
        if self.getVacio() == True:
            print ("Lista Vacia")
        else:
            validar = True
            temp = self.primero
            while(validar):

                print (temp.getElemento())
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.pSig


    def iterarhasta(self,limite):
        i = 0
        if self.getVacio() == True:
            print ("Lista Vacia")
        else:


            temp = self.primero
           # print ("el tam de la lista",self.contador)
            if limite < ((self.contador)):
                while (i < limite):
                  #  print ("en el while")
                    if i< limite:
                      #  print ("en el if dentro del while")
                        i+=1
                        #print ("el valor de i, ",i," el valor del limte", limite)
                        temp = temp.pSig

                return temp.getElemento()

    def EliminarEn(self,limite):

            i = 0
            if self.getVacio() == True:
                print("Lista Vacia")
            else:

                temp = self.primero
                pre = None
                # print ("el tam de la lista",self.contador)
                if limite < ((self.contador)):
                    while (i < limite):
                        #  print ("en el while")
                        if i < limite:
                            #  print ("en el if dentro del while")
                            i += 1
                            pre = temp
                            # print ("el valor de i, ",i," el valor del limte", limite)
                            temp = temp.pSig

                    pre.pSig = temp.pSig
                    self.contador-=1
                    print("/*/Dato Eliminado*/*")



    def DelLista(self,pos):
        return self.EliminarEn(pos)



    def obtenerenlaposicion(self,limite):
        i = 0
        if self.getVacio() == True:
            print ("Lista Vacia")
        else:


            temp = self.primero
           # print ("el tam de la lista",self.contador)
            if limite < ((self.contador)):
                while (i < limite):
                  #  print ("en el while")
                    if i< limite:
                      #  print ("en el if dentro del while")
                        i+=1
                        #print ("el valor de i, ",i," el valor del limte", limite)
                        temp = temp.pSig

                return temp.getElemento()

    def retornaren(self,limite):
        i = 0
        if self.getVacio() == True:
            print ("Lista Vacia")
        else:


            temp = self.primero
           # print ("el tam de la lista",self.contador)
            if limite < ((self.contador)):
                while (i < limite):
                  #  print ("en el while")
                    if i< limite:
                      #  print ("en el if dentro del while")
                        i+=1
                        #print ("el valor de i, ",i," el valor del limte", limite)
                        temp = temp.pSig

                return temp.getElemento()


    def existe(self,nombre):
        exist=False
        if self.getVacio() == True:
            return exist
        else:
            temp = self.primero
            for i in range(self.contador):

                if str(temp.getElemento())== nombre:
                    exist=True

                else:
                    temp= temp.pSig

        return exist




    def getLista(self, limite):
        i = 0
        if self.getVacio() == True:
            print ("Lista Vacia desde getlista")
        else:

            temp = self.primero
           # print ("el tam de la lista", self.contador)
            if limite < ((self.contador)):
                while (i < limite):
                   # print ("en el while")
                    if i < limite:
                       # print ("en el if dentro del while")
                        i += 1
                       # print ("el valor de i, ", i, " el valor del limte", limite)
                        temp = temp.pSig

                return  temp.getElemento()



            else:
                print ("intervalo incorrecto")

