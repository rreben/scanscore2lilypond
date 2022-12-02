# scanscore2lilypond
Purges lilypond-file that have been created from scanscore via musicxml.

Scanscore is a commercial OMR (optical music recognition) program, that analyzes scanned sheet music and generates musicxml and midi files. It has a graphical editor to correct glitches that usually occur during the OMR Process.

The musicxml file can be transformed to lilypond (a sophisticated text based music engraver software). However the lilypond file is cluttered with all types of layout instructions, that are not helpfull for further work with the lilypond file.

This is where scanscore2lilypond comes in handy: It purges the resulting lilypond file.

