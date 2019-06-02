# Base of the Plex Auto Downloader Project
# Nick Steinmetz and Minhaj Shahid - June 2019
#%%
# Dependencies to install:
# pip install qbittorrent-api
from qbittorrentapi import Client

# Version of this application
version = '0.0.1'

# Class to handle all of the qbittorrent api events
class qbittorrent:
    # Initializing the client & passing in default arguments
    '''
        :param host: the address to access the WebUI interface, following a structure of 'externalip:port'
        :param username: username for the WebUI login
        :param password: password for the WebUI login
        :param verbose: optional arg to show basic information on program and user
    '''
    def init(self, host='74.83.83.201:55440', username='admin', password='adminadmin', verbose=False):
        client = Client(host,username,password)
        print('----------------------------- \n Plex Auto Downloader v%s \n----------------------------- \n' % version)
        # Return application version, api version, and preferences if verbose output is desired
        if verbose == True:
            pref = client.app_preferences()
            print('---------------------------------------- \nqBittorrent application version: %s \nqBittorrent WebUI API version: %s \nUser logged in: %s \n----------------------------------------\n' % (client.app_version(), client.app_web_api_version(), (pref.get('web_ui_username'))))
        # Return the client when calling the class
        return(client)

    # Function to search for torrents and return a dictionary containing the results
    '''
        :param search_term: term or phrase to search for
        :param num_results: the number of results to show
    '''
    def search(self, search_term, num_results=None):
        # Begin a search with a specific search_term and use 'all' available plugins
        search_id = client.search_start(pattern=search_term, plugins='all')
        # Debugging to see what the search_id is returned as
        print('The search ID is: %s' % search_id)
        # Print the status of the search to make sure operation completed successfully
        status = client.search_status(search_id)
        print('The status of the search is: %s' % status)
        # Store list of torrents and return the list
        results = client.search_results(search_id=search_id, limit=num_results)
        return(results)

# Create an object 'qbit' of class qbittorrent
qbit = qbittorrent()
# Call init with the default parameters
client = qbit.init(verbose=True)

# Testing the search function
# currently returning 'None' - not sure why
search_term = 'brrip'
results = qbit.search(search_term)
# Print out the JSON file of the search results
print('The results are: %s' %results)

# Print out the list of current completed torrents
# Implemented to see if there was a response from the WebUI API call
# torrent_list = client.torrents_info(status_filter='completed')
# print(torrent_list)

# Print out a list of methods contained in qbittorrentapi
print()
help(Client)
#%%
