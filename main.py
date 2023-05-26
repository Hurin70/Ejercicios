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


USER = 'Dani' # User correcto
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
        print('usuario bloqueado')
   

