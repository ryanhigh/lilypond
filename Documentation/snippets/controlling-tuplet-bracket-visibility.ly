%% DO NOT EDIT this file manually; it was automatically
%% generated from `Documentation/snippets/new/`.
%%
%% Make any changes in `Documentation/snippets/new/`,
%% then run `scripts/auxiliar/makelsr.pl --new`.
%%
%% This file is in the public domain.
%%
%% Note: this file works from version 2.23.14.

\version "2.23.14"

\header {
  lsrtags = "rhythms, tweaks-and-overrides"

  texidoc = "
The default behavior of tuplet bracket visibility is to print a
bracket unless there is a beam of the same length as the tuplet.

To control the visibility of tuplet brackets, set the property
@code{'bracket-visibility} to either @code{#t} (always print a
bracket), @code{'if-no-beam} (only print a bracket if there is no
beam), or @code{#f} (never print a bracket).  The latter is in fact
equivalent to omitting the @code{TupletBracket} object altogether
from the printed output.
"

  doctitle = "Controlling tuplet bracket visibility"
} % begin verbatim


music = \relative c'' {
  \tuplet 3/2 { c16[ d e } f8]
  \tuplet 3/2 { c8 d e }
  \tuplet 3/2 { c4 d e }
}

\new Voice {
  \relative c' {
    \override Score.TextMark.non-musical = ##f
    \textMark "default" \music
    \override TupletBracket.bracket-visibility = #'if-no-beam
    \textMark \markup \typewriter "'if-no-beam" \music
    \override TupletBracket.bracket-visibility = ##t
    \textMark \markup \typewriter "#t" \music
    \override TupletBracket.bracket-visibility = ##f
    \textMark \markup \typewriter "#f" \music
    \omit TupletBracket
    \textMark \markup \typewriter "omit" \music
  }
}
