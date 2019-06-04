#%%
from qbittorrentapi import Client
# Version of this application
GLOBAL_version = '0.0.1'

# Class to handle all of the qbittorrent api events
class qbittorrent(object):
    # Setting up the client property
    client = Client(host='74.83.83.201:55440', username='admin', password='adminadmin')

    # Constructor to output information for the program 
    def __init__(self):
        print('----------------------------- \n Plex Auto Downloader v%s \n----------------------------- \n' % GLOBAL_version)
        # Return application version, api version, and preferences if verbose output is desired
        print('---------------------------------------- \nqBittorrent application version: %s \nqBittorrent WebUI API version: %s \nUser logged in: %s \n----------------------------------------\n' % (self.client.app_version(), self.client.app_web_api_version(), (self.client.app_preferences().get('web_ui_username'))))

    # Function to return the available plugins and/or update the current plugins
    '''
        :param update: set to 'True' to update all plugins
        :param verbose: set to 'True' to list all plugins
    '''
    def plugins(self, update=False, verbose=False):
        # Updating the available plugins
        if update == True:
            self.client.search_update_plugins()
        # Listing the available plugins
        if verbose == True:
            if len(self.client.search_plugins()) >= 1:
                print('List of available plugins:')
                for i in range(0, len(self.client.search_plugins())):
                    print('- '+self.client.search_plugins()[i]['fullName'])
            else:
                raise Exception('No plugins detected')

    # Function to search for torrents and return a dictionary containing the results
    '''
        :param search_term: term or phrase to search for
        :param num_results: the number of results to show
    '''
    def search(self, search_term=None, num_results=5):
        # Fetch and list the categories available to search for
        categories = self.client.search_categories(plugin_name='all')
        print('\nList of available categories:')
        for i in categories:
            if i != '':
                print('- '+i)
        # Begin a search_job with a specific search_term and use 'all' available plugins and categories
        search_job = self.client.search.start(pattern=search_term, plugins='all', category='all')
        # Parse for search_id
        search_id = search_job['id']
        # Debugging to see what the search_id is returned as
        print('\nSearch ID of search term "%s" is: %s' % (search_term, search_id))
        print(search_job.status()[0].status)
        # Let search continue until results populate
        while True:
            # Stops running the search if status changes to 'Stopped'
            if (search_job.status()[0].status) == 'Stopped':
                break
        # Print the search results
        print(search_job.results())
        # Delete the search results
        search_job.delete()

        # # Store result of search and return the list
        # results = self.client.search_results(search_id=search_id, limit=5, offset=None)['results']

        # # Raise an exception if results array is empty
        # if results == []:
        #     raise Exception('Empty array for "results"')
        # else:
        #     # Else print out the search results            
        #     return(results)

#%%
