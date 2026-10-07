# Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto de desarrollo de kernel/sistema operativo! Toda ayuda es bienvenida, desde la corrección de errores en drivers hasta la optimización de código en ensamblador o la mejora de la documentación.

---

## 1. Reglas Generales y Filosofía de Código

Para mantener la estabilidad del código bare-metal, por favor ten en cuenta los siguientes lineamientos:

* **Entorno Freestanding (`-ffreestanding`):** No asumas la existencia de la biblioteca estándar de C (`<stdio.h>`, `<stdlib.h>`, etc.). Toda función requerida debe ser implementada dentro del proyecto o pertenecer a librerías de soporte bajo nivel.
* **Acceso a Memoria Seguro:** Garantiza que las direcciones de memoria mapeada por hardware (MMIO) utilicen el calificador `volatile` cuando corresponda para evitar optimizaciones no deseadas del compilador.
* **Compatibilidad de Linkeo:** Asegúrate de declarar correctamente los símbolos globales cuando haya interacción entre C y Ensamblador NASM (respetando la convención de llamadas `cld`, manejo de registros, etc.).
* **Documentación:** Todo nuevo driver, estructura de datos o función pública debe incluir comentarios en formato **Doxygen**.

---

## 2. Flujo de Trabajo (Git Workflow)

1. **Haz un Fork** del repositorio.
2. **Crea una rama** para tu funcionalidad o corrección:
   ```bash
   git checkout -b feat/driver-teclado
   # o para corrección de bugs:
   git checkout -b fix/desbordamiento-vga
