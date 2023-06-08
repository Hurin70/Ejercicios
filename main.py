"""n = int(input('inserta un numero'))
n2 = int(input('inserta un numero'))
if n > n2:
    print ('n es mayor que n2')

if n <= n2:
    print(str(n) + ' es menor que '+ str(n2)"""

"""galletas = True;
if galletas == True:
    print ("Hay galletas")

else:
    print( "no hay galletas")"""

"""num == 7
if num ==0:
    print("num es igual a 0")
else: 
    if num ==1:
        print("num es igual a 1")"""
"""for i in range (10):
    print (i)"""

'''or letra in "Hola":
        print(letra)'''

'''n = 14
while n > 1:
    print(n)
    n-=1'''

'''n2 = 99
while n2 > 90 and (n2%2==1):
    print(n2)
    n2-=2'''

'''EJERCICIO 1'''

'''n1 = int(input('inserta un numero'))
n2 = int(input('inserta un numero'))
n3 = int(input('inserta un numero'))
if n1 < n2:
    if n1 < n3:
        print ('n1 es el menor de los 3')
if n2 < n1:
    if n2 < n1:
        print ('n2 es el menor de los 3')
if n3 < n1:
    if n3 < n1:
        print ('n3 es el menor de los 3')'''

'''EJERCICIO 2'''

'''n1 = int(input('inserta un numero'))
n2 = int(input('inserta un numero'))
n3 = int(input('inserta un numero'))
if n1 < n2 and n1 < n3:
        print ('n1 es el menor de los 3')
if n2 < n1 and n2 < n3:
        print ('n2 es el menor de los 3')
if n3 < n1 and n2:
          print ('n3 es el menor de los 3')'''\

'''frase = input ('inserte una frase: ')
letra = input ('¿que letra quieres contar?: ')
contador = 0
for caracter in frase:
    if letra == caracter:
        contador += 1
print ('la letra '+ letra +' se repite '+ str (contador)+' veces')'''

'''EJERCICIO 3'''

'''n1 = int (input ('inserte numero 1 '))
n2 = int (input ('inserte numero 2 '))
pregunta = input ('¿que quiere hacer sumar(s) + restar (r)? ')
if pregunta == 's':
    resultado = n1+n2
if pregunta == 'r':
    resultado = n1-n2
print ('el resultado es '+ str (resultado))'''

'''EJERCICIO 4'''


'''USER = 'Dani' # User correcto
PASS = '123' # Pass correcto
cont = 0
login = False
while cont < 3 and login == False:
    usuario = input('introduzca usuario: ')
    contrasena = input('introduzca contraseña: ')
    if usuario == USER and contrasena == PASS:
        print('bienvenido')
        login = True
    else:
        print('usuario o contraseña incorrecta')
        cont = cont+1
    if cont == 3:
        print('usuario bloqueado')'''


'''_____________________________________________________________________________________________'''

'''Frameworks de empleo: "Data Science"
    -Spring
    -Muc
    -Asp.net
    -Core MVC
    -Django (desarrollo app web)

__________________________________________________________________________________________________

Al importa funciones para python

Clase:
    Propiedades: 
        Metodos == Funciones
Ejemplo:

from math import floor, ceil

        from = ruta de clar
        math = clase de artchivo a importar
        import = acción que pedimos
        Floor and ceil, son las funciones que importamos
        
___________________________________________________________________________________________________

  input % + (un numero)
   Esto, divide el numero que se mete por imput por el numero que se indique, y te muestra el resto
___________________________________________________________________________________________________

Podemos utilizar el SubString de otros lenguajes de programación
EJEMPLOS:'''

'''s = 'Hello, everybody!'
>>> s[0] #(Aquí, se le puede inidcar un valor, si se le indica cero o nada, empieza desde el principio y solo coge la letra inical)
'H'
>>> s[:3] #(cuando no se le indica el valor inicial, inicia desde cero hasta la posición 3)
'Hel'
>>> s[2:5] #(aquí se indica que empiece desde la posición 2 hasta la posición 5) 
'llo'
'''
'''
______________________________________________________________________________________________________
CONGETURA DE COLLATZ
    
num = int(input('Introduzca un numero '))

while num != 1: #si el numero NO es 1 se mantiene el bucle
    if (num % 2 == 0):# si sigue en el bucle (el numero se divide entre 2 y te da el resto) "num%2", si el resto es 0, el numero es par
        num = num /2 # sise cumple el "if" y el numero es par, se divide entre 2
    else:
        num = (num * 3) + 1  # si no se cumple el if, se entiende que el numero no es par, entonces se multiplica por 3
    print(num) # cuando se han cumplico las operaciones, print num, muestra todos los pasos por los que ha pasado "num"
    '''
'''
t(f'el v

#Rango
for i in range(0,10): # se especifica que el rango de valores que se muestran va del 0 al 10-1)
    prinalor de i es :{i}')
#Incrementos
for i in range(0,10,2): # al añadir el 2 en el rango de busqueda, se especifica que se busquen solo los pares)
    print(f'el valor de i es :{i}')
'''
