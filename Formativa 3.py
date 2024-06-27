import csv
import os
import time

trabajadores = {}

def crear_planilla():
    with open('PlanillaTrabajadores', 'w',) as archivo:
        formato_fila = f"{{:<{15}}}  {{:<{10}}}  {{:<{15}}}   {{:<{15}}}   {{:<{15}}}   {{:<{15}}}"
        archivo.write(formato_fila.format("Trabajador", "Cargo", "Sueldo Bruto", "Desc.Salud", "Desc. AFP", "Líquido a pagar") + '\n')
        archivo.write('-'*100)

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
            trabajador = input('Ingrese el nombre del trabajador: ')
            if len(trabajador) == 0:
                print('¡Error! Ingresa un nombre')
                continue
            cargo = input('Ingrese el cargo del trabajador: ').upper()
            if len(cargo) == 0:
                print('¡Error! Ingresa un nombre de cargo')
                continue
            if cargo not in ['CEO', 'DESARROLLADOR', 'ANALISTA DE DATOS']:
                print('Debes ingresar uno de los siguientes Cargos: CEO, Desarrollador, Analista de datos')
                continue
            sueldo_bruto = int(input('Ingrese el sueldo bruto: '))
            if sueldo_bruto <= 0:
                print('¡Error! Ingresa un sueldo bruto mayor a 0')
                continue
            desc_salud = int(sueldo_bruto*0.07)
            desc_afp = int(sueldo_bruto*0.12)
            sueldo_liquido = int(sueldo_bruto*0.81)
            datos_trabajador = {
                'Trabajador':trabajador, 
                'Cargo':cargo, 
                'Sueldo Bruto':sueldo_bruto, 
                'Desc. Salud':desc_salud, 
                'Desc. AFP':desc_afp, 
                'Líquido a pagar':sueldo_liquido
                }
            trabajadores.update(datos_trabajador)
            validar_ingreso = False
        except ValueError:
            print('¡Error! Ingresaste un caracter en sueldo bruto')
    with open('PlanillaTrabajadores', 'a',) as archivo:
        formato_fila = f"{{:<{15}}}  {{:<{10}}}  {{:<{15}}}   {{:<{15}}}   {{:<{15}}}   {{:<{15}}}"
        trabajador = datos_trabajador['Trabajador']
        cargo = datos_trabajador['Cargo']
        sueldo_bruto = datos_trabajador['Sueldo Bruto']
        desc_salud = datos_trabajador['Desc. Salud']
        desc_afp= datos_trabajador['Desc. AFP']
        sueldo_liquido= datos_trabajador['Líquido a pagar']
        archivo.write('\n')
        archivo.write(formato_fila.format(trabajador, cargo, sueldo_bruto,desc_salud,desc_afp,sueldo_liquido) + '\n')


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
        print(trabajadores)
    elif op == 4:
        print('Saliste del programa...')





        

