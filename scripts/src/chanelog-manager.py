#!/usr/bin/env python3
"""
Changelog Manager CLI
Ubicación esperada: raiz/scripts/src/changelog-manager.py

Permite registrar cambios (Added, Changed, Deprecated, Removed, Fixed, Security)
en la sección [Unreleased] de CHANGELOG.md y promocionarlos a una nueva versión.
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

# Definición de categorías válidas según Keep a Changelog
CATEGORIES = {
    "added": "Added",
    "changed": "Changed",
    "deprecated": "Deprecated",
    "removed": "Removed",
    "fixed": "Fixed",
    "security": "Security",
}

DEFAULT_CHANGELOG_TEMPLATE = """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

"""


def find_changelog_path(script_path: Path) -> Path:
    """
    Busca CHANGELOG.md en la raíz del proyecto subiendo 2 niveles desde scripts/src.
    Si no existe, se ubica por defecto en la raíz.
    """
    project_root = script_path.resolve().parents[2]
    return project_root / "CHANGELOG.md"


def ensure_changelog_exists(changelog_path: Path) -> None:
    if not changelog_path.exists():
        changelog_path.write_text(DEFAULT_CHANGELOG_TEMPLATE, encoding="utf-8")
        print(f"[+] Creado nuevo archivo CHANGELOG en: {changelog_path}")


def add_entry(changelog_path: Path, category: str, message: str) -> None:
    ensure_changelog_exists(changelog_path)
    content = changelog_path.read_text(encoding="utf-8")

    category_title = CATEGORIES[category.lower()]
    entry_line = f"- {message.strip()}\n"

    # Verificar si existe la sección [Unreleased]
    if "## [Unreleased]" not in content:
        print("[!] No se encontró la sección '## [Unreleased]'. Creándola...")
        content = content.replace("# Changelog\n", "# Changelog\n\n## [Unreleased]\n")

    # Separar el contenido alrededor de [Unreleased]
    parts = content.split("## [Unreleased]", 1)
    header = parts[0] + "## [Unreleased]\n"
    rest = parts[1]

    # Encontrar la siguiente cabecera de versión (si existe)
    next_header_match = re.search(r"\n## \[", rest)
    if next_header_match:
        unreleased_block = rest[: next_header_match.start()]
        remaining_content = rest[next_header_match.start() :]
    else:
        unreleased_block = rest
        remaining_content = ""

    # Buscar la subcategoría dentro del bloque [Unreleased]
    category_pattern = rf"### {category_title}\n"
    if category_pattern in unreleased_block:
        # Insertar debajo del título de la subcategoría
        unreleased_block = unreleased_block.replace(
            f"### {category_title}\n", f"### {category_title}\n{entry_line}"
        )
    else:
        # Crear la subcategoría al final del bloque [Unreleased]
        unreleased_block = unreleased_block.rstrip() + f"\n\n### {category_title}\n{entry_line}\n"

    new_content = header + unreleased_block + remaining_content
    changelog_path.write_text(new_content, encoding="utf-8")
    print(f"[✓] Entrada agregada a '{category_title}': {message}")


def release_version(changelog_path: Path, version: str) -> None:
    ensure_changelog_exists(changelog_path)
    content = changelog_path.read_text(encoding="utf-8")

    if "## [Unreleased]" not in content:
        print("[!] No hay sección [Unreleased] para liberar.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    version_header = f"## [{version}] - {today}"

    # Reemplazar la cabecera [Unreleased] para incluir la nueva versión
    new_content = content.replace(
        "## [Unreleased]\n", f"## [Unreleased]\n\n{version_header}\n"
    )

    changelog_path.write_text(new_content, encoding="utf-8")
    print(f"[🚀] Versión {version} liberada con fecha {today}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gestor CLI para CHANGELOG.md (Keep a Changelog)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcomando 'add'
    add_parser = subparsers.add_parser("add", help="Agregar una nueva entrada al Changelog")
    add_parser.add_argument(
        "category",
        choices=list(CATEGORIES.keys()),
        help="Categoría del cambio (added, changed, deprecated, removed, fixed, security)",
    )
    add_parser.add_argument("message", help="Descripción del cambio realizado")

    # Subcomando 'release'
    release_parser = subparsers.add_parser("release", help="Convertir [Unreleased] en una versión")
    release_parser.add_argument(
        "version", help="Número de versión a publicar (ejemplo: v1.0.0 o 1.0.0)"
    )

    args = parser.parse_args()
    script_path = Path(__file__).resolve()
    changelog_path = find_changelog_path(script_path)

    if args.command == "add":
        add_entry(changelog_path, args.category, args.message)
    elif args.command == "release":
        release_version(changelog_path, args.version)


if __name__ == "__main__":
    main()
