Chatterfox
==========
Chatterfox is a simple, lightweight and easy to setup chat client for use on local area networks. It has been tested with Python 2.7 on Windows (XP|7) and Mac OS X 10.8 and works well on both. Incoming text is currently displayed as black text on a green background; soon these colors will be easily configured via an environment variable.

Chatterfox relies solely on the python standard library, so no need to bother with package managers.

Setup
=====
Add chatterfox/chatter to your path
* ```[sudo] ln -s /path/to/chatterfox/chatter /usr/local/bin```

Usage
=====
Assuming chatter is in your path
* ```chatter [ ip ]```

If the IP is left out, chatterfox will shell out a list of IPs on the network and you may select the one you want to connect to.
