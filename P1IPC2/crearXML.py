from xml.etree.ElementTree import Element, SubElement, Comment
import os
from ElementTree_pretty import prettify

top = Element('Matrices')

comment = Comment('Generado por Selvin')
top.append(comment)

child = SubElement(top,'Matriz',nombre="loquesea", m="1", n="2")
child2= SubElement(child,'dato',x="1",y="2")
child2.text = '5'


def ptfy():
    file = open("salida.xml", "w")
    file.write(str((prettify(top))))

    file.close()

