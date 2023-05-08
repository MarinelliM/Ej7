from Viajero_Frecuente import Viajero

import csv

def test():
    m = Viajero(4783, '43.242.2424', 'mauri', 'mama', 492283)
    print(m.getmillas())
    print('su nombre es {}' .format(m.getnombrecompleto()))
    m.acumularMillas(int(input('ingrese las millas a acumular:')))
    m.canjearMillas(int(input('Ingrese las millas a canjear:')))
    n = Viajero(4000, '43.839.127', 'hernesto', 'alvaerez', 30000)
    print(m > n)
    #suma = m + n
    #print('La suma de las millas del viajero mauri mas las del viajero hernesto dan un total de {}' .format(suma))
    suma2 = m + 100
    print('La suma de las millas del viajero mauri mas 100 es {}' .format(suma2))
    #resta = m - n
    #print('La resta de las millas del viajero mauri mas las del viajero hernesto dan un total de {}' .format(resta))
    resta2 = m-100
    print('La resta de las millas del viajero mauri menos 100 es de {}' .format(resta2))
    if m == 492283:
        print('True')
    else: print('False')
    if 492283 == m:
        print('True')
    else: print('False')
    suma3 = 100 + m
    print('La suma de las millas del viajero mauri mas 100 es {}' .format(suma3))
    resta3 = 100 - m
    print('La resta de las millas del viajero mauri menos 100 es {}' .format(resta3))




if __name__ == "__main__":
    test()
    viajeros = []
    with open('Viajeros_varios.csv', newline='') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        next(reader) #Saltea la primer fila con los encabezados
        for fila in reader:
            num_viajero, dni, nombre, apellido, millas_acumuladas = fila
            viajero = Viajero(int(num_viajero), dni, nombre, apellido, int(millas_acumuladas))
            viajeros.append(viajero)
        for viajero in viajeros:
            print("Numero de viajero: {}, DNI: {}, Nombre: {}, Apellido: {}, Millas acumuladas: {}".format(viajero.num_viajero, viajero.dni, viajero.nombre, viajero.apellido, viajero.getmillas()))
    num_vfrecuente = int(input('Ingrese un nnumero de viajero frecuente:'))
    viajero_actual = Viajero
    for viajero in viajeros:
        if viajero.getnumv() == num_vfrecuente:
            viajero_actual = viajero
            break
    
    if viajero_actual is None:
        print('El numero de viajero ingresado no es valido')
    else:
        while True:
            print('Menu')
            print('o - Salida')
            print('a - Consultar cantidad de millas')
            print('b - Acumular millas')
            print('c - Canjear millas')
            op = input('Ingrese opcion:')
            if op == 'a':
                print('Cantidad de millas acumuladas {}' .format(viajero_actual.getmillas()))
            elif op == 'b':
                millas = int(input('Ingrese cantidad de millas a acumular:'))
                viajero_actual.acumularMillas(millas)
            elif op == 'c':
                millas = int(input("Ingrese la cantidad de millas a canjear: "))
                viajero_actual.canjearMillas(millas)
            elif op == 'd':
                i = 0
                b = 0
                max = -1
                while i < len(viajeros):
                    if viajeros[i].getmillas() > max:
                        max=viajeros[i].getmillas()
                        i += 1
                while b < len(viajeros):
                    if viajeros[b].getmillas() == max:
                        print('Viajeros con mayor cantidad de millas:')
                        print("Numero de viajero: {}, DNI: {}, Nombre: {}, Apellido: {}, Millas acumuladas: {}".format(viajero.num_viajero, viajero.dni, viajero.nombre, viajero.apellido, viajero.getmillas()))
            elif op == 'o':
                print('Fin del programa')
            else:
                print("Opción inválida")
