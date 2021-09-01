import re
# formulas patrón
ID = re.compile(r'[a-zA-Z]+[\w]*')
opAsignacion = re.compile(r'[a-zA-Z]+[\w]*=[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opEntero = re.compile(r'[\d]+')
opReal= re.compile(r'[\d]+\.[\d]+')
opSuma = re.compile(r'[\d]+[+][\d]+')
opResta = re.compile(r'[\d]+[-][\d]+')
opMultiplicacion = re.compile(r'[\d]+[*][\d]+')
opDivision = re.compile(r'[\d]+[/][\d]+')

opMenor = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*<[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opMayor = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*>[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opMenorIgual = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*<=[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opMayorIgual = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*>=[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opDif = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*!=[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opIgual = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*==[a-zA-Z]*[a-zA-Z0-9]*[\d]*')

opAnd = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*&&[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opOr = re.compile(r'[a-zA-Z]*[a-zA-Z0-9]*[\d]*\|\|[a-zA-Z]*[a-zA-Z0-9]*[\d]*')
opNot = re.compile(r'![a-zA-Z]*[a-zA-Z0-9]*[\d]*')

CmpIf = re.compile(r'if\([a-zA-Z]*[a-zA-Z0-9]*[\d]*<?>?[<=]?[>=]?[!=]?[=]?[a-zA-Z]*[a-zA-Z0-9]*[\d]*\)')
CmpElse = re.compile(r'else')
CmpWhile = re.compile(r'while\([a-zA-Z]*[a-zA-Z0-9]*[\d]*<?>?[<=]?[>=]?[!=]?[=]?[a-zA-Z]*[a-zA-Z0-9]*[\d]*\)')
CmpReturn = re.compile(r'return')

ID_int = re.compile(r'int')
ID_Float = re.compile(r'float')
ID_Void = re.compile(r'void')

# Pruebas de las expresiones regulares
if __name__ == '__main__':
    cadena_entrada = 'float pi'
    coincidir = FLOAT.match(cadena_prueba)
    if coincidir:
        print(coincidir.group())
    else:
        print('No hubo match')