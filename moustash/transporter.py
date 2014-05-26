#!/usr/bin/env python
# -*- coding: utf-8 -*-
#config.py for Config File in /home/loic/GitHub/Moustash/moustash
#
#Made by Loïc Tosser, Findspire.com
#Login   <loic@wowi.io>
#
#

import ConfigParser
import redis
from utils import config_section_map

class Franck:
    def __init__(self, config_file):
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)
        self.moustash_config = {}
        self.moustash_config["Moustash"] = config_section_map(self.config, "Moustash")
        self.moustash_config["Cuir"] = config_section_map(self.config, "Cuir")
        if self.moustash_config["Moustash"]["transport"] == "redis":
            self.broker = self.connect_to_redis()
            self.broker_namespace = self.moustash_config["Moustash"]["redis_namespace"]
        else:
            print("Not yet implemented : %s !" % moustash_config["Moustash"]["transport"])
    
    def connect_to_redis(self):
        r = redis.StrictRedis(host=self.moustash_config["Moustash"]["redis_ip"], \
                              port=int(self.moustash_config["Moustash"]["redis_port"]), \
                              db=int(self.moustash_config["Moustash"]["redis_db"]))
        return r

    def push_moustash(self, json_message):
        if self.moustash_config["Moustash"]["transport"] == "redis":
            self.broker.rpush(self.broker_namespace, json_message)

