from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    correo: str

@dataclass
class Paquete:
    id: int
    nombre: str
    precio: float
    descripcion: str

@dataclass
class Transaccion:
    id: int
    usuario: Usuario
    paquete: Paquete
    estado: str
