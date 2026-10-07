# Política de Seguridad

## 1. Versiones Soportadas

Dado que este es un proyecto de desarrollo de bajo nivel / kernel, la seguridad se enfoca principalmente en la estabilidad del código, prevención de corrupción de memoria y aislamiento de ejecución.

| Versión | Soportada          |
| ------- | ------------------ |
| Main    | :white_check_mark: |
| < 1.0   | :x:                |

---

## 2. Reporte de Vulnerabilidades o Fallos Críticos

Nos tomamos muy en serio los problemas que puedan causar corrupción de memoria, ejecución no controlada, desbordamientos de búfer en memoria física o ciclos infinitos en el manejo de interrupciones.

Si descubres un problema grave de seguridad o un fallo crítico de estabilidad:

1. **NO abras una issue pública** en el repositorio.
2. Contacta directamente al equipo mantenedor a través de una de las siguientes vías:
   * **Borrador de Asesoría de Seguridad en GitHub:** A través de la pestaña *Security* -> *Advisories* -> *Report a vulnerability*.
   * **Correo electrónico:** *[Inserta aquí tu correo de contacto]*

---

## 3. Información a Incluir en el Reporte

Por favor incluye el máximo detalle posible para facilitar la reproducción del fallo:

* **Módulo/Driver afectado:** (ej. `src/drivers/vga.c`, manejador de interrupciones, etc.).
* **Descripción del problema:** (ej. desbordamiento de buffer, desalineación de pila, puntero nulo en espacio de kernel).
* **Pasos para reproducir:** Instrucciones precisas o secuencia de eventos que provocan el fallo en QEMU/Bochs.
* **Traza de registros o Pila (si está disponible):** Salida de registros de QEMU (`info registers`) o dump de memoria relevante.

---

## 4. Proceso de Respuesta

* **Confirmación:** Recibirás una respuesta inicial confirmando la recepción del reporte en un plazo máximo de **48 horas**.
* **Evaluación y Parche:** Se trabajará en una solución en una rama privada.
* **Publicación:** Una vez aplicado el parche en la rama principal, se le dará crédito al reportador (si así lo desea) en las notas de actualización.
