import os
import string


def abrir_archivo(nombre):
    """ Abre el archivo previamente cargado en 'archivo_nombre'
    y retorna su contenido como una lista donde sus elementos están
    divididos por un salto de línea"""
    base_path = os.path.abspath(os.path.dirname(__file__))
    archivo = os.path.join(base_path, nombre + '.txt')
    with open(archivo, 'r', encoding="utf-8") as fp:
        contenido = fp.readlines()
    return contenido


def reconocer_datos(nombre):
    """ Recibe por parámetro el nombre del archivo a abrir para luego
    devolver su contenido como una lista que tiene en su índice -1 el tipo
    de dato que contiene."""
    excluidos = ['\n', ',', "'"]
    contenido = abrir_archivo(nombre)
    for i in range(len(contenido)):
        palabra = [char for char in contenido[i] if char not in excluidos]
        contenido[i] = ''.join(char for char in palabra)
    if contenido[0].isalpha():
        contenido = limpiar_nombres(contenido)
        contenido.append("nombres")
    else:
        contenido = limpiar_nums(contenido)
        contenido.append("números")
    return contenido


def limpiar_nums(lista):
    """ Recibe una lista de números en formato string y devuelve
    una lista de números."""
    for i in range(len(lista)):
        clear_word = "".join(filter(lambda x: x in string.digits,
                                    lista[i]))
        lista[i] = float(clear_word)
    return lista


def limpiar_nombres(lista):
    """ Recibe una lista de nombres y devuelve la lista solo con los valores
    permitidos."""
    valores = string.ascii_letters.join(["á", "é", "í", "ó", "ú"])
    for i in range(len(lista)):
        clear_word = "".join(filter(lambda x: x in valores,
                                    lista[i].lower())).capitalize()
        lista[i] = clear_word
    return list(filter(lambda x: x != '', lista))


def obtener_listas(nombre_archivo, textos):
    lista = reconocer_datos(nombre_archivo)
    tipo = lista.pop()
    textos[tipo].append(lista)
    if tipo == 'nombres':
        print(lista)
        print("tipo de archivo = strings")
    else:
        print(lista)
        print("tipo de archivo = dígitos")


def obtener_listados(*args):
    """ Lee por teclado nombres de archivos a cargar hasta que se ingresa
    'fin'. Retorna un diccionario con los tipos de texto (nombres, números)
    como keys y una lista de listas como value"""
    listados = {'nombres': [], 'números': []}
    if len(args) == 0:
        print("Comienzo carga de archivos (ingrese fin para terminar)")
        nombre_archivo = input('Nombre del archivo: ')
        while nombre_archivo != 'fin':
            obtener_listas(nombre_archivo, listados)
            nombre_archivo = input('Nombre del archivo: ')
    else:
        for i in range(3):
            obtener_listas(args[i], listados)
    print("-"*30)
    return listados


def sumar_notas(notas):
    """ Suma las notas con el mismo índice de distintas listas y los guarda en
    la lista de posición '0'"""
    total = []
    for j in range(len(notas) - 1):
        total = [notas[0][i] + notas[j + 1][i]
                 for i in range(len(notas[0]))]
    total.append(len(notas))
    return total


def promedio_indi(notas, div):
    return [nota / div for nota in notas]


def promedio_general(notas):
    return sum(notas) / len(notas) - 1


def informar_promedios(notas, nombres):
    """ Recibe como parámetro las notas a promediar y los nombres, ambos
    relativos en cuanto a posición """
    cant_notas = notas.pop()
    prom_g = promedio_general(notas)
    promedios = promedio_indi(notas, cant_notas)
    print(f"Nombre{' ' * 9}| Prom.")
    print("-" * 30)
    for i in range(len(notas)):
        if promedios[i] < prom_g:
            promedio = float(promedios[i]).__format__(".4")
            esp = 15 - len(nombres[i])
            print(f"{nombres[i]}{' ' * esp}| {promedio} ")


def elegir_op():
    """ Si se selecciona 'promedios' sin antes 'cargar' se usan los valores
    'nombres_1', 'eval' y 'eval2'."""
    print("""
    -~- Menu principal -~-\n
    1.  Cargar 
    2.  Promedios
    3.  Salir
    """)
    char = input('Opción (1-3): ')
    if char in string.digits:
        valor = int(char)
    else:
        valor = -1
    return valor


def main():
    fin = False
    pos = 0
    while not fin:
        choice = elegir_op()
        match choice:
            case 1:
                ls = obtener_listados()
                ls["números"] = sumar_notas(ls["números"])
                pos = 1
            case 2:
                if pos == 0:
                    ls = obtener_listados("nombres_1", "eval", "eval2")
                    ls["números"] = sumar_notas(ls["números"])
                informar_promedios(ls["números"], ls["nombres"][0])
            case 3:
                fin = True
            case _:
                print("Opción no válida")


if __name__ == '__main__':
    main()
