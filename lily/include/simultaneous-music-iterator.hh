/*
  This file is part of LilyPond, the GNU music typesetter.

  Copyright (C) 1997--2022 Han-Wen Nienhuys <hanwen@xs4all.nl>

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

#ifndef SIMULTANEOUS_MUSIC_ITERATOR_HH
#define SIMULTANEOUS_MUSIC_ITERATOR_HH

#include "music-iterator.hh"

#include "ly-smob-list.hh"

class Simultaneous_music_iterator : public Music_iterator
{
public:
  Simultaneous_music_iterator () = default;
  Simultaneous_music_iterator (Simultaneous_music_iterator const &);
  void derived_mark () const override;
  DECLARE_SCHEME_CALLBACK (constructor, ());
  OVERRIDE_CLASS_NAME (Simultaneous_music_iterator);

  Moment pending_moment () const override;
  void do_quit () override;
  bool run_always () const override;

  void preorder_walk (const std::function<void (Music_iterator *)> &) override;

protected:
  void create_children () override;
  void create_contexts () override;
  void process (Moment) override;

  const ly_smob_list<Music_iterator> &get_children () const
  {
    return children_list_;
  }

private:
  ly_smob_list<Music_iterator> children_list_;
};

#endif // SIMULTANEOUS_MUSIC_ITERATOR_HH
