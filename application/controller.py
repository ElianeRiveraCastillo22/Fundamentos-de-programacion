from interface.ui import (
    solicitar_datos_usuario,
    mostrar_paquetes,
    seleccionar_paquete,
    solicitar_datos_pago
)
from interface.notifications import mostrar_confirmacion_venta, mostrar_error
from infrastructure.payment_gateway import validar_pago, procesar_pago
from domain.entities import Transaccion
from domain.services import (
    verificar_transaccion,
    activar_paquete,
    actualizar_estado,
    generar_notificacion
)

def iniciar_proceso():
    usuario = solicitar_datos_usuario()
    paquetes = mostrar_paquetes()
    try:
        paquete = seleccionar_paquete(paquetes)
    except ValueError as e:
        mostrar_error(str(e))
        return

    datos_pago = solicitar_datos_pago()
    if not validar_pago(datos_pago):
        mostrar_error("Pago inválido. Verifique los datos.")
        return

    if not procesar_pago():
        mostrar_error("La pasarela de pago falló.")
        return

    transaccion = Transaccion(
        id=1,
        usuario=usuario,
        paquete=paquete,
        estado="confirmada"
    )
    mostrar_confirmacion_venta(transaccion.id)

    if verificar_transaccion(transaccion):
        activar_paquete(transaccion)
        actualizar_estado(transaccion)
        generar_notificacion(transaccion)
