%% DO NOT EDIT this file manually; it was automatically
%% generated from the LilyPond Snippet Repository
%% (http://lsr.di.unimi.it).
%%
%% Make any changes in the LSR itself, or in
%% `Documentation/snippets/new/`, then run
%% `scripts/auxiliar/makelsr.pl`.
%%
%% This file is in the public domain.

\version "2.23.13"

\header {
  lsrtags = "editorial-annotations"

  texidoc = "
Choose different font sizes for instrumentName and shortInstrumentName
as a context override.
"

  doctitle = "Different font size settings for instrumentName and shortInstrumentName"
} % begin verbatim


InstrumentNameFontSize =
#(define-music-function (font-size-pair)(pair?)
"Sets the @code{font-size} of @code{InstrumentName}.
The font-size for the initial @code{instrumentName} is taken from the first
value in @var{font-size-pair}.  @code{shortInstrumentName} will get the second
value of @var{font-size-pair}.
"

;; This code could be changed/extended to set different values for each
;; occurance of `shortInstrumentName'

#{
  \override InstrumentName.after-line-breaking =
    #(lambda (grob)
       (let* ((orig (ly:grob-original grob))
              (siblings (if (ly:grob? orig)
                            (ly:spanner-broken-into orig)
                            '())))
         (if (pair? siblings)
             (begin
               (ly:grob-set-property!
                 (car siblings)
                 'font-size
                 (car font-size-pair))
               (for-each
                 (lambda (g)
                   (ly:grob-set-property! g 'font-size (cdr font-size-pair)))
                 (cdr siblings))))))
#})

\layout {
  \context {
    \Staff
    \InstrumentNameFontSize #'(6 . -3)
  }
}

\new StaffGroup <<
  \new Staff
     \with {
       instrumentName = "Flute"
       shortInstrumentName = "Fl."
     }
     { c''1 \break c'' \break c'' }
  \new Staff
   \with {
     instrumentName = "Violin"
     shortInstrumentName = "Vl."
   }
   { c''1 \break c'' \break c'' }
>>
