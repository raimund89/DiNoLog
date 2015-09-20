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

import configparser


class ConfigHandler(configparser.ConfigParser):

    def __init__(self):
        super().__init__()

        # TODO: add other ways to specify the location of the config file
        # For now, the config file is in the current directory
        try:
            self.read_file(open('dinologserver.conf'))
            self.hasfile = True
        except IOError:
            # The config file does not exist. Quit with the message
            # that the user should either specify the file or put it in
            # the right place. The server can work with an empty file,
            # but not with a nonexistant file
            print("ERROR: The file 'dinologserver.conf' does not exist")
            print("       It should exist before starting the DiNoLogServer")
            print("       You can find a sample config in the documentation")

            self.hasfile = False

    def status(self):
        '''Returns the status of the handler.'''
        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if not self.hasfile:
            return {'code': False, 'reason': 'Could not open config file'}
        else:
            return {'code': True, 'reason': ''}
