#randint genera numeros enteros aleatorios
#unifomr genera numeros flotantes aleatorios
#random
import os
from random import randint, uniform,random

def Z():
    a=randint(1,6)
    return a
def R():
    b=uniform(0,100)
    return b
    os.system("cls")
print ("the z number is :",Z())
print ("the z number is :",R())