rios_paises={'Nilo':'Egipto', 'Amazonas':'Colombia', 'Indo':'Pakistán', 'Misisipi':'Estados Unidos','Danubio':'Alemania'}
print(rios_paises)
print()
for key in rios_paises:
    print ('El ',key,' corre a travéz de ',rios_paises[key])
print()
for key in rios_paises:
    print (key)
print()
for key in rios_paises:
    print (rios_paises[key])
print()
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
print()
glosario={'Array':'Es un tipo de dato estructurado que permite almacenar un conjunto de datos homogeneo, es decir, todos ellos del mismo tipo y relacionados.',
          'Clase':'Colección encapsulada de datos y operaciones que actúan sobre los datos.',
          'IDE':'Software para ayudar a los programadores a escribir código eficientemente.',
          'Palabra reservada':'Es una palabra definida como parte del lenguaje de programación y  no se puede utilizar para ningún otro propósito.',
          'OOP':'Un enfoque de programación que implica organización de objetos y sus comportamiento en clases de componentesrealizables.'}
for key in glosario:
    print (key,':',glosario[key])
