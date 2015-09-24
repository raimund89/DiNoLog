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

from threading import Event, Thread
from time import sleep


class USB():
    '''Class providing monitoring of the USB-ports of the server'''

    def __init__(self):

        # The event that enables the handler to stop running
        self.stoprunning = Event()

        # Set this one up for later
        self.processthread = None

    def run(self, loghandler):
        '''Run the USB monitoring thread'''

        # First make sure the stop event is not set
        self.stoprunning.clear()

        # Set the running variable
        self.processthread = Thread(None, self.process, 'USBHandler-0',
                                    (self.stoprunning, loghandler))

        # And now run it!
        self.processthread.start()

    def stop(self):
        '''Stop monitoring the USB-devices'''

        # Set the event to stop running.
        self.stoprunning.set()

        # No wait for the process function to finish
        self.processthread.join()

    def process(self, event, loghandler):
        '''Monitor the USB devices'''

        # As long as we do not get a stop signal
        while not event.is_set():
            # Wait a little while to not stress the processor
            sleep(0.02)  # 20 milliseconds

        print('Got the stop signal, so stopping')

    def status(self):
        '''Returns the status of the USB monitoring'''

        if 0:
            pass
        else:
            return {'code': True, 'reason': ''}
