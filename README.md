Eurovision Bingo
================

A generator for Bingo cards for Eurovision lyrics.

Some people say that all Eurovision songs are the same. That's probably not
quite true, but there is perhaps a hint of truth in the suggestion that some
themes tend to recur from year to year. Hence, I thought, Eurovision Bingo.

The slightly hacky code in this repo will analyse a directory full of lyrics,
normally those from the previous year of the competition, and work out the
frequency of occurrence of each word. It will then generate Bingo cards, with
sets of words of different levels of commonness.

The middle square, sometimes marked FREE in some versions of Bingo, is marked
LOVE in Eurovision Bingo - i.e. basically the same thing. :-)

Code Requirements
-----------------

I have added a pre-generated set of cards to the repo so if you want to play,
you can just print those. If you want to generate your own, you will need at
least:

* Python
* LibreOffice
* Appy Pod (Python Open Document) library
  http://www.appyframework.org/pod.html

Edit the constants at the top of the source to change the year of lyrics used,
or the number of cards to generate. If you generate lots, though, you'll get
repeated words. You may or may not care about this.

Edit cards.odt in LibreOffice, being careful to preserve the special comments,
in other to make the cards look smarter than they currently do, or add your
own explanatory text at the top.

This software was developed on Linux; I have no idea whether it'll work on any
other operating system. I see no reason it shouldn't, although it does use
Unix directory separators.

Pull requests are welcome. :-)

Copyright: CC0 for all my contributions. The copyrights in the lyrics, of
course, rest with the original authors. (Actually no they don't, given the
way the music industry works, but the point is, I don't own them.)

How To Play
-----------

* Generate yourself a set of cards, or print out the ones in the repo.
* Turn on Eurovision, and turn on English subtitles
* Tick off words as they are sung; ask your fellow players in case of doubt
* The word has to be exact - "loving" is not the same as "love"
* The first person to complete a line of 5 (horizontal, vertical or diagonal)
  wins!

Prizes are left as an exercise for the reader.

Have fun!

Gerv
First Sunday Before Eurovision, 59 AE (2015 AD)
