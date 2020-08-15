import re
cadena = "Gerson Salas"
formato = re.compile(r"(?P<nombre>\w+) (?P<apellido>\w+)")
s=formato.search(cadena)
print(s.group('nombre'))
print(s.group('apellido'))