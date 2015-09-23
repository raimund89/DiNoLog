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


class DiNoLogNode:
    '''The main node class of the DiNoLog logging system'''

    def __init__(self):

        pass

    def send_data(self, data, timestamp=None):
        '''Send data to the server'''

        # Type determination is done by this function.
        # If it fails, we do not send the data and report back to the user
        pass

    def status(self):
        '''Returns the status of the node'''

        if 0:
            pass
        else:
            return {'code': True, 'reason': ''}
