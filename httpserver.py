#!/usr/local/bin/python2

"""
Testing http server with minimal config and authentication.
WARNING: this server is unsafe and should not be used in production.
"""

from twisted.web import server, resource
from twisted.internet import reactor
from twisted.python import log
import sys
import yaml

with open("./config.yml") as configfile:
    config = yaml.load(configfile.read())["servers"]["http"]
port = config["port"]


class CaptureTraffic(resource.Resource):
    isLeaf = True

    def render(self, request):
        print(request.method + " Request:")
        print("----------")
        print(request.content.read())
        print("----------")
        return ""

reactor.listenTCP(port, server.Site(CaptureTraffic()))
reactor.callLater(0.1, lambda: log.startLogging(sys.stdout))
reactor.run()
