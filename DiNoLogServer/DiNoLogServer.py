# -*- coding: utf-8 -*-

# The server flow:
# - Read the config file (includes the server list)
# - Add an instance of the LoggingHandler so we can read and
#   write data, and get a list of nodes when necessary
# - Create and instance of the SyncHandler (does an initial update)
# - When syncing is done, create a NodeHandler. It listens for any
#   incoming node connections and handles them


class DiNoLogServer():

    def __init__(self):
        '''Initialize some basic parameters and load the config file'''
        pass

    def update(self):
        '''Forces a synchronization between the servers. Must be done'''
        '''before the /run/ function can be called!!'''
        pass

    def run(self):
        '''Actually starts the server to listen to the nodes'''
        pass

    def stop(self):
        '''A graceful way of killing the server'''
        pass
