from calculos import planilla
from utilerias.menu import MENU, limpiar

while(True):
    print(MENU)
    op = int(input('Digite opcion: '))

    if op>=1 and op<=6:
        sueldo = float(input('Digite sueldo: $ '))
        match op: # a partir de Python 3.10
            case 1:
                print(f'El ISSS es: {planilla.isss(sueldo):.2f}')
            case 2:
                print(f'El AFP es: {planilla.afp(sueldo):.2f}')
            case 3:
                print(f'El Sueldo gravable es: {planilla.sueldo_gravable(sueldo):.2f}')
            # TODO: agregar opciones faltantes
        input()
        limpiar()
    else:
        break