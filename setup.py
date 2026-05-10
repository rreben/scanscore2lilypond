# setup.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license

from setuptools import setup, find_packages
from pathlib import Path

# README laden, falls vorhanden
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
version_path = Path(__file__).parent / "scanscore2lilypond" / "VERSION"
version = version_path.read_text(encoding="utf-8").strip()

setup(
    name="scanscore2lilypond",
    version=version,
    packages=find_packages(include=["scanscore2lilypond", "scanscore2lilypond.*"]),
    description=(
        "Bereinigt LilyPond-Dateien, die aus ScanScore über MusicXML erzeugt wurden."
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Dr. Rupert Rebentisch",
    author_email="rupert.rebentisch@gmail.com",
    license="MIT",
    python_requires=">=3.7",
    install_requires=[
        "Click",
        "pyfiglet",
    ],
    include_package_data=True,
    package_data={
        # ordnet die VERSION-Datei dem Paket zu
        "scanscore2lilypond": ["VERSION"],
    },
    entry_points={
        "console_scripts": [
            # ruft die main()-Funktion in __main__.py auf
            "scanscore2lilypond = scanscore2lilypond.__main__:main",
        ],
    }
)
