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


class QueryHandler(Thread):
    '''Handles all incoming requests for data from external sources'''

    def __init__(self, config, event):
        Thread.__init__(self)

        # The query config
        self.config = config

        # The event that will signal the stop command
        self.stoprunning = event

    def run(self):
        '''Run the query listener'''

        while not self.stoprunning.is_set():
            sleep(0.2)

        print('QueryHandler: got the stop signal, so stopping')
