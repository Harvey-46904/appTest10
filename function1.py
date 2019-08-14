#function1:multiplicar
## libraries##
import os
#function
def calc(a,b):
    os.system("cls")
    c=a*b
    return c

#Maion#####
os.system("sls")
print("Press number 1: ")
n1=int(input())
n2=int(input("Press number 2: "))

print("the answer is :",calc(n1,n2))

