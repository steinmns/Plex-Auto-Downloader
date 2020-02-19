# Base of the Plex Auto Downloader Project
# Nick Steinmetz and Minhaj Shahid - June 2019

# Dependencies to install:
# pip install qbittorrent-api
from API.qbtAPI import qbittorrent

# Create an object 'qbit' of class qbittorrent
qbit = qbittorrent()

# Testing the search function
search_term = 'Elite Yankee Saburo'
if(('1080p' in search_term)== False):
    search_term += ' 1080p'
print(search_term)
searchResults = qbit.search(search_term=search_term, num_results=5) #NOTE: returns as a dict so you cannot just say results[0] to get first item

if(len(searchResults.results) > 0):
    print(str(len(searchResults.results)) + ' results found!')
    #if(searchResults.results[0].nbSeeders > 0 and searchResults.results[0].nbLeechers >= 0):
    qbit.startTorrent(searchResults.results[0].fileUrl)
else:
    print('No results found')
    

# Print out the list of current completed torrents
# print('Completed torrents:')
#completed_torrent_list = qbit.client.torrents_info(status_filter='completed')

# Iterate through the list of completed torrents and print the name of each one
# for torrent in range(0,len(completed_torrent_list)):
#     print('- '+completed_torrent_list[torrent]['name'])

# Print out a list of methods contained in qbittorrentapi
# print()
# help(client)
