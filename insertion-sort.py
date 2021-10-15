import time

# Algoritmo de insertion-sort
#
# Para las pruebas voy a usar arreglos generados aletoriamente.
# Usaré los arreglos generados y también los ordenaré de forma descendiente para evaluar el peor de los casos.
# Voy a evaluar con n pequeño, mediano y grande.

def insertionSort(array):

    for rightElement in range(1,len(array)):

        key = array[rightElement]

        leftElement = rightElement - 1

        while leftElement >= 0 and key < array[leftElement]:

            array[leftElement + 1] = array[leftElement]

            leftElement = leftElement - 1

        array[leftElement + 1] = key
    return array


def main():

    array = [5,2,4,6,1,3]

    start = time.time()
    insertionSort(array)
    end = time.time()
    for i in range(len(array)):

        print("% d" % array[i])

    print("El tiempo de ejecucion es : ", end - start)

if '__main__' == __name__:
    main()
