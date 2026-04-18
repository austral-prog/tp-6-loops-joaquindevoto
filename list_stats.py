# ---- Funciones provistas (NO modificar) ----

def find_min(numbers):
    """Dada una lista de numeros, retorna el menor valor."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    """Dada una lista de numeros, retorna el mayor valor."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# ---- Funciones a implementar ----

def range_of(numbers):
    """
    Retorna la diferencia entre el maximo y el minimo de la lista.
    Debe USAR las funciones find_min y find_max.

    Ejemplo: range_of([3, 1, 7, 2]) -> 6  (7 - 1)
    """
    maximo = find_max(numbers)
    minimo = find_min(numbers)

    return maximo - minimo


def average(numbers):
    """
    Retorna el promedio de los numeros en la lista, redondeado a 1 decimal.
    Si la lista esta vacia, retorna 0.0.
    Usar un bucle for para sumar los elementos.

    Ejemplo: average([10, 20, 30]) -> 20.0
    """
    if not numbers:
        return 0.0

    suma_total = 0
    for n in numbers:
        suma_total += n

    promedio = suma_total / len(numbers)
    return round(promedio, 1)


def describe(numbers):
    """
    Retorna un string con el formato:
    "Min:{min} Max:{max} Range:{range} Avg:{avg}"

    Debe USAR las funciones find_min, find_max, range_of y average.
    Si la lista esta vacia, retorna "Empty list".

    Ejemplo: describe([3, 1, 7, 2]) -> "Min:1 Max:7 Range:6 Avg:3.2"
    """
    if len(numbers) == 0:
        return "Empty list"



    mini = find_min(numbers)
    maxi = find_max(numbers)
    ran = range_of(numbers)
    avg = average(numbers)

    return f"Min:{mini} Max:{maxi} Range:{ran} Avg:{avg}"
