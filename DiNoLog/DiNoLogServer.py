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
from threading import Event


class DiNoLogServer():
    '''The main server class of the DiNoLog logging system'''

    def __init__(self, configfile=None):
        '''Initialize the DiNoLog server'''

        # TODO: making the appropriate attributes private

        # An event to stop the LoggingHandler
        self.stopevent = Event()

        self.confighandler = ConfigHandler.ConfigHandler(configfile)
        if not self.confighandler.status()['code']:
            self.print_warning()
            return

        self.loghandler = LoggingHandler.LoggingHandler(
            self.confighandler['Database'], self.stopevent)
        if self.loghandler is None:
            self.print_warning()
            return

        # TODO: check if this server is registered in the database

        self.synchandler = SyncHandler.SyncHandler(
            self.confighandler['Server Pool'], self.stopevent)
        if self.synchandler is None:
            self.print_warning()
            return

        self.nodehandler = NodeHandler.NodeHandler(self.confighandler, self)
        if not self.nodehandler.status()['code']:
            self.print_warning()
            return

        self.queryhandler = QueryHandler.QueryHandler(
            self.confighandler['Querying'], self.stopevent)
        if self.queryhandler is None:
            self.print_warning()
            return

    def update(self):
        '''Forces a synchronization between the servers. Must be done
           before the /run/ function can be called!!'''

        pass

    def run(self):
        '''Actually starts the server to listen to the nodes'''

        self.stopevent.clear()

        if self.loghandler:
            self.loghandler.start()
        else:
            self.print_warning()
            return

        if self.synchandler:
            self.synchandler.start()
        else:
            self.stopevent.set()
            self.loghandler.join()
            self.print_warning()
            return

        if self.nodehandler.status()['code']:
            self.nodehandler.run()
        else:
            self.stopevent.set()
            self.synchandler.join()
            self.loghandler.join()
            self.print_warning()
            return

        if self.queryhandler:
            self.queryhandler.start()
        else:
            self.nodehandler.stop()
            self.stopevent.set()
            self.synchandler.join()
            self.loghandler.join()
            self.print_warning()
            return

    def stop(self):
        '''A graceful way of killing the server'''

        self.nodehandler.stop()
        if not self.nodehandler.status()['code']:
            self.print_warning()

        self.stopevent.set()
        self.queryhandler.join()
        self.synchandler.join()
        self.loghandler.join()

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

        self.stop()

    def log(self, data, location, timestamp=None):
        '''Adds the ability to (directly) log something to the server'''

        if data is None or location is None:
            return False

        # If no timestamp is given, use our own timestamp
        if timestamp is None:
            timestamp = time()

        return self.loghandler.log(data, timestamp)
