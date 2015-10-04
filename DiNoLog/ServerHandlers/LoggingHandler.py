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

import tables
from multiprocessing import Queue
from threading import Thread
from time import sleep


class LoggingHandler(Thread):
    '''Handles the logging of all incoming node data to the database'''

    def __init__(self, config, event):
        Thread.__init__(self)

        # We need a queue for all applications that
        # want to send or receive data
        self.queue = Queue()

        # The event that enables the server to stop this service
        self.stoprunning = event

        # Now open the database file
        self.database = tables.open_file(config['Path'], mode="a",
                                         title="DiNoLog")

        if self.database is None:
            print('Something went wrong while opening the database')
            return

        if not self.database.root.__contains__('config'):
            # Apparently, the file is made for the first time.

            # Add the 'config' group, and add the 'servers' and 'nodes'
            # information tables
            confgr = self.database.create_group("/", "config",
                                                "DiNoLog Configuration Group")
            self.database.create_table(confgr, "servers",
                                       Table_Servers, "Server Pool")
            self.database.create_table(config, "nodes", Table_Nodes,
                                       "Registered Nodes")

            # Add the data group
            self.database.create_group("/", "data",
                                       "DiNoLog Data Group")

            # Important: write to the database
            self.flush()

        # TODO: set compression

    def run(self):
        '''Process the incoming database'''

        # As long as we do not get a stop signal
        # Even if we need to stop: first process the remaining items!
        while not self.stoprunning.is_set() or not self.queue.empty():

            if self.queue.empty():
                # Wait a little while to not stress the processor
                sleep(0.02)  # 20 milliseconds

                continue

            # We can get an item from the queue
            item = self.queue.get()
            print(item['data'])

            # Action values:
            # 0 - Data logging
            # 1 - Registration of new node
            # 2 - Registration of new server
            # 3 - Query of data
            # 4 - Request for server list
            # 5 - Request for node list

            if item['action'] == 0:
                # Log it!
                pass
            elif item['action'] == 1:
                # Register a node
                pass
            elif item['action'] == 2:
                # Register a server
                pass
            elif item['action'] == 3:
                # Its a query
                pass
            elif item['action'] == 4:
                # Returning a list of all registered servers
                pass
            elif item['action'] == 5:
                # Returning a list of all registered nodes
                pass
            else:
                # Unknown action, log an error and continue
                print('Unknown queue action')

        print('LoggingHandler: got the stop signal, so stopping')

    def log(self, data, location, node, timestamp=None):
        '''Add new data to the queue'''

        # At this moment we assume no errors will occur here, because
        # this function should NEVER be called by external sources

        # Add it to the queue. Action 0 indicates a logging action
        self.queue.put({'data': data, 'location': location, 'node': node,
                        'time': timestamp, 'action': 0})

        return True

node_types = tables.Enum(['Ethernet', 'Radio433MHz', 'RF24', 'Sockets', 'USB'])


class Table_Servers(tables.IsDescription):
    name = tables.StringCol()
    ip = tables.StringCol()
    port = tables.UInt16Col()
    server_id = tables.UInt32()
    key = tables.StringCol()
    description = tables.StringCol()


class Table_Nodes(tables.IsDescription):
    name = tables.StringCol()
    node_type = tables.EnumCol(node_types, 'Ethernet')
    node_id = tables.UInt32()
    key = tables.StringCol()
    description = tables.StringCol()
