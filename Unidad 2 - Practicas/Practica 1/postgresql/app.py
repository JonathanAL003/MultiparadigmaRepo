from Juego import Juego
from Producto import Producto
from Proveedor import Proveedor
from JuegoDAO import JuegoDAO
from ProductoDAO import ProductoDAO
from ProveedorDAO import ProveedorDAO
from logger_base import log

if __name__ == "__main__":
    log.debug('Inicio de la aplicación')
    print("Aplicación Con Conexión A Postgresql\nBienvenido, ingrese la opción que desea: ")
    nuevo = 1
    while nuevo == 1:
        while True:
            res = input('1.- Catalogo De Juegos. 2.- Catalogo De Productos. 3.- Catalogo De Proveedores. 4.- Salir\nOpcion: ')
            if (res.isnumeric()):
                res = int(res)
                if (res < 5 and res > 0):
                    break
                else:
                    print("Favor de ingresar una opción válida.")
            else:
                print("Favor de ingresar solo un dígito del 1 al 4 para las opciones.")
        if res == 1:            #Juegos
            print("Catalogo De Juegos")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 6 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 5 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Juegos - SELECT')
                juegos = JuegoDAO.Seleccionar()
                for j in juegos:
                    log.debug(j)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Juegos - INSERT')
                    nombre = input('Nombre: ')
                    desarrollador = input('Desarrollador: ')
                    anio_publicacion = int(input('Año De Publicación: '))
                    juego = Juego(nombre=nombre, desarrollador=desarrollador, anio_publicacion=anio_publicacion)
                    inserted = JuegoDAO.Insertar(juego)
                    log.debug(f"Juego Agregado {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Juegos - UPDATE')
                    id = int(input('Id del juego a actualizar: '))
                    nombre = input('Nombre: ')
                    desarrollador = input('Desarrollador: ')
                    anio_publicacion = int(input('Año De Publicación: '))
                    juego = Juego(id_juego=id, nombre=nombre, desarrollador=desarrollador, anio_publicacion=anio_publicacion)
                    updated = JuegoDAO.Actualizar(juego)
                    log.debug(f"Juego Actualizado {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Juegos - DELETE')
                    id = int(input('Id del juego a eliminar: '))
                    juego = Juego(id_juego=id)
                    deleted = JuegoDAO.Eliminar(juego)
                    log.debug(f"Juego Eliminado {deleted}")
                except Exception as ex:
                    log.error(ex)
            else:
                print("Saliendo del programa...")
                break

        elif res == 2:          #Productos
            print("Catalogo De Productos")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 6 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 5 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Productos - SELECT')
                productos = ProductoDAO.Seleccionar()
                for p in productos:
                    log.debug(p)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Productos - INSERT')
                    nombre = input('Nombre: ')
                    descripcion = input('Descripción: ')
                    precio = float(input('Precio: '))
                    stock = int(input('Stock: '))
                    producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
                    inserted = ProductoDAO.Insertar(producto)
                    log.debug(f"Producto Agregado {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Producto - UPDATE')
                    id = int(input('Id del producto a actualizar: '))
                    nombre = input('Nombre: ')
                    descripcion = input('Descripción: ')
                    precio = float(input('Precio: '))
                    stock = int(input('Stock: '))
                    producto = Producto(id_producto=id, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
                    updated = ProductoDAO.Actualizar(producto)
                    log.debug(f"Producto Actualizado {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Productos - DELETE')
                    id = int(input('Id del producto a eliminar: '))
                    producto = Producto(id_producto=id)
                    deleted = ProductoDAO.Eliminar(producto)
                    log.debug(f"Producto Eliminado {deleted}")
                except Exception as ex:
                    log.error(ex)
            else:
                print("Saliendo del programa...")
                break
        elif res == 3:          #Proveedores
            print("Catalogo De Proveedores")
            while True:
                res2 = input('1.- Consultar. 2.- Agregar. 3.- Editar. 4.- Eliminar. 5.- Salir\nOpcion: ')
                if (res2.isnumeric()):
                    res2 = int(res2)
                    if (res2 < 6 and res2 > 0):
                        break
                    else:
                        print("Favor de ingresar una opción válida.")
                else:
                    print("Favor de ingresar solo un dígito del 1 al 5 para las opciones.")
            if res2 == 1:
                log.debug('Catalogo De Proveedores - SELECT')
                proveedores = ProveedorDAO.Seleccionar()
                for p in proveedores:
                    log.debug(p)
            elif res2 == 2:
                try:
                    log.debug('Catalogo De Proveedores - INSERT')
                    nombre = input('Nombre: ')
                    rfc = input('RFC: ')
                    curp = input('CURP: ')
                    anio_fundacion = int(input('Año De Fundación: '))
                    proveedor = Proveedor(nombre=nombre, rfc=rfc, curp=curp, anio_fundacion=anio_fundacion)
                    inserted = ProveedorDAO.Insertar(proveedor)
                    log.debug(f"Proveedor Agregado {inserted}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 3:
                try:
                    log.debug('Catalogo De Provedores - UPDATE')
                    id = int(input('Id del proveedor a actualizar: '))
                    nombre = input('Nombre: ')
                    rfc = input('RFC: ')
                    curp = input('CURP: ')
                    anio_fundacion = int(input('Año De Fundación: '))
                    proveedor = Proveedor(id_proveedor=id ,nombre=nombre, rfc=rfc, curp=curp, anio_fundacion=anio_fundacion)
                    updated = ProveedorDAO.Actualizar(proveedor)
                    log.debug(f"Proveedor Actualizado {updated}")
                except Exception as ex:
                    log.error(ex)
            elif res2 == 4:
                try:
                    log.debug('Catalogo De Proveedores - DELETE')
                    id = int(input('Id del proveedor a eliminar: '))
                    proveedor = Proveedor(id_proveedor=id)
                    deleted = ProveedorDAO.Eliminar(proveedor)
                    log.debug(f"Proveedor Eliminado {deleted}")
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