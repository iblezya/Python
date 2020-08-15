#Expresiones regulares
#
#Punteros (Comodines
#\d = un solo digito [0-9]
#\D = cualquier caracter que NO sea un digito[0-9]
#\w = cualquier caracter alfanumerico[0-9A-Za-z]
#\W= cualquier caracter que NO sea un alfanumerico
import re
cadena = 'sol'
print(re.search(r'[aeiou]+',cadena))