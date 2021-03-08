class Node(object):
    def __init__(self,elemento):
        self.elemento=elemento
        #puntero que servira para unir a los nodos cuando se construya la lista
        self.pSig = None

    def getElemento(self):
        return self.elemento