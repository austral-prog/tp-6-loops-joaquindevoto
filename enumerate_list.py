# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    resultado = []
    indice_consecutivo = 0

    for palabra in lst:
        if palabra != "":

            item = f"{indice_consecutivo}. {palabra}"
            resultado.append(item)
            indice_consecutivo += 1  #

    return resultado


def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    resultado = []
    indice_consecutivo = 0

    for palabra in lst:
        if palabra != "":
            palabra_al_reves = palabra[::-1]
            item = f"{indice_consecutivo}. {palabra_al_reves}"
            resultado.append(item)
            indice_consecutivo += 1

    return resultado


