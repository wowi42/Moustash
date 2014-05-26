#!/usr/bin/env python
# -*- coding: utf-8 -*-
#utils.py for Utils for Moustash in /home/loic/GitHub/Moustash/moustash
#
#Made by Loïc Tosser, Findspire.com
#Login   <loic@wowi.io>
#
#

def config_section_map(config, section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
