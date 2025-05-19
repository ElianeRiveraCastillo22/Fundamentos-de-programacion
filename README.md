# Sistema Automatizado de Compra de Paquetes de Roaming para Movistar

## 📄 Resumen

Movistar, proveedor líder de servicios de telecomunicaciones, enfrenta deficiencias operativas en la comercialización de paquetes de roaming que afectan negativamente la experiencia del usuario. Actualmente, los usuarios deben comunicarse por WhatsApp con un agente para realizar una compra, lo cual genera demoras, insatisfacción y pérdida de clientes. Este proyecto propone e implementa una solución automatizada dentro de la app Mi Movistar.

## 🔎 Propósito del Sistema

Diseñar un módulo automático dentro de la app Mi Movistar para:

* Visualizar paquetes de roaming disponibles
* Realizar la compra y activación inmediata del paquete
* Recibir alertas inteligentes sobre consumo de datos internacionales

## 📂 Organización del Proyecto

```
roaming_system/
│
├── data/
│   └── paquetes.py
│
├── domain/
│   ├── entities.py
│   └── services.py
│
├── infrastructure/
│   └── payment_gateway.py
│
├── interface/
│   ├── ui.py
│   └── notifications.py
│
├── application/
│   └── controller.py
│
└── main.py

```
## 📂 Descripción de Carpetas

### `data/`  
Contiene datos estáticos del sistema como la lista de paquetes de roaming disponibles.  
**No tiene lógica**, solo actúa como fuente de datos.

- `paquetes.py`: listado simulado de paquetes con precios y duración.

---

### `domain/`  
Contiene las **entidades principales y lógica del negocio puro**, independiente de tecnologías externas.

- `entities.py`: clases como `Paquete`, `Usuario`, etc.
- `services.py`: reglas como validaciones, cálculo de costos o disponibilidad.

✅ Esta capa es el **corazón del sistema** y no depende de ninguna otra.

---

### `infrastructure/`  
Conecta con servicios externos (por ejemplo, simulación de pasarela de pago).

- `payment_gateway.py`: gestiona el proceso de pago simulado.

📌 Esta capa puede cambiar sin afectar la lógica del negocio.

---

### `interface/`  
Maneja la entrada y salida del sistema, incluyendo la **interacción con el usuario** y **notificaciones**.

- `ui.py`: visualización y entrada del usuario por consola.
- `notifications.py`: sistema que alerta al usuario cuando se le está por acabar el roaming.

---

### `application/`  
Contiene los **casos de uso o lógica de aplicación**. Orquesta todo el sistema: ejecuta flujos completos de negocio.

- `controller.py`: decide qué debe pasar según el estado del sistema y entradas del usuario.

🔁 Llama a `domain`, `interface`, `data` e `infrastructure`.

---

### `main.py`  
Punto de entrada del sistema. Desde aquí se lanza la aplicación y se inicializa el flujo principal.

---
## 🚀 Flujo de Ejecución

1. El sistema inicia (`main.py`).
2. Se activa el `controller` de `application/`.
3. Se notifica al usuario si su roaming está por agotarse (`interface/notifications.py`).
4. Se muestran los paquetes disponibles (`data/paquetes.py`).
5. El usuario elige un paquete vía la UI (`interface/ui.py`).
6. Se valida y procesa la compra (`domain/services.py`, `infrastructure/payment_gateway.py`).
7. Se activa el paquete, finalizando el flujo.

---
## ⚒️ Detalle del Flujo del Sistema
1. El usuario recibe la notificación que su paquete de roming está por agotarse
2. El usuario ingresa sus datos
3. Visualiza los paquetes disponibles
4. Selecciona uno mediante su ID
5. Ingresa los datos de pago
6. Se valida el pago y se procesa la transacción
7. Se activa el paquete y se genera la notificación de confirmación
---
## 🏗️ Arquitectura y Buenas Prácticas

* **Arquitectura por Capas (Clean Architecture inspirada):** Separación en `interface`, `domain` e `infrastructure`.
* **Principio de Responsabilidad Única:** Cada archivo o módulo tiene una sola razón de cambio.
* **Tipado estático con `type hints`:** Mejora la mantenibilidad del código.
* **Manejo de errores con `try/except`:** Robustez ante inputs inválidos.
* **Modularidad y reutilización:** Fácil de extender para otros servicios en la app Mi Movistar.

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** Python
* **Control de versiones:** Git
* **Gestor de tareas y backlog:** Trello
* **Colaboración y almacenamiento:** Google Drive
* **IDE:** AWS 
---


## 📊 Impacto Esperado

| Métrica                      | Antes     | Después | Mejora Esperada |
| ---------------------------- | --------- | ------- | --------------- |
| Tiempo de compra             | 10–30 min | < 2 min | -90%            |
| Conversión tras intento      | 10%       | 45%     | +35 puntos      |
| Abandono por frustración     | 20%       | 5%      | -15 puntos      |
| Ahorro en atención operativa | 40%       | 20%     | -20% en costos  |

## 📒 Futuras Mejores

* Integración con base de datos real
* Identificación de usuario mediante login
* Historial de transacciones
* Panel de administración para gestionar paquetes y alertas

---
## 👥 Participantes

* Michelle Katherine Polo Varillas
* Marco Antonio Fernandez Herrera
* Yulissa Teran Cerquin
* Milagros Nieves Palma Saenz
* Eliane Juana Rivera Castillo


> *Este proyecto simula un entorno real de ingeniería de sistemas con propósito académico para demostrar competencias técnicas y metodológicas.*
