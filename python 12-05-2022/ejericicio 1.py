lista1=[]
lista2=[]
#6
# 1valor=int(input('escriba un numero:  ')) si se agrega esto otra vez sale error
for x in range(10):
    valor=int(input('escriba un numero:  '))
    
    if valor%2==0:
        lista1.append(valor)
    else:
        lista2.append(valor)
 
print('lista 1',lista1)
print('lista 2',lista2)
