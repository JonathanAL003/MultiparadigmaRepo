from Doctor import Doctor
from DoctorDAO import DoctorDAO
from Animal import Animal
from AnimalDAO import AnimalDAO
from Consulta import Consulta
from ConsultaDAO import ConsultaDAO
from logger_base import log
import datetime

if __name__ == "__main__":
    log.debug('Inicio de la aplicacion')
    print("Aplicación Con Conexión A Postgresql\nBienvenido, ingrese la opción que desea: ")
    nuevo = 1
    while nuevo == 1:
        while True:
            res = input('1.- Animales. 2.- Doctores. 3.- Consultas. 4.- Salir\nOpcion: ')
            if (res.isnumeric()):
                res = int(res)
                if (res < 5 and res > 0):
                    break
                else:
                    print("Favor de ingresar una opción válida.")
            else:
                print("Favor de ingresar solo un dígito del 1 al 4 para las opciones.")
        if res == 1:            
            print("Catalogo De Animales")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Animales Con Su Doctor 6.- Animal Especifico Con Su Doctor 7.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 8 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 7 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Animales - SELECT')
                animales = AnimalDAO.Seleccionar()
                for a in animales:
                    log.debug(a)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Animales - INSERT')
                    raza = input('Raza: ')
                    fecha_ingreso = input('Fecha De Ingreso (dd/mm/YYYY): ')
                    fecha_salida = input('Fecha De Salida (dd/mm/YYYY): ')
                    animal = Animal(raza=raza,fecha_ingreso=fecha_ingreso,fecha_salida=fecha_salida)
                    inserted = AnimalDAO.Insertar(animal)
                    log.debug(f"Animal Agregado {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Animales - UPDATE')
                    id = int(input('Id del animal a actualizar: '))
                    raza = input('Raza: ')
                    fecha_ingreso = input('Fecha De Ingreso (dd/mm/YYYY): ')
                    fecha_salida = input('Fecha De Salida (dd/mm/YYYY): ')
                    animal = Animal(id=id,raza=raza,fecha_ingreso=fecha_ingreso,fecha_salida=fecha_salida)
                    updated = AnimalDAO.Actualizar(animal)
                    log.debug(f"Animal Actualizado. {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Animales - DELETE')
                    id = int(input('Id del animal a eliminar: '))
                    animal = Animal(id=id)
                    deleted = AnimalDAO.Eliminar(animal)
                    log.debug(f"Animal Eliminado. {deleted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 5:
                try:
                    log.debug('Catalogo De Animales - Obtener a todos los animales ingresados con su doctor')
                    animales = AnimalDAO.ObtenerAnimalesConDoctor()
                    for a in animales:
                        log.debug(a)
                except Exception as ex:
                    log.error(ex)
            elif res2 == 6:
                try:
                    log.debug('Catalogo De Animales - Obtener un animal en específico ingresado con su doctor')
                    id = int(input("Ingrese el id del animal que se desea consultar: "))
                    animal = Animal(id=id)
                    animales = AnimalDAO.ObtenerAnimalEspecificoConDoctor(animal)
                    for a in animales:
                        log.debug(a)
                except Exception as ex:
                    log.error(ex)
            else:
                print("Saliendo del programa...")
                break

        elif res == 2:          
            print("Catalogo De Doctores")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Doctores Sin Cita 6.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 7 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 6 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Doctores - SELECT')
                doctores = DoctorDAO.Seleccionar()
                for d in doctores:
                    log.debug(d)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Doctores - INSERT')
                    nombre = input('Nombre: ')
                    telefono = input('Numero De Telefono: ')
                    doctor = Doctor(nombre=nombre, numero_telefono=telefono)
                    inserted = DoctorDAO.Insertar(doctor)
                    log.debug(f"Doctor Agregado {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Doctores - UPDATE')
                    id = int(input('Id del doctor a actualizar: '))
                    nombre = input('Nombre: ')
                    telefono = input('Numero De Telefono: ')
                    doctor = Doctor(nombre=nombre, numero_telefono=telefono, id=id)
                    updated = DoctorDAO.Actualizar(doctor)
                    log.debug(f"Doctor Actualizado {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Doctor - DELETE')
                    id = int(input('Id del doctor a eliminar: '))
                    doctor = Doctor(id=id)
                    deleted = DoctorDAO.Eliminar(doctor)
                    log.debug(f"Doctor Eliminado {deleted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 5:
                try:
                    log.debug('Catalogo De Doctores - Doctores Sin Cita')
                    doctor = DoctorDAO.ObtenerDoctorSinCitas()
                    for d in doctores:
                        log.debug(d)
                except Exception as ex:
                    log.error(ex)
            else:
                print("Saliendo del programa...")
                break
        elif res == 3:          
            print("Catalogo De Consultas")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Consulta Anterior 6.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 6 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 6 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Consultas - SELECT')
                consultas = ConsultaDAO.Seleccionar()
                for c in consultas:
                    log.debug(c)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Consultas - INSERT')
                    id_animal = int(input('Id Animal: '))
                    id_doctor = int(input('Id Doctor: '))
                    servicio = input('Servicio: ')
                    costo = float(input('Costo: '))
                    consulta = Consulta(id_animal=id_animal, id_doctor=id_doctor, servicio=servicio, costo=costo)
                    inserted = ConsultaDAO.Insertar(consulta)
                    log.debug(f"Consulta Agregada {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Consultas - UPDATE')
                    id_animal = int(input('Id Animal: '))
                    id_doctor = int(input('Id Doctor: '))
                    servicio = input('Servicio: ')
                    costo = float(input('Costo: '))
                    consulta = Consulta(id_animal=id_animal, id_doctor=id_doctor, servicio=servicio, costo=costo)
                    updated = ConsultaDAO.Actualizar(consulta)
                    log.debug(f"Consulta Actualizada {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Consultas - DELETE')
                    id_animal = int(input('Id del animal a eliminar: '))
                    id_doctor = int(input('Id del doctor a eliminar: '))
                    consulta = Consulta(id_animal=id_animal, id_doctor=id_doctor)
                    deleted = ConsultaDAO.Eliminar(consulta)
                    log.debug(f"Consulta Eliminado {deleted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 5:
                try:
                    log.debug('Catalogo De Consultas - Consulta Dia Anterior')
                    fecha = datetime.date.today()
                    dia = (fecha.day - 1)
                    consultas = ConsultaDAO.DiaAnterior(dia)
                    for c in consultas:
                        log.debug(c)
                except Exception as ex:
                    log.error(ex)
            else:
                print("Saliendo del programa...")
                break
        else:
            print("Saliendo del programa...")
            break
        while True:
            res3 = input('¿Volver al menu principal? (y/n): ').upper()
            if res3 == "Y":
                nuevo = 1
                log.debug('Nueva peticion')
                break
            elif res3 == "N":
                nuevo = 0
                log.debug('Fin del programa')
                break
            else:
                print("Eliga una opción válida.")