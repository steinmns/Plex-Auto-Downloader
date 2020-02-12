# Base of the Plex Auto Downloader Project
# Nick Steinmetz and Minhaj Shahid - June 2019

# Dependencies to install:
# pip install qbittorrent-api
from API.qbtAPI import qbittorrent

# Create an object 'qbit' of class qbittorrent
qbit = qbittorrent()
print('test')
# Testing the search function
search_term = 'no country for old men'
qbit.search(search_term=search_term, num_results=5)

# Print out the list of current completed torrents
# print('Completed torrents:')
completed_torrent_list = qbit.client.torrents_info(status_filter='completed')
# Iterate through the list of completed torrents and print the name of each one
# for torrent in range(0,len(completed_torrent_list)):
#     print('- '+completed_torrent_list[torrent]['name'])

# Print out a list of methods contained in qbittorrentapi
# print()
# help(client)
