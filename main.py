#Garcia Ramos Saul Ezequiel
#Codigo: 215465492
#Analizador Lexico Completo
#Seminario de Solucion de problemas de Traductores 2
#Profesor: Michel Emanuel

import Analizador_Lexico as Analizador

fuente = []  # Lista Vacía de concatenacion
# Leer de un archivo las palabras y agregarlas a la lista
with open('programa.txt') as linea_de_entrada:
    for fila in linea_de_entrada:
        fuente.extend(fila.split())  # El split() remueve los saltos de linea y el extend() hace que no sean listas

fuente.append('$')

print('Resultado del Analisis Lexico\n')
print('Elemento\t\t\tCodigo')


for palabra in fuente:
    # Si la palabra coincide con los patrones, la imprime con su respectivo tipo. Si no coincide imprime None
    if palabra == '$':
        print(f'{palabra}\t\t\t23')

    elif Analizador.CmpElse.match(palabra):
        print(f'{palabra}\t\t\t22')

    elif Analizador.CmpReturn.match(palabra):
        print(f'{palabra}\t\t\t21')

    elif Analizador.CmpWhile.match(palabra):
        slista = Analizador.re.split(r'(\()', palabra)
        for sub_cadena in slista:
            if scadena == 'while':
                print(f'{scadena}\t\t\t20')
            elif scadena == '(':
                print(f'{scadena}\t\t\t14')
            else:
                print(f'{scadena}\t\t\t15')

    elif Analizador.CmpIf.match(palabra):
        slista = Analizador.re.split(r'(\()', palabra)
        for scadena in sub_lista:
            if scadena == 'if':
                print(f'{scadena}\t\t\t19')
            elif scadena == '(':
                print(f'{scadena}\t\t\t14')
            else:
                print(f'{scadena}\t\t\t15')

    elif Analizador.opAsignacion.match(palabra):
        slista = Analizador.re.split(r'(=)', palabra)
        for scadena in sub_lista:
            if scadena == '=':
                print(f'{scadena}\t\t\t18')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opDif.match(palabra):
        slista = Analizador.re.split(r'(!=)', palabra)
        for scadena in sub_lista:
            if scadena == '!=':
                print(f'{scadena}\t\t\t11')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opIgual.match(palabra):
        slista = Analizador.re.split(r'(==)', palabra)
        for scadena in sub_lista:
            if sub_cadena == '==':
                print(f'{scadena}\t\t\t11')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opNot.match(palabra):
        slista = Analizador.re.split(r'(!)', palabra)
        for scadena in sub_lista:
            if scadena == '!':
                print(f'{scadena}\t\t\t10')
            elif not scadena:
                continue
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opAnd.match(palabra):
        slista = Analizador.re.split(r'(&&)', palabra)
        for scadena in sub_lista:
            if scadena == '&&':
                print(f'{scadena}\t\t\t9')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opOr.match(palabra):
        slista = Analizador.re.split(r'(\|\|)', palabra)
        for scadena in slista:
            if scadena == '||':
                print(f'{scadena}\t\t\t8')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opMenorIgual.match(palabra):
        slista = Analizador.re.split(r'(<=)', palabra)
        for scadena in sub_lista:
            if scadena == '<=':
                print(f'{scadena}\t\t\t7')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opMayorIgual.match(palabra):
        slista = Analizador.re.split(r'(>=)', palabra)
        for scadena in sub_lista:
            if scadena == '>=':
                print(f'{scadena}\t\t\t7')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opMenor.match(palabra):
        slista = Analizador.re.split(r'(<)', palabra)
        for scadena in slista:
            if sub_cadena == '<':
                print(f'{scadena}\t\t\t7')
            elif sub_cadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opMayor.match(palabra):
        slista = Analizador.re.split(r'(>)', palabra)
        for scadena in slista:
            if sub_cadena == '>':
                print(f'{scadena}\t\t\t7')
            elif scadena.isnumeric():
                print(f'{scadena}\t\t\t1')
            else:
                print(f'{scadena}\t\t\t0')

    elif Analizador.opMultiplicacion.match(palabra):
        slista = Analizador.re.split(r'(\*)', palabra)
        for scadena in sub_lista:
            if scadena == '*':
                print(f'{scadena}\t\t\t6')
            else:
                print(f'{scadena}\t\t\t1')

    elif Analizador.opDivision.match(palabra):
        slista = Analizador.re.split(r'(/)', palabra)
        for scadena in sub_lista:
            if scadena == '/':
                print(f'{scadena}\t\t\t6')
            else:
                print(f'{scadena}\t\t\t1')

    elif Analizador.opSuma.match(palabra):
        sub_lista = Analizador.re.split(r'(\+)', palabra)
        for sub_cadena in sub_lista:
            if sub_cadena == '+':
                print(f'{sub_cadena}\t\t5')
            else:
                print(f'{sub_cadena}\t\t1')

    elif Analizador.opResta.match(palabra):
        slista = Analizador.re.split(r'(-)', palabra)
        for scadena in slista:
            if sub_cadena == '-':
                print(f'{scadena}\t\t\t5')
            else:
                print(f'{scadena}\t\t\t1')

    elif Analizador.opEntero.match(palabra):
        print(f'{palabra}\t\t\t4')

    elif Analizador.ID_Float.match(palabra):
        print(f'{palabra}\t\t\t4')

    elif Analizador.ID_Void.match(palabra):
        print(f'{palabra}\t\t\t4')

    elif Analizador.ID_Float.match(palabra):
        print(f'{palabra}\t\t\t2')

    elif Analizador.ID_int.match(palabra):
        print(f'{palabra}\t\t\t1')

    elif Analizador.ID.match(palabra):
        print(f'{palabra}\t\t\t0')

    else:
        print(f'{palabra}\t\t\tError')