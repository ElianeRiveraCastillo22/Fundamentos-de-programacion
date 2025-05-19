def validar_pago(datos_pago: dict) -> bool:
    return datos_pago.get("numero_tarjeta") and datos_pago.get("codigo_seguridad")

def procesar_pago() -> bool:
    print("[PAGO] Procesando pago con la pasarela simulada...")
    return True
