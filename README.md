# scanscore2lilypond
Purges lilypond-file that have been created from scanscore via musicxml.

Scanscore is a commercial OMR (optical music recognition) program, that analyzes scanned sheet music and generates musicxml and midi files. It has a graphical editor to correct glitches that usually occur during the OMR Process.

The musicxml file can be transformed to lilypond (a sophisticated text based music engraver software). However the lilypond file is cluttered with all types of layout instructions, that are not helpfull for further work with the lilypond file.

This is where scanscore2lilypond comes in handy: It purges the resulting lilypond file.

## How to use scanscore2lilypond

```scanscore2lilypond``` has to be installed as a python library (s. below). You can start the purge with.

```sh
scanscore2lilypond somelilypondfile.ly
```

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


## How to use ScanScore

We use the "optimize for MuseScore" option when exporting a musicxml file.

