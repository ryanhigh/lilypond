/*
  This file is part of LilyPond, the GNU music typesetter.

  Copyright (C) 2005--2022 Han-Wen Nienhuys <hanwen@xs4all.nl>

  LilyPond is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  LilyPond is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with LilyPond.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "config.hh"

#include "pango-font.hh"

LY_DEFINE (ly_make_pango_description_string, "ly:make-pango-description-string",
           2, 0, 0, (SCM chain, SCM size),
           R"(
Make a @code{PangoFontDescription} string for the property alist @var{chain} at
size @var{size}.
           )")
{
  LY_ASSERT_TYPE (scm_is_number, size, 1);
  PangoFontDescription *pfd
    = properties_to_pango_description (chain, from_scm<double> (size));
  char *str = pango_font_description_to_string (pfd);

  SCM scm_str = scm_from_locale_string (str);
  g_free (str);
  pango_font_description_free (pfd);
  return scm_str;
}
