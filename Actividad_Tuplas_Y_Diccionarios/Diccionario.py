huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'} # hacer un diccionarion con su clave y valor.



print (huespedes) #imprimir el diccionario
print (huespedes.items()) # imprimir los items en el diccionario

print (huespedes.keys()) #imprimir las claves
for key in huespedes: # imprimir individualmente las claves con un for
    print (key)

print (huespedes.values()) #imprimir los valores del diccinario
for key in huespedes: # imprimir individualmente las claves con un for
    print (huespedes[key])
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion]) #Imprimir individualmente con un for las habitaciones : con sus respectivos huespedes
print()
for habitacion,huesped in huespedes.items(): #
    print (habitacion,':',huespedes[key])
for indice, key in enumerate(huespedes): # imprimir el nombre del huerped con su respectiva habitacion ademas de enumerarlos del 1 al 3
    print (indice+1,key,huespedes[key])
print()

print (huespedes[105]) #Iprimir el nombre del huesped con la clave 105
print (huespedes.get(105)) #"Traer"  e imprimir el nomnre del hueesped con la clave 105

print ('====================================')

huespedes[102]='Fanny Lu' #Agregar mas huespedes con sus respectivas claves al diccionario
huespedes[107]='Don Omar' #Agregar mas huespedes con sus respectivas claves al diccionario
huespedes.setdefault('109','Luis Miguel') #Agregar mas huespedes con sus respectivas claves al diccionario

for huesped in huespedes.items():
    print (habitacion,':',huesped) #Imprimir el diccionario con las nuevas modificaciones hechas.
print()

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'} # Hacer un segundo diccionario con las personas que se registraron ese dia
huespedes.update(registroshoy) # se agrega al primer diccionario los datos de los huespedes del segundo diccionario
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped) # se imprime el primer diccionario ya actualizado con los nuevos huespedes incluidos.
print()

print ('====================================')

huespedes[107]='Ricky Martin'
print (huespedes) # se cambia al huesped con la clave 107 "Don Omar" por "Ricky Martin" y se imprmie el diccionario con el cambio hecho

print ('====================================')


del huespedes[102]
huespedes.pop(202) #Se imprimer solos los huespedes en un rango de claves.
print(huespedes)

print ('====================================')

copia1=huespedes.copy()
print ('copia1: ',copia1)  #Se hace una copia de la lista y se imprime
copia2={}
copia2.update(huespedes) # A una lista vacia se actualiza o llena con los datos de las lista preexistente de huespedes y se llama copia 2
print ("copia2: ",copia2)

print ('====================================')

lista=[2,5,7,1] # se crea otra lista nueva
diccio=dict.fromkeys(lista,"xxx") #se agrega xxx a cada item de la lista
print(diccio) #se imprime

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1} #Se crea un diccionario con item y subitems
print (inventario) # se imprime el diccionario
inventario["cartera"].sort() #Se organizan alfabeticamnete los subitems del item cartera
print(inventario) # se imprime el diccionario
inventario["cartera"].remove("Moneda") # del item cartera se elimina el subitem Moneda.
print(inventario) # se imprime el diccionario
print(inventario.get("plata")[0]) #del item plata se imprime el subitem que tiene la posicion 0.
