from domain.entities import Transaccion

def verificar_transaccion(transaccion: Transaccion) -> bool:
    return transaccion.estado == "confirmada"

def activar_paquete(transaccion: Transaccion):
    print(f"[SISTEMA] Activando paquete '{transaccion.paquete.nombre}' para el usuario {transaccion.usuario.nombre}...")

def actualizar_estado(transaccion: Transaccion):
    transaccion.estado = "activado"

def generar_notificacion(transaccion: Transaccion):
    print(f"[NOTIFICACIÓN] Paquete '{transaccion.paquete.nombre}' activado para {transaccion.usuario.nombre}. ¡Buen viaje!")
