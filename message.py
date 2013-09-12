import socket, sys
from text_colors import Colors

MAX = 65535
PORT = 1060

class Message(object):
  """Model for sending and receiving messages"""

  def __init__(self, remote_address = None):
    self.bind_sock()
    self.buddies = {}
    if remote_address:
      self.connect_to_remote_host(remote_address)
    print 'Client socket name is', self.s.getsockname()

  def bind_sock(self):
    try:
      self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.s.bind(('',PORT))
    except socket.error:
        print 'Address in use. Are you already running Chatterfox?'
        sys.exit(2)

  def connect_to_remote_host(self, remote_address):
    self.remote_address = remote_address
    self.s.connect((remote_address, PORT))

  def add_buddy(self, address):
    name = raw_input('No nickname for ' + address + '. What would you like to name your buddy? ')
    self.buddies[address] = name

  def pretty_print(self, buddy_name, text = ''):
    print Colors.TEXTGREEN, '<', buddy_name, '>', text, Colors.END

  def send(self, text, address = None):
    try:
      self.s.send(text) if address == None else self.s.sendto((text, address))
    except socket.error as e:
      print e,'Either your friend is not running Chatterfox or the address is incorrect.'
      remote_address = raw_input('Please enter another address (ctrl+c to exit): ')
      self.remote_address = remote_address
      self.s.connect((remote_address, PORT))

  def receive(self):
    data, address = self.s.recvfrom(MAX)

    if not self.buddies.has_key(address[0]):
      self.add_buddy(address[0])

    self.pretty_print(self.buddies[address[0]], repr(data))

  def cleanup(self):
    self.s.shutdown()
    self.s.close()
