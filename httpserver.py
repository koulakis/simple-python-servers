from twisted.web import server, resource
from twisted.internet import reactor
from twisted.python import log
import sys


class CaptureTraffic(resource.Resource):
    isLeaf = True

    def render(self, request):
        print(request.method + " Request:")
        print("----------")
        print(request.content.read())
        print("----------")
        return ""

reactor.listenTCP(8000, server.Site(CaptureTraffic()))
reactor.callLater(0.1, lambda: log.startLogging(sys.stdout))
reactor.run()
