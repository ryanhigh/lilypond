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
  lsrtags = "rhythms, tweaks-and-overrides"

  texidoc = "
By default, bar lines in StaffGroup, PianoStaff, or GrandStaff groups
are connected between the staves, i.e. a SpanBar is printed.  This
behaviour can be overridden on a staff-by-staff basis.
"

  doctitle = "Removing connecting bar lines on StaffGroup, PianoStaff, or GrandStaff"
} % begin verbatim


\relative c' {
  \new StaffGroup <<
    \new Staff {
      e1 | e
      \once \override Staff.BarLine.allow-span-bar = ##f
      e1 | e | e
    }
    \new Staff {
      c1 | c | c
      \once \override Staff.BarLine.allow-span-bar = ##f
      c1 | c
    }
    \new Staff {
      a1 | a | a | a | a
    }
  >>
}
