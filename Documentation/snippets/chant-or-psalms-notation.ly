%% DO NOT EDIT this file manually; it was automatically
%% generated from `Documentation/snippets/new/`.
%%
%% Make any changes in `Documentation/snippets/new/`,
%% then run `scripts/auxiliar/makelsr.pl --new`.
%%
%% This file is in the public domain.
%%
%% Note: this file works from version 2.23.13.

\version "2.23.13"

\header {
  lsrtags = "ancient-notation, contexts-and-engravers, rhythms, specific-notation, vocal-music"

  texidoc = "
This form of notation is used for Psalm chant, where verses aren't
always the same length.
"

  doctitle = "Chant or psalms notation"
} % begin verbatim


stemOff = \hide Staff.Stem
stemOn  = \undo \stemOff

\score {
  \new Staff \with { \remove "Time_signature_engraver" }
  {
    \key g \minor
    \cadenzaOn
    \stemOff a'\breve bes'4 g'4
    \stemOn a'2 \section
    \stemOff a'\breve g'4 a'4
    \stemOn f'2 \section
    \stemOff a'\breve^\markup { \italic flexe }
    \stemOn g'2 \fine
  }
}
