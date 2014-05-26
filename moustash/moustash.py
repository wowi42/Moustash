#!/usr/bin/env python
# -*- coding: utf-8 -*-
#moustash.py for Moustash in /home/loic/GitHub/Moustash/moustash
#
#Made by Loic Tosser, Wowi.io
#Login   <loic@wowi.io>
#
#

import platform
import time

class Moustash:
    def __init__(self):
        self.moustash = {}
        self.moustash["tags"] = []
        self.moustash["@timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.moustash["host"] = platform.node()
        self.moustash["message"] = ""
        self.moustash["type"] = ""
        self.moustash["program"] = ""
        self.moustash["source"] = ""
        self.moustash["notification"] = True