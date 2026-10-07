# Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo.
El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Añadido
- Scroll automático y manejo de caracteres `\n`, `\r`, `\t` en el driver VGA (`src/drivers/vga.c`).
- Documentación Doxygen completa en el driver de pantalla.
- Configuración de CI con GitHub Actions (`.github/workflows/ci.yml`).
- Archivos de gobernanza del repositorio (Code of Conduct, Contributing, Security, etc.).

## [0.1.0] - 2026-10-01

### Añadido
- Inicialización básica de pantalla VGA en modo texto (80x25) en dirección `0xB8000`.
- Estructura inicial del proyecto y archivos de cabecera (`include/drivers.h`).
