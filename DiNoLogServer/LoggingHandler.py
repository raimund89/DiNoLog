# -*- coding: utf-8 -*-

from twisted.internet import protocol


class LoggingHandler(protocol.Protocol):

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        pass

    def connectionLost(self):
        pass
