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
  lsrtags = "really-simple, rhythms"

  texidoc = "
Tuplet brackets can be made to run to prefatory matter or the next
note. Default tuplet brackets end at the right edge of the final note
of the tuplet; full-length tuplet brackets extend farther to the right,
either to cover all the non-rhythmic notation up to the following note,
or to cover only the whitespace before the next item of notation, be
that a clef, time signature, key signature, or another note.  The
example shows how to switch tuplets to full length mode and how to
modify what material they cover.
"

  doctitle = "Modifying tuplet bracket length"
} % begin verbatim


\new RhythmicStaff {
  % Set tuplets to be extendable...
  \set tupletFullLength = ##t
  % ...to cover all items up to the next note
  \set tupletFullLengthNote = ##t
  \time 2/4
  \tuplet 3/2 { c4 4 4 }
  % ...or to cover just whitespace
  \set tupletFullLengthNote = ##f
  \time 4/4
  \tuplet 5/4 { 4 1 }
  \time 3/4
  2.
}
