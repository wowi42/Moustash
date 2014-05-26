#!/usr/bin/env python
# -*- coding: utf-8 -*-
#cuir.py for Cuir in /home/loic/GitHub/Moustash/moustash
#
#Made by Loic Tosser, Findspire.com
#Login   <loic@wowi.io>
#
#

"""Cuir.

Usage:
  cuir <file>
  cuir (-h | --help)
  cuir --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
from moustash import Moustash
from transporter import Franck
import platform
import time
import socket

class Cuir:
   def __init__(self, config_file):
       self.franck = Franck(config_file)
       self.cuirs = []
       for cuir, vache in self.franck.moustash_config["Cuir"].iteritems():
          if cuir == "interval":
             self.interval = int(vache)
          else:
             cuero = {}
             split_line = vache.split(':')
             cuero["ip"] = split_line[0]
             cuero["port_int"] = int(split_line[1])
             cuero["port"] = split_line[1]
             cuero["message"] = split_line[2]
             cuero["tag"] = cuir
             cuero["status"] = 0
             self.cuirs.append(cuero)

   def port_prober(self):
      while 42:
         for cuir in self.cuirs:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((cuir["ip"],cuir["port_int"]))
            if result != 0:
               if cuir["status"] != result:
                  moustash = Moustash(cuir["message"], ["cuir", cuir["tag"]], "cuir", cuir["tag"], cuir["ip"]+ ":" + cuir["port"], True)
                  self.franck.push_moustash(moustash.json_dump())
               else:
                  moustash = Moustash(cuir["message"], ["cuir", cuir["tag"]], "cuir", cuir["tag"], cuir["ip"]+ ":" + cuir["port"], False)
                  self.franck.push_moustash(moustash.json_dump())
               cuir["status"] = result
            sock.close()
         time.sleep(self.interval)

def main():
   arguments = docopt(__doc__, version='Cuir 0.1')
   cuir = Cuir(arguments["<file>"])
   cuir.port_prober()

if __name__ == '__main__':
    main()
