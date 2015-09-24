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


class SyncHandler(Thread):
    '''Organizes the synchronization of the database with other servers'''

    def __init__(self, config, event):
        Thread.__init__(self)

        # The synchronization config
        self.config = config

        # The event that will signal the stop command
        self.stoprunning = event

    def run(self):
        '''Start continuous sync, passing new data to all other servers'''

        while not self.stoprunning.is_set():
            sleep(0.2)

        print('SyncHandler: got the stop signal, so stopping')
