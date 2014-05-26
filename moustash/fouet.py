#!/usr/bin/env python
# -*- coding: utf-8 -*-
#fouet.py for Fouet in /home/loic/GitHub/Moustash/moustash
#
#Made by Loïc Tosser, Findspire.com
#Login   <loic@wowi.io>
#
#

"""Fouet.

Usage:
  fouet <file>
  fouet (-h | --help)
  fouet --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import sys
from moustash import Moustash
from transporter import Franck


def fouet_supervisor(franck, headers, data2):
   data = dict([ x.split(':') for x in data2.split() ])
   moustash = Moustash(headers["eventname"], ["fouet"], "fouet", data["processname"], headers["pool"], True)
   franck.push_moustash(moustash.json_dump())
         
def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
#    arguments = docopt(__doc__, version='Fouet 0.1')
    franck = Franck("/tmp/fouet.ini")
    while 1:
        write_stdout('READY\n') # transition from ACKNOWLEDGED to READY
        line = sys.stdin.readline()  # read header line from stdin
        write_stderr(line) # print it out to stderr
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len'])) # read the event payload
        fouet_supervisor(franck, headers, data)
        write_stderr(data) # print the event payload to stderr
        write_stdout('RESULT 2\nOK') # transition from READY to ACKNOWLEDGED

if __name__ == '__main__':
    main()
