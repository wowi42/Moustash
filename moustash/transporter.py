#!/usr/bin/env python
# -*- coding: utf-8 -*-
#config.py for Config File in /home/loic/GitHub/Moustash/moustash
#
#Made by Loic Tosser, Findspire.com
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
            redis_namespace = "moustash"
            if "redis_namespace" in self.moustash_config["Moustash"]:
                redis_namespace = self.moustash_config["Moustash"]["redis_namespace"]
            self.broker_namespace = redis_namespace
        else:
            print("Not yet implemented : %s !" % moustash_config["Moustash"]["transport"])
    
    def connect_to_redis(self):
        redis_ip = "127.0.0.1"
        redis_port = "6379"
        redis_db = "0"
        if "redis_ip" in self.moustash_config["Moustash"]:
            redis_ip = self.moustash_config["Moustash"]["redis_ip"]
        if "redis_port" in self.moustash_config["Moustash"]:
            redis_port = self.moustash_config["Moustash"]["redis_port"]
        if "redis_db" in self.moustash_config["Moustash"]:
            redis_db = self.moustash_config["Moustash"]["redis_db"]
        r = redis.StrictRedis(host=redis_ip, port=int(redis_port), db=int(redis_db))
        return r

    def push_moustash(self, json_message):
        if self.moustash_config["Moustash"]["transport"] == "redis":
            self.broker.rpush(self.broker_namespace, json_message)

