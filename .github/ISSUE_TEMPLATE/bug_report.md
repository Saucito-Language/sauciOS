---
name: Reporte de Error (Bug)
about: Crea un informe para ayudarnos a corregir un fallo en el kernel o drivers
title: '[BUG] '
labels: bug
assignees: ''
---

**Descripción del error**
Una descripción clara y concisa de lo que sucede.

**Entorno de Ejecución**
- **Emulador / Hardware:** [ej. QEMU 8.0, Bochs, Hardware Real]
- **Arquitectura destino:** [ej. x86_32, x86_64]
- **Compilador:** [ej. GCC 13.2.0 -m32, NASM 2.16]

**Pasos para reproducir**
1. Compilar con `make ...`
2. Ejecutar en QEMU con `qemu-system-i386 ...`
3. Ver el fallo en la pantalla/consola.

**Comportamiento esperado**
Descripción clara de lo que se esperaba que sucediera.

**Registros / Logs (si aplica)**
Si dispones de la salida de registros de QEMU (`info registers`) o mensajes del compilador, pégalos aquí.
