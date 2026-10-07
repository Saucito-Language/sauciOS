cmake_minimum_required(VERSION 3.20)

# ------------------------------------------------------------------------------
# Configuración del Proyecto
# ------------------------------------------------------------------------------
project(
    MyProject
    VERSION 0.1.0
    DESCRIPTION "Proyecto C++20 con scripts de soporte en Python"
    LANGUAGES CXX C
)

# Exportar compile_commands.json para autocompletado en Neovim (clangd) / VS Code
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ------------------------------------------------------------------------------
# Estándar y Opciones de Compilación C++
# ------------------------------------------------------------------------------
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Opciones de salida para binarios y librerías
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# ------------------------------------------------------------------------------
# Flags de Compilación según el Compilador
# ------------------------------------------------------------------------------
if(MSVC)
    add_compile_options(/W4 /permissive- /utf-8)
else()
    add_compile_options(-Wall -Wextra -Wpedantic -Wconversion)
endif()

# ------------------------------------------------------------------------------
# Búsqueda de Python (Para integrar con changelog-manager.py u otros scripts)
# ------------------------------------------------------------------------------
find_package(Python3 COMPONENTS Interpreter REQUIRED)

# Target personalizado para ejecutar el changelog manager mediante CMake/Ninja
add_custom_target(
    changelog_add
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/src/changelog-manager.py add ${CATEGORY} "${MSG}"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Agregando entrada al CHANGELOG.md..."
    USES_TERMINAL
)

# ------------------------------------------------------------------------------
# Target Principal (Ejecutable)
# ------------------------------------------------------------------------------
# Busca código fuente en src/
file(GLOB_RECURSE PROJECT_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

if(PROJECT_SOURCES)
    add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})

    target_include_directories(${PROJECT_NAME}
        PUBLIC
            $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
            $<INSTALL_INTERFACE:include>
    )
else()
    message(STATUS "No se encontraron archivos fuente en src/. Crea un main.cpp para compilar.")
endif()

# ------------------------------------------------------------------------------
# Ejemplo de pruebas unitarias (Opcional)
# ------------------------------------------------------------------------------
option(BUILD_TESTS "Habilitar la compilación de pruebas unitarias" OFF)

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()
