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

import h5py
from multiprocessing import Queue
from threading import Event, Thread
from time import sleep


class LoggingHandler():
    '''Handles the logging of all incoming node data to the database'''

    def __init__(self, config):

        # We need a queue for all applications that
        # want to send or receive data
        self.queue = Queue()

        # The event that enables the handler to stop running
        self.stoprunning = Event()

        # Set this one up for later
        self.processthread = None

        # Now open the database file
        self.database = h5py.File(config['Path'], 'a')

        if self.database is None:
            print('Something went wrong while opening the database')
            return

        # TODO: set compression

    def run(self):
        '''Handle the logging queue, so the database will be updated'''

        # First make sure the stop event is not set
        self.stoprunning.clear()

        # Set the running variable
        self.processthread = Thread(None, self.process, 'LoggingHandler-0',
                                    (self.stoprunning, self.queue))

        # And now run it!
        self.processthread.start()

    def stop(self):
        '''Stop handling the queue. Any new data will not be processed'''

        # Set the event to stop running.
        self.stoprunning.set()

        # No wait for the process function to finish
        self.processthread.join()

    def process(self, event, queue):
        '''Process the incoming database'''

        # As long as we do not get a stop signal
        # Even if we need to stop: first process the remaining items!
        while not event.is_set() or not queue.empty():

            if queue.empty():
                # Wait a little while to not stress the processor
                sleep(0.02)  # 20 milliseconds

                continue

            # We can get an item from the queue
            item = queue.get()
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

    def log(self, data, location, timestamp=None):
        '''Add new data to the queue'''

        # At this moment we assume no errors will occur here, because
        # this function should NEVER be called by external sources

        # Add it to the queue. Action 0 indicates a logging action
        self.queue.put({'data': data, 'location': location,
                        'time': timestamp, 'action': 0})

        return True

    def status(self):
        '''Returns the status of the handler.'''
        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if 0:
            pass
        else:
            return {'code': True, 'reason': ''}
