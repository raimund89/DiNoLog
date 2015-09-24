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
from threading import Event


class NodeHandler():
    '''Handles all incoming client information, uses the Network-classes'''

    def __init__(self, config, loghandler):

        # An event to stop all networks
        self.stoprunning = Event()

        # Remember the config
        self.config = config

        if config['Networks']['Ethernet'] == 'enabled':
            self.net_ethernet = Ethernet.Ethernet(self.stoprunning, loghandler)

        if config['Networks']['Radio433MHz'] == 'enabled':
            self.net_radio = Radio433MHz.Radio433MHz(self.stoprunning,
                                                     loghandler)

        if config['Networks']['RF24'] == 'enabled':
            self.net_rf24 = RF24.RF24(self.stoprunning, loghandler)

        if config['Networks']['Sockets'] == 'enabled':
            self.net_socket = Sockets.Sockets(self.stoprunning, loghandler)

        if config['Networks']['USB'] == 'enabled':
            self.net_usb = USB.USB(self.stoprunning, loghandler)

    def run(self):
        '''Start all enabled (in serverconf) Networks for listening'''

        self.stoprunning.clear()

        if self.net_ethernet:
            self.net_ethernet.start()

        if self.net_radio:
            self.net_radio.start()

        if self.net_rf24:
            self.net_rf24.start()

        if self.net_socket:
            self.net_socket.start()

        if self.net_usb:
            self.net_usb.start()

    def stop(self):
        '''Stop all running Network listeners'''

        self.stoprunning.set()

        if self.net_ethernet:
            self.net_ethernet.join()

        if self.net_radio:
            self.net_radio.join()

        if self.net_rf24:
            self.net_rf24.join()

        if self.net_socket:
            self.net_socket.join()

        if self.net_usb:
            self.net_usb.join()

    def status(self):
        '''Returns the status of the handler.'''

        # TODO: increase the testing in this status method

        # Status can be True or False. If False, an additional string will
        # specify what exactly is the problem
        if self.config['Networks']['Ethernet'] and self.net_ethernet is None:
            return {'code': False, 'reason': 'Ethernet not monitored'}
        elif self.config['Networks']['Radio433MHz'] and self.net_radio is None:
            return {'code': False, 'reason': 'Radio not monitored'}
        elif self.config['Networks']['RF24'] and self.net_rf24 is None:
            return {'code': False, 'reason': 'RF24 not monitored'}
        elif self.config['Networks']['Sockets'] and self.net_socket is None:
            return {'code': False, 'reason': 'Sockets not monitored'}
        elif self.config['Networks']['USB'] and self.net_usb is None:
            return {'code': False, 'reason': 'USB not monitored'}
        else:
            return {'code': True, 'reason': ''}
