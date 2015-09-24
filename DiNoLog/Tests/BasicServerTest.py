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

from DiNoLog.DiNoLogServer import DiNoLogServer
import getopt
import sys


def run():
    '''This runs the most basic server test: can it run?'''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:", ["configfile="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    configfile = None

    for opt, arg in opts:
        if opt in ("-c", "--configfile"):
            configfile = arg

    try:
        server = DiNoLogServer(configfile)
        if not server.status()['code']:
            print("Not continuing, something is wrong")
        else:
            print("Running the server")
            server.run()
            stop = False
            while not stop:
                data = input('Return an empty line to stop...')
                if data != '':
                    server.log(data, '/test/commandline')
                else:
                    stop = True
            server.stop()
    except:
        print('Something went wrong. Check the logs.')
        raise  # Raise the error again for debugging
    finally:
        print('Goodbye!')

# If the file is run as is, just run the test
if __name__ == '__main__':
    run()
