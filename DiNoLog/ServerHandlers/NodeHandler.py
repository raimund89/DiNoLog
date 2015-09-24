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

from .Networks import Ethernet, Radio433MHz, RF24, Sockets, USB


class NodeHandler():
    '''Handles all incoming client information, uses the Network-classes'''

    def __init__(self, config):

        if config['Networks']['Ethernet'] == 'enabled':
            self.net_ethernet = Ethernet.Ethernet()

        if config['Networks']['Radio433MHz'] == 'enabled':
            self.net_radio = Radio433MHz.Radio433MHz()

        if config['Networks']['RF24'] == 'enabled':
            self.net_rf24 = RF24.RF24()

        if config['Networks']['Sockets'] == 'enabled':
            self.net_socket = Sockets.Sockets()

        if config['Networks']['USB'] == 'enabled':
            self.net_usb = USB.USB()

    def run(self):
        '''Start all enabled (in serverconf) Networks for listening'''

        if self.net_ethernet:
            self.net_ethernet.run()

        if self.net_radio:
            self.net_radio.run()

        if self.net_rf24:
            self.net_rf24.run()

        if self.net_socket:
            self.net_socket.run()

        if self.net_usb:
            self.net_usb.run()

    def stop(self):
        '''Stop all running Network listeners'''

        if self.net_ethernet:
            self.net_ethernet.stop()

        if self.net_radio:
            self.net_radio.stop()

        if self.net_rf24:
            self.net_rf24.stop()

        if self.net_socket:
            self.net_socket.stop()

        if self.net_usb:
            self.net_usb.stop()

    def status(self):
        '''Returns the status of the handler.'''

        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if 0:
            pass
        else:
            return {'code': True, 'reason': ''}
