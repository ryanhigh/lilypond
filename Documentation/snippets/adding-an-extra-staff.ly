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
  lsrtags = "contexts-and-engravers, really-simple, staff-notation"

  texidoc = "
An extra staff can be added (possibly temporarily) after the start of a
piece.
"

  doctitle = "Adding an extra staff"
} % begin verbatim


\score {
  <<
    \new Staff \relative c'' {
      c1 | c | c | c | c
    }
    \new StaffGroup \relative c'' {
      \new Staff {
        c1 | c
        <<
          {
            c1 | d
          }
          \new Staff {
            \once \omit Staff.TimeSignature
            c1 | b
          }
        >>
        c1
      }
    }
  >>
}
