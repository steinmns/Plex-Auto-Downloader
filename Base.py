# Base of the Plex Auto Downloader Project
# Nick Steinmetz and Minhaj Shahid - June 2019
#%%
# Dependencies to install:
# pip install qbittorrent-api
from qbittorrentapi import Client

# Version of this application
version = '0.0.1'

# Class to handle all of the qbittorrent api events
class qbittorrent(object):
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
    def search(self, search_term=None, num_results=5):
        # Fetch and list the categories available to search for
        categories = client.search_categories(plugin_name='all')
        print('List of available categories:')
        for i in categories:
            if i != '':
                print('- '+i)
        # Begin a search with a specific search_term and use 'all' available plugins and store the search id
        search_id = client.search_start(pattern=search_term, plugins='all', category='all')['id']
        # Debugging to see what the search_id is returned as
        print('\nSearch ID of search term "%s" is: %s' % (search_term, search_id))
        # Print the status of the search to make sure operation completed successfully
        status = client.search_status(search_id=search_id)[0]
        print('Status of search: %s' % status['status'])
        # Attempting to let search continue until results populate
        # while (status['total']) < 2:
        #     if status['total'] == 1:
        #         print('The status of the search is: %s' % status)
        # Stops running the search
        client.search_stop(search_id=search_id)
        # Store result of search and return the list
        results = client.search_results(search_id=search_id, limit=5, offset=None)['results']
        return(results)

# Create an object 'qbit' of class qbittorrent
qbit = qbittorrent()
# Call init with the default parameters
client = qbit.init(verbose=True)

# Testing the search function
search_term = 'no country for old men'
results = qbit.search(search_term=search_term, num_results=50)
# Raise an exception if results array is empty
if results == []:
    raise Exception('Empty array for "results"')
else:
    # Else print out the search results
    print('The results are: %s\n' % results)

# Print out the list of current completed torrents
print('Completed torrents:')
completed_torrent_list = client.torrents_info(status_filter='completed')
# Iterate through the list of completed torrents and print the name of each one
for torrent in range(0,len(completed_torrent_list)):
    print('- '+completed_torrent_list[torrent]['name'])

# Print out a list of methods contained in qbittorrentapi
print()
help(Client)
#%%
