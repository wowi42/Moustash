#!/usr/bin/env python
# -*- coding: utf-8 -*-
#config.py for Config File in /home/loic/GitHub/Moustash/moustash
#
#Made by Loic Tosser, Wowi.io
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
        self.broker = {}
        if self.moustash_config["Moustash"]["transport"] == "redis":
            redis_parameters = {"redis_host" : "localhost", "redis_port" : "6379", "redis_db" : "0", "redis_namespace": "logstash:moustash"}
            self.fill_broker_options(redis_parameters)
            self.broker_connection = self.connect_to_redis()
        else if self.moustash_config["Moustash"]["transport"] == "rabbitmq":
            rabbitmq_parameters = {"rabbitmq_host" : "localhost", "rabbitmq_port": "5672",
                                   "rabbitmq_ssl" : "0", "rabbitmq_ssl_key" = None, 
                                   "rabbitmq_ssl_cert" = None, "rabbitmq_ssl_cacert" = None,
                                   "rabbitmq_vhost" = "/", "rabbitmq_username" = "guest",
                                   "rabbitmq_password" = "guest",
                                   "rabbitmq_queue" = "logstash-queue", "rabbitmq_queue_durable" = "0",
                                   "rabbitmq_exchange_type" = "direct", "rabbitmq_exchange_durable" = "0",
                                   "rabbitmq_key" = "logstash-key", "rabbitmq_exchange" = "logstash-exchange"}
            self.fill_broker_options(rabbitmq_parameters)
            self.broker_connection = self.connect_to_rabbitmq()
        else:
            print("Not yet implemented : %s !" % moustash_config["Moustash"]["transport"])
            

    def fill_broker_options(self, options):
        for option_name, option_value in options.iteritems():
            if option_name in self.moustash_config["Moustash"]:
                self.broker[option_name] = self.moustash_config["Moustash"][option_name]
            else:
                self.broker[option_name] = option_value

    def connect_to_redis(self):
        r = redis.StrictRedis(host=self.broker["redis_ip"], port=int(self.broker["redis_port"]), db=int(self.broker["redis_db"]))
        return r

    def connect_to_rabbitmq(self):
        r = redis.StrictRedis(host=self.broker["redis_ip"], port=int(self.broker["redis_port"]), db=int(self.broker["redis_db"]))
        return r

    def push_moustash(self, json_message):
        if self.moustash_config["Moustash"]["transport"] == "redis":
            self.broker.rpush(self.broker["redis_namespace"], json_message)
