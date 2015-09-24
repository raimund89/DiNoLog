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
                             SyncHandler, ConfigHandler)
from time import time


class DiNoLogServer():
    '''The main server class of the DiNoLog logging system'''

    def __init__(self):
        '''Initialize the DiNoLog server'''

        # TODO: making the appropriate attributes private

        self.confighandler = ConfigHandler.ConfigHandler()
        if not self.confighandler.status()['code']:
            self.print_warning()
            return

        self.loghandler = LoggingHandler.LoggingHandler(
                                                self.confighandler['Database'])
        if not self.loghandler.status()['code']:
            self.print_warning()
            return

        # TODO: check if this server is registered in the database

        self.synchandler = SyncHandler.SyncHandler()
        if not self.synchandler.status()['code']:
            self.print_warning()
            return

        self.nodehandler = NodeHandler.NodeHandler(
                                                self.confighandler)
        if not self.nodehandler.status()['code']:
            self.print_warning()
            return

        self.queryhandler = QueryHandler.QueryHandler()
        if not self.queryhandler.status()['code']:
            self.print_warning()
            return

    def update(self):
        '''Forces a synchronization between the servers. Must be done
           before the /run/ function can be called!!'''

        pass

    def run(self):
        '''Actually starts the server to listen to the nodes'''

        if self.loghandler.status()['code']:
            self.loghandler.run()
        else:
            self.print_warning()
            return

        if self.synchandler.status()['code']:
            self.synchandler.run()
        else:
            self.loghandler.stop()
            self.print_warning()
            return

        if self.nodehandler.status()['code']:
            self.nodehandler.run()
        else:
            self.synchandler.stop()
            self.loghandler.stop()
            self.print_warning()
            return

        if self.queryhandler.status()['code']:
            self.queryhandler.run()
        else:
            self.nodehandler.stop()
            self.synchandler.stop()
            self.loghandler.stop()
            self.print_warning()
            return

    def stop(self):
        '''A graceful way of killing the server'''

        self.queryhandler.stop()
        if not self.queryhandler.status()['code']:
            self.print_warning()

        self.nodehandler.stop()
        if not self.queryhandler.status()['code']:
            self.print_warning()

        self.synchandler.stop()
        if not self.queryhandler.status()['code']:
            self.print_warning()

        self.loghandler.stop()
        if not self.loghandler.status()['code']:
            self.print_warning()

    def status(self):
        '''Returns the status of the server'''

        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if not self.confighandler.status()['code']:
            return {'code': False, 'reason': 'Confighandler: ' +
                                             self.confighandler.status()['reason']}
        else:
            return {'code': True, 'reason': ''}

    def print_warning(self):
        '''Print a do-not-use warning if something went wrong'''

        # TODO: raise errors or return error codes for better error-handling
        print("\n====================== WARNING ======================")
        print("Do not use this instance of DiNoLogServer! Something")
        print("went wrong during initialization. Check the logs!")
        print("====================== WARNING ======================\n")

    def log(self, data, location, timestamp=None):
        '''Adds the ability to (directly) log something to the server'''

        if data is None or location is None:
            return False

        # If no timestamp is given, use our own timestamp
        if timestamp is None:
            timestamp = time()

        return self.loghandler.log(data, timestamp)
