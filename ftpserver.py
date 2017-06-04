"""
Testing ftp server with minimal config and authentication.
WARNING: this server is unsafe and should not be used in production.
"""

from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.internet import reactor
from twisted.python import log
import sys
import yaml

with open("./config.yml") as configfile:
    config = yaml.load(configfile.read())["servers"]["ftp"]
port = config["port"]
username = config["username"]
password = config["password"]
homeDirectory = config["homeDirectory"]

userChecker = InMemoryUsernamePasswordDatabaseDontUse()
userChecker.addUser(username, password)

ftp = FTPFactory(
        Portal(
            FTPRealm('./', userHome=homeDirectory),
            [AllowAnonymousAccess(), userChecker]))

reactor.listenTCP(port, ftp)
reactor.callLater(0.1, lambda: log.startLogging(sys.stdout))
reactor.run()
