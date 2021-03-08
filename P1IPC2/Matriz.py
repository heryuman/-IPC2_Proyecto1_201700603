import ListaCircularSimple


class matrix():


    def __init__(self, filas,columnas,nombre):
        self.filas=filas
        self.columnas=columnas
        self.nombre=nombre
        self.ifil=0
        self.icol=0
        self.Lfila = ListaCircularSimple.ListaCircularSimpl()

    def tamFila(self):
        return self.Lfila.tamanio()

    def getNumFila(self):
        return self.filas
    def getNumColumna(self):
        return self.columnas

    def getPaton(self):
        return self.patron

    def getMatriz(self):
        return self.Lfila

    def getNombreMatriz(self):
        return self.nombre
    def setPatron(self, patron):
        self.patron=patron

    def insertMatriz(self,elemento):

        if self.Lfila.getVacio()== True:
            Lcolumna = ListaCircularSimple.ListaCircularSimpl()
            self.Lfila.addNodoalFinal(Lcolumna)
            self.Lfila.getLista(self.ifil).addNodoalFinal(elemento)
            self.icol += 1

        else:
            if self.icol < self.getNumColumna() :
                self.Lfila.getLista(self.ifil).addNodoalFinal(elemento)
                self.icol += 1
            elif self.icol == ((self.getNumColumna())) :
                Lcolumna = ListaCircularSimple.ListaCircularSimpl()
                self.Lfila.addNodoalFinal(Lcolumna)
                self.icol = 0
                self.ifil += 1
                self.Lfila.getLista(self.ifil).addNodoalFinal(elemento)
                self.icol += 1


    def mostrarmatriz(self):
       for i in range((self.getNumFila())):
           print()
           for j in range ((self.getNumColumna())):

              #if self.Lfila.getLista(i).iterarhasta(j) != None:

                  print(self.Lfila.getLista(i).iterarhasta(j),end="|")

    def mostrarenfilaycolumna(self, fila, columna):
       valor=""
       for i in range((self.getNumFila())):
           #print()
           for j in range ((self.getNumColumna())):

              if i== fila and j == columna:

                 # print(,"mostrar en filay col")
                 valor= self.Lfila.getLista(fila).retornaren(columna)

       return  valor







