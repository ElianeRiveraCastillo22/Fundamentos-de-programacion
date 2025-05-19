from data.paquetes import paquetes_disponibles
from domain.entities import Usuario, Paquete

def solicitar_datos_usuario() -> Usuario:
    print("\n--- Por favor ingrese sus datos ---")

    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    return Usuario(nombre, correo)

def mostrar_paquetes() -> list:
    print("\n--- Paquetes Disponibles ---")
    for paquete in paquetes_disponibles:
        print(f"{paquete['id']}. {paquete['nombre']} - S/.{paquete['precio']} ({paquete['descripcion']})")
    return paquetes_disponibles

def seleccionar_paquete(paquetes: list) -> Paquete:
    seleccion = int(input("Seleccione el ID del paquete deseado: "))
    for paquete in paquetes:
        if paquete["id"] == seleccion:
            return Paquete(**paquete)
    raise ValueError("ID de paquete no válido.")

def solicitar_datos_pago() -> dict:
    print("\n--- Información de Pago para la compra ---")
    numero_tarjeta = input("Número de tarjeta: ")
    codigo_seguridad = input("Código de seguridad: ")
    return {"numero_tarjeta": numero_tarjeta, "codigo_seguridad": codigo_seguridad}
