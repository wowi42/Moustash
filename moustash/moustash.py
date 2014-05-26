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
    def __init__(self, message, tags, type_stash, program, source, notification):
        self.moustash = {}
        self.moustash["tags"] = []
        self.moustash["tags"].append(tags)
        self.moustash["@timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.moustash["host"] = platform.node()
        self.moustash["message"] = message
        self.moustash["type"] = type_stash
        self.moustash["program"] = program
        self.moustash["source"] = source
        self.moustash["notification"] = notification
