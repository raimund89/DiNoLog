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


class LoggingHandler():
    '''Handles the logging of all incoming node data to the database'''

    def __init__(self):
        pass

    def run(self):
        '''Handle the logging queue, so the database will be updated'''
        pass

    def stop(self):
        '''Stop handling the queue. Any new data will not be processed'''
        pass

    def status(self):
        '''Returns the status of the handler.'''
        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if 0:
            pass
        else:
            return {'code': True, 'reason': ''}