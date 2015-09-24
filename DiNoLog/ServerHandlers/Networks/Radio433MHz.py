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

from threading import Thread
from time import sleep


class Radio433MHz(Thread):
    '''Class providing monitoring of 433MHz radios connected to the server'''

    def __init__(self, event, loghandler):
        Thread.__init__(self)

        # The event that enables the handler to stop running
        self.stoprunning = event

        # The loghandler to log events
        self.loghandler = loghandler

    def run(self):
        '''Monitor the radio devices'''

        # As long as we do not get a stop signal
        while not self.stoprunning.is_set():
            # Wait a little while to not stress the processor
            sleep(0.02)  # 20 milliseconds

        print('Radio_Network: got the stop signal, so stopping')
