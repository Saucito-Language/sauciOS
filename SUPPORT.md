# Soporte del Proyecto

¡Gracias por utilizar este proyecto! Si necesitas ayuda para compilar el kernel, entender la arquitectura o reportar alguna duda sobre los drivers y el entorno bare-metal, aquí te mostramos los canales disponibles.

---

## 1. Preguntas y Discusiones

Para dudas generales sobre el código, arquitectura x86, configuración de compiladores cruzados (*cross-compilers*) o sugerencias sobre el diseño del sistema operativo:

* **GitHub Discussions:** Abre un hilo en la pestaña **Discussions** de este repositorio. Es el lugar idóneo para preguntas abiertas, ideas sobre nuevas características o consultas de arquitectura.

---

## 2. Reporte de Errores y Bugs

Si encuentras un comportamiento inesperado en la ejecución del kernel, fallos en la memoria de video VGA, desbordamientos de pila o errores de compilación con `gcc`/`nasm`:

1. Revisa la sección de **Issues** para verificar que el problema no haya sido reportado previamente.
2. Si es un error nuevo, abre un **New Issue** detallando:
   * El emulador o entorno de ejecución usado (ej. QEMU, Bochs, VirtualBox, hardware real).
   * La versión de la herramienta de compilación (`nasm -v`, `gcc --version`).
   * Pasos precisos para reproducir el fallo y trazas de salida/registros si están disponibles.

---

## 3. Problemas de Seguridad

Para reportar fallos críticos de seguridad o corrupción grave de memoria, **no utilices las issues públicas**. Revisa nuestra **[Política de Seguridad](SECURITY.md)** para conocer el procedimiento de reporte privado.

---

## 4. Recursos Recomendados (OSDev)

Si estás aprendiendo desarrollo de sistemas operativos desde cero, te recomendamos consultar los siguientes recursos de referencia utilizados en este proyecto:

* **[OSDev Wiki](https://wiki.osdev.org):** La enciclopedia de referencia para desarrollo de kernels bare-metal.
* **[Manuales para Desarrolladores de Arquitectura Intel 64 e IA-32](https://www.intel.com):** Especificaciones técnicas oficiales sobre el funcionamiento del procesador.
