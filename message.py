import socket

MAX = 65535
PORT = 1060

class Message(object):
  """Model for sending and receiving messages"""

  def __init__(self, remote_address = None):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.s.bind(('',PORT))
    self.buddies = {}
    if remote_address:
      self.remote_address = remote_address
      self.s.connect((remote_address, PORT))
    print 'Client socket name is', self.s.getsockname()

  def add_buddy(self, address):
    name = raw_input('No nickname for ' + address + '. What would you like to name your buddy? ')
    self.buddies[address] = name

  def send(self, text, address = None):
    self.s.send(text) if address == None else self.s.sendto((text, address))

  def receive(self):
    data, address = self.s.recvfrom(MAX)
    if not self.buddies.has_key(address[0]):
      self.add_buddy(address[0])
    print '<', self.buddies[address[0]], '>', repr(data)
