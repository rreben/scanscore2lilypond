import pytest
from scanscore2lilypond import purgelily as pl


def test_replace_point_and_click():
    # Testdaten
    input_content = [
        r'\version "2.22.1"',
        r"% automatically converted by musicxml2ly"
        r" from /Users/rupertrebentisch/"
        r"scanscore2lilypond/scanscore2lilypond/tests/"
        r"test_files/Pleyel_Presto_I_step1.xml"
        r"scanscore2lilypond/tests/test_files/Pleyel_Presto_I_step1.xml",
        r"\pointAndClickOff",
        r"some other content",
    ]

    expected_output = [
        r'\version "2.22.1"',
        r"% automatically converted by musicxml2ly"
        r" from /Users/rupertrebentisch/"
        r"scanscore2lilypond/scanscore2lilypond/tests/"
        r"test_files/Pleyel_Presto_I_step1.xml"
        r"scanscore2lilypond/tests/test_files/Pleyel_Presto_I_step1.xml",
        r"\pointAndClickOn",
        r"some other content",
    ]

    # Ausführen der Funktion
    result = pl.replace_point_and_click(input_content)

    # Assertion: Überprüfung, ob das Ergebnis wie erwartet ist
    assert (
        result == expected_output
    ), r"The \pointAndClickOff should be replaced with \pointAndClickOn"


def test_remove_global_staff_and_layout():
    # Test input: Content of a LilyPond file
    input_content = [
        r'\header {',
        r'    encodingsoftware =  "MusicXML Library v3"',
        r'    }',
        r'#(set-global-staff-size 17.142857142857146)',
        r'\paper {',
        r'    paper-width = 21.0\cm',
        r'    paper-height = 29.7\cm',
        r'    top-margin = 1.5\cm',
        r'    bottom-margin = 1.5\cm',
        r'    left-margin = 1.5\cm',
        r'    right-margin = 1.5\cm',
        r'    indent = 1.6153846153846154\cm',
        r'    }',
        r'\layout {',
        r'    \context { \Score',
        r'        autoBeaming = ##f',
        r'        }',
        r'    }',
        r'PartPOneVoiceOne =  \relative a\' {',
        r'    \repeat volta 2 {',
        r'        \clef "alto" \time 1/8 \key f \major  |',
        r'        \tempo "" 4=120 a8 ^. _\f |',
        r'    }',
        r'}',
    ]

    # Expected output after removing global staff size,
    # paper, and layout blocks
    expected_output = [
        r'\header {',
        r'    encodingsoftware =  "MusicXML Library v3"',
        r'    }',
        r'PartPOneVoiceOne =  \relative a\' {',
        r'    \repeat volta 2 {',
        r'        \clef "alto" \time 1/8 \key f \major  |',
        r'        \tempo "" 4=120 a8 ^. _\f |',
        r'    }',
        r'}',
    ]

    # Call the function to test
    result = pl.remove_global_staff_and_layout(input_content)

    # Assert that the result matches the expected output
    assert result == expected_output


# Zum Ausführen des Tests
if __name__ == "__main__":
    pytest.main()
