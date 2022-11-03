t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe') #Creación de una tupla llamada t.
print (t) #Mostara/imprimir en pantalla la tupla.
print (len(t)) #Se imprime en pantalla la cantidad de items en la tupla.


print ('=====================================')  #Imprime lineas
print (t[0]) #Imprime el item que esta en la pocisión 0, las tuplas se enumeran empezando desde cero
print (t[3]) #Imprime el item que esta en la pocisión 3
print (t[1:3]) #Imprime los itemes desde la pocición 1 hasta el 3 sin incluir.
print (t[3][1]) #Imprime de la tupla el subitem en la posición 1 del item en la posición 3.


print ('====================================') #Imprime lineas
print (t[3])  #Imprime el item que esta en la pocisión 3
t[3].append('lorito') #Agrega al item en la pocición 3 otra palabra
print (t) #Mostara/imprimir en pantalla la tupla.

print ('====================================') # De la linea 18 a 20 es para imprimir individualmente cada elemento en la tupla por medio de un for.
for elemento in t:
    print (elemento)

print ('====================================') #De la linea 22 a 24 se imprimer individualmente cada uno de los elementos de la tupla solo que esta vez se usa un for para ir imprimiendo por las pociciones en las que estan desde cero hasta <la cantidad de items en la tupla.
for index in range(0,len(t)):
    print (t[index])

print ('====================================') # Se verifica si cirto elemento esta en la tupla y si es cierto de imprime un mensaje.
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")

print ('====================================')
lista=list(t) #se convierte la tupla en una lista
lista[1]='A' # se sustituye en item en la pocición 1 por otro.
print (lista) # se imprime la lista

tupla=tuple(lista) #se covierte la lista en tupla.
print (tupla) # se imprime la tupla

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)] #Lista con elementos
for x, y in l: #For loop para ir agregando : entre los numeros en los subitems de la lista.
    print (x, ':', y)
