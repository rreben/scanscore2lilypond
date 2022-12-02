# setup.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license


from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='scanscore2lilypond',
    packages=find_packages(),
    description=(
        'Purges lilypond-file that have been created from scanscore via musicxml.'),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Dr. Rupert Rebentisch',
    author_email='rupert.rebentisch@gmail.com',
    install_requires=[
        'Click'
    ],
    include_package_data=True,
    package_data={'': ['scanscore2lilypond/VERSION']},
    entry_points={
        'console_scripts': [
            'scanscore2lilypond = scanscore2lilypond:ScanScore2LilyPond.run'
        ],
    }
)
