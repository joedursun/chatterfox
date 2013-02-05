import socket, sys

MAX = 65535
PORT = 1060

class Message(object):
  """Model for sending and receiving messages"""

  def __init__(self, remote_address = None):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.s.bind(('',PORT))
    if remote_address:
      self.remote_address = remote_address
      self.s.connect((remote_address, PORT))
    print 'Client socket name is', self.s.getsockname()

  def send(self, text, address = None):
    try:
      self.s.send(text) if address == None else self.s.sendto((text, address))
    except:
      raise

  def receive(self):
    try:
      data, address = self.s.recvfrom(MAX)
      print address[0], '>', repr(data)
    except:
      raise
