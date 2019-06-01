# Plex Auto Downloader
Plex Auto Downloader is a tool that serves as a mediator between a front end designed in Bootstrap and a Python powered database backend for Plex media servers using an open source p2p program, qBittorrent. The front end will be built using Node.js and Bootstrap while the backend will be handled from an application built in Python using qBittorrent.

# Upcoming Features:
- Automatically choose best torrent
- Pipe results to Plex directory
- Acquire any missing metadata (Plex may automatically take care of this, if so need to send Plex an 'update libraries' call)
- Limit number of simultaneous torrents
- Postpone torrents with slow DL speeds (use seed ratios as a determinant?)
- Interface to show log and any other interesting info
- Check library first to see if file already exists (or typos of filename)
- Display current queue and DL status
- GUI (web portal) for search bar
  - category button (is file a movie or a tv
show, etc)
  - logging mode button

# Technical Specifications
  - Base application written in Python
  - Webapp written in: *TBD*
# Reference Documents
  - [qBittorrent WebUI API GitHub Repository](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-Documentation)
  - [Node.js - JavaScript runtime](https://nodejs.org/en/)
  - [Open Port Check Tool](https://www.canyouseeme.org/) 
  - [qBittorrent API Python Wrapper](https://github.com/rmartin16/qbittorrent-api.git)

# Change Log
6/1/2019: 
- Set-up qBittorrent external access through creating an “application”
with the following settings:
   - WAN Interface of “Ethernet_DEFAULT” (Due to being directly
connected to router)
   - Server IP of 192.168.200.26 (IPV4 address)
   - Start & End ports as 55440
   - TCP Protocol
 - qBittorrent settings were configured as followed:
   - IP address of 192.168.200.26 (Hard coded in case current IP
dynamically changes)
   - Port as 55440
 - To access the remote qBittorrent WebUI use the following host:
   - http://192.168.200.26:55440/ (for localhost)
   - http://74.83.83.201:55440/ (for all outside connections)