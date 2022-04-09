print ('Este programa sirve para determinar en que posicion esta las palabras de una frase')
frase= str(input('intoduce una frase  '))

for i, c in enumerate(frase):
    print('caracter: %s - indice: %i' % (c,i))