# scanscore2lilypond
Purges lilypond-file that have been created from scanscore via musicxml.

Scanscore is a commercial OMR (optical music recognition) program, that analyzes scanned sheet music and generates musicxml and midi files. It has a graphical editor to correct glitches that usually occur during the OMR Process.

The musicxml file can be transformed to lilypond (a sophisticated text based music engraver software). However the lilypond file is cluttered with all types of layout instructions, that are not helpfull for further work with the lilypond file.

This is where scanscore2lilypond comes in handy: It purges the resulting lilypond file.

## How to use scanscore2lilypond

```scanscore2lilypond``` has to be installed as a python library (s. below). You can start the purge with.

We use to steps to improve the generation of a lilypond file from a scanscore musicsxml file:
1. We purge the musicsxml file with (we need the ```-x``` option here):
   ```sh
   scanscore2lilypong -x -o purged_musicsxmlfile.xml some_musicsxmlfile.xml
   ```
   We then use the ```musicxml2ly``` program of the lilypond package to create an improved version of the lilypond file.
   ```sh
   musicxml2ly purged_musicsxmlfile.xml
   ```
2. The resulting ```purged_musicsxmlfile.ly``` can be further improved with 
    ```sh
    scanscore2lilypond purged_musicsxmlfile.ly
    ```
    This time we do NOT use the ```-x``` option, as we are modifying the lilypond file directly.

The result of the purge process will be printed to stdout.

We get the help information with:

```sh
scanscore2lilypond --help
```

## How to install scanscore2lilypond

Right now scanscore2lilypond is still in alpha. So we have to install the file locally.

We clone the repo with.
```sh
git clone https://github.com/rreben/scanscore2lilypond
```


We navigate to the newly created directory of the repository. Then we setup a virtual environment with:

```sh
virtualenv --python python3.10 venv
source venv/bin/activate
```

Now we install the dependencies in this virtual environment.

```sh
pip install click
```

Now we can install the lib with:
```sh
pip install -e . 
```
The terminal must be completely closed (quit) once. After that, the terminal needs to be restarted and the virtual environment must be restarted with source venv/bin/activate. Only then is the Python library in the shell's path.

The following command can be used to view the metadata of the library:
```sh
pip show scanscore2lilypond
```

## How to use ScanScore

We use the "optimize for MuseScore" option when exporting a musicxml file.

