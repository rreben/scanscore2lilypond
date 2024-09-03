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


# Zum Ausführen des Tests
if __name__ == "__main__":
    pytest.main()
