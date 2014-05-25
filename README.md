Moustash
========

Moustash is project which permit to have a scalable notification system.
Moustash is 3 parts project

##Cuir

Cuir is a port prober which send messages to logstash broker

##Fouet

Fouet is an event listener for supervisor, which send a message to a broker each time the status of a process change

##PanPan

PanPan is a futur project which will permit to send messages directly to the broker through a socket

#Infrastructure

Moustash is based on Logstash :

![Moustash](docs/Moustash.jpg)

The principle is to have a fast, scalable and easy to install deployment system


# Tips

```{"tags": ["test"], "@version": 1, "@timestamp": "2014-05-25T17:01:33.062Z", "host": "wowi.io", "file": "/var/log/test.log", "message": "toto", "type": "test", "program": "cuir", "source": "moustash"}```

date ISO8601

 iso_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
