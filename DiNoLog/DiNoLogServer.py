# -*- coding: utf-8 -*-

"""
    DiNoLog - Distributed Node Logging System for Python
    Copyright (C) 2015  Raimond Frentrop

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# The server flow:
# - Read the config file (includes the server list)
# - Add an instance of the LoggingHandler so we can read and
#   write data, and get a list of nodes when necessary
# - Create and instance of the SyncHandler (does an initial update)
# - When syncing is done, create a NodeHandler. It listens for any
#   incoming node connections and handles them

from .ServerHandlers import (LoggingHandler, NodeHandler, QueryHandler,
                             SyncHandler)


class DiNoLogServer():

    def __init__(self):
        '''Initialize the DiNoLog server'''

        self.loghandler = LoggingHandler.LoggingHandler()
        self.nodehandler = NodeHandler.NodeHandler()
        self.queryhandler = QueryHandler.QueryHandler()
        self.synchandler = SyncHandler.SyncHandler()

    def update(self):
        '''Forces a synchronization between the servers. Must be done'''
        '''before the /run/ function can be called!!'''
        pass

    def run(self):
        '''Actually starts the server to listen to the nodes'''
        pass

    def stop(self):
        '''A graceful way of killing the server'''
        pass
