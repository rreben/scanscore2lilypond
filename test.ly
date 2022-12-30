\version "2.22.1"
% automatically converted by musicxml2ly from Pig_Ankle_Rag_purged.xml
\pointAndClickOff

\header {
    encodingsoftware =  "MusicXML Library v3"
    }

#(set-global-staff-size 17.142857142857146)
\paper {
    
    paper-width = 21.0\cm
    paper-height = 29.7\cm
    top-margin = 1.5\cm
    bottom-margin = 1.5\cm
    left-margin = 1.5\cm
    right-margin = 1.5\cm
    indent = 1.6153846153846154\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative a'' {
    \repeat volta 2 {
        \clef "treble" \time 1/4 \key d \major  |
        \tempo "" 4=120 a8 [ fis8 ] \numericTimeSignature\time 2/2
        \repeat volta 2 {
            g8 [ e8 cis8 a8 ] a8 <a' fis>4 |
            <g e>8 [ cis,8 a8 ~ ] a8 [ a8 ( b8 ) a8 ] |
            d8 [ a8 b8 a8 ] d8 [ a8 ( b8 a8 ) ] |
            d8 [ a8 b8 d8 ~ ] d8 a'4 fis8 |
             |
            g8 [ e8 cis8 a8 ~ ] a8 a'4 fis8 |
            g8 [ e8 cis8 a8 ~ ] a8 [ a8 ( b8 ) a8 ] |
            d8 [ a8 b8 a8 ] d8 [ a8 ( b8 a8 ) ] |
            d8 [ a8 b8 d8 ~ ] d8 [ b8 ] a4 |
             | 
            b2 d2 |
            fis8 a4 b8 ~ b8 [ a8 ( ] fis4 ) |
            e8 [ fis8 e8 a8 ~ ] a8 [ fis8 ] e4 }
        \alternative { {
                |
                d2. a'8 ( [ fis8 ) ] }
            {
                |
                d2. cis8 ( [ b8 ) ] }
            } |
         |
        R1 \bar "||"
        \repeat volta 2 {
            a8 [ b8 cis8 a8 ] b8 [ cis8 a8 b8 ] |
            cis8 [ a8 b8 cis8 ~ ] cis8 [ b8 ] a4 |
            a8 [ b8 d8 a8 ( ] b8 [ d8 ) a8 b8 ] |
            d8 [ a8 b8 d8 ~ ] d8 [ b8 ] a4  | 
            a8 [ b8 cis8 a8 ] b8 [ cis8 a8 b8 ] |
            cis8 [ a8 b8 cis8 ~ ] cis8 [ a8 ( b8 ) a8 ] |
            d8 [ a8 b8 a8 ] d8 [ a8 ( b8 a8 ) ] |
            d8 [ a8 b8 d8 ~ ] d8 [ b8 ] a4 |
             |
            b2 d2 |
            fis8 a4 b8 ~ b8 [ a8 ( ] fis4 ) |
            e8 [ fis8 e8 a8 ~ ] a8 [ fis8 ] e4 }
        \alternative { {
                |
                d2 ^. r4 cis8 ( [ b8 ) ] }
            } |
        \time 3/4  }
    \alternative { {
            |
            d2. fis,2. }
        } }

PartPOneVoiceOneChords =  \chordmode {
    \repeat volta 2 {
        \repeat volta 2 {
            |
            s8 \repeat volta 2 {
                a8:7 s8 s8 s8 s4 s8 |
                s8 s8 s8 s8 s8 s8 s8 s8 |
                d8:5 s8 s8 s8 s8 s8 s8 s8 |
                s8 s8 s8 s8 s8 s4 s8 |
                a8:7 s8 s8 s8 s8 s4 s8 |
                s8 s8 s8 s8 s8 s8 s8 s8 |
                d8:5 s8 s8 s8 s8 d8:5 s8 s8 |
                s8 s8 d8:5 s8 s8 s8 s4 |
                g2:5 s2 |
                d8:5 s4 s8 b8:5 s8 s4 |
                e8:5 s8 s8 s8 a8:5 s8 s4 }
            \alternative { {
                    |
                    s2. s8 }
                } s8 }
        \alternative { {
                |
                s2. s8 }
            } |
        s8 |
        a8:7 s8 s8 s8 s8 s8 s8 s8 |
        s8 s8 s8 s8 s8 s8 s4 |
        d8:5 s8 s8 s8 s8 s8 s8 s8 |
        s8 s8 s8 s8 s8 s8 s4 | 
        a8:7 s8 s8 s8 s8 s8 s8 s8 |
        s8 s8 s8 s8 s8 s8 s8 s8 |
        d8:5 s8 s8 s8 s8 s8 s8 s8 |
        s8 s8 s8 s8 s8 s8 s4 |
        g2:5 s2 |
        d8:5 s4 s8 b8:5 s8 s4 |
        e8:5 s8 s8 s8 a8:5 s8 s4 }
    \alternative { {
            |
            d2:5 s4 s8 }
        } s8 |
    d2.:5 \bar "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \context ChordNames = "PartPOneVoiceOneChords" { \PartPOneVoiceOneChords}
            \new Staff
            <<
                \set Staff.instrumentName = "Piano"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

