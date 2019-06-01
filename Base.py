# Base of the Plex Auto Downloader Project
# Nick Steinmetz and Minhaj Shahid - May 2019
#%%
# Dependencies to install:
# pip install qbittorrent-api
from qbittorrentapi import Client

# Class to handle all of the qbittorrent api events
class qbittorrent:
    # Initializing the client & passing in default arguments
    '''
        :param host: the address to access the WebUI interface, following a structure of 'externalip:port'
        :param username: username for the WebUI login
        :param password: password for the WebUI login
    '''
    def init(self, host='74.83.83.201:55440', username='admin', password='adminadmin'):
        client = (Client(host,username,password))
        return(client)

    # Function to search for torrents and return a dictionary containing the results
    '''
        :param search_term: term or phrase to search for
        :param num_results: the number of results to show
    '''
    def search(self, search_term, num_results=None):
        search_id = client.search_start(pattern=search_term, plugins=all)
        print(search_id)
        results = client.search_results(search_id=search_id, limit=num_results)
        return(results)

# Create an object 'qbit' of class qbittorrent 
qbit = qbittorrent()
client = qbit.init()

# Testing search term
# currently returning 'None' - not sure why
'''search_term = 'no country for old men'
results = qbit.search(search_term)
print(results)'''

# Print out a list of methods contained in qbittorrentapi
# help(Client)

# Printing the log of the current client
# print(client.log_main())



#%%