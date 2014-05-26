#!/usr/bin/env python
# -*- coding: utf-8 -*-
#panpan.py for PanPan in /home/loic/GitHub/Moustash/moustash
#
#Made by Loïc Tosser, Findspire.com
#Login   <loic@wowi.io>
#
#

"""Panpan.

Usage:
  panpan <file> <message> <program> <source> <notification>
  panpan (-h | --help)
  panpan --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
from moustash import Moustash
from transporter import Franck

def main():
   arguments = docopt(__doc__, version='Cuir 0.1')
   franck = Franck(arguments["<file>"])
   if arguments["<notification>"] == "True":
       moustash = Moustash(arguments["<message>"], ["panpan"], "panpan", arguments["<program>"], arguments["<source>"], True)
   else if arguments["<notification>"] == "False":
       moustash = Moustash(arguments["<message>"], ["panpan"], "panpan", arguments["<program>"], arguments["<source>"], True)
   else:
       print "arguments[\"<notification>\"] must be True or False !!!" 
   franck.push_moustash(moustash.json_dump())

if __name__ == '__main__':
    main()
