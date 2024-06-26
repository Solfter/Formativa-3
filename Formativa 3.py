import csv
import os
import time

trabajadores = []

def crear_planilla():
    with open('PlanillaTrabajadores', 'w',) as archivo:
        trabajador = 'Trabajador'.ljust(20)
        cargo = 'Cargo'.rjust(5)
        sueldo_bruto = 'Sueldo Bruto'.rjust(15)
        desc_salud = 'Desc. Salud'.rjust(25)
        desc_afp = 'Desc. AFP'.rjust(35)
        sueldo_liquido = 'Liquido a pagar'.rjust(45)
        archivo.write(f'{trabajador}{cargo}{sueldo_bruto}{desc_salud}{desc_afp}{sueldo_liquido}')

def limpiar_pantalla():
    os.system("cls")

def menu():
    print('Bienvenido a nuestra a aplicación'
      '\n1. Registrar trabajador'
      '\n2. Listar todos los trabajadores'
      '\n3. Imprimir planilla de sueldos'
      '\n4. Salir del programa')

    validar_op = True
    while validar_op:
        try:
            op = int(input('¿Que deseas? '))
            if op not in range(1,5):
                print('¡Error! Ingresa una opción válida')
            else:
                validar_op = False
        except ValueError:
            print('¡Error! Ingresa un número')
    return op

def registrar_trabajador():
    print('Seleccionaste agregar trabajador...\n')
    validar_ingreso = True
    while validar_ingreso:
        try:
            nombre = input('Ingrese el nombre del trabajador: ')
            if len(nombre) == 0:
                print('¡Error! Ingresa un nombre')
                continue
            cargo = input('Ingrese el cargo del trabajador: ')
            if len(cargo) == 0:
                print('¡Error! Ingresa un nombre de cargo')
                continue
            sueldo_bruto = int(input('Ingrese el sueldo bruto: '))
            if sueldo_bruto <= 0:
                print('¡Error! Ingresa un sueldo bruto mayor a 0')
                continue
            desc_salud = int(sueldo_bruto*0.07)
            desc_afp = int(sueldo_bruto*0.12)
            sueldo_liquido = int(sueldo_bruto*0.81)
            trabajador = [nombre, cargo, sueldo_bruto, desc_salud, desc_afp, sueldo_liquido]
            validar_ingreso = False
        except ValueError:
            print('¡Error! Ingresaste un caracter en sueldo bruto')
    with open('PlanillaTrabajadores', 'w',) as archivo:
        trabajador = 'Trabajador'.ljust(20)
        cargo = 'Cargo'.rjust(5)
        sueldo_bruto = 'Sueldo Bruto'.rjust(15)
        desc_salud = 'Desc. Salud'.rjust(25)
        desc_afp = 'Desc. AFP'.rjust(35)
        sueldo_liquido = 'Liquido a pagar'.rjust(45)
        archivo.write(f'{trabajador}{cargo}{sueldo_bruto}{desc_salud}{desc_afp}{sueldo_liquido}')

        


def listar_trabajadores():
    with open('PlanillaTrabajadores', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)


crear_planilla()
op = 0
while op != 4:
    op = menu()
    if op == 1:
        registrar_trabajador()
    elif op == 2:
        listar_trabajadores()
    elif op == 3:
        pass
    elif op == 4:
        print('Saliste del programa...')





        

