import sys, socket
from message import Message
from threading import Thread

def start_thread(func, arguments):
  thread = Thread(target = func, args = arguments)
  thread.setDaemon(True)
  thread.start()

def get_remote_address():
  import os
  print 'Searching for other devices on the network. This may take a while...'
  ip_list = os.system('arp -a')
  print 'Here is a list of possible hosts: ', ip_list
  return raw_input('Enter the ip of the host to connect to: ')

def receive_messages(telegram):
  print 'Listening for incoming messages.'
  while True:
    telegram.receive()

def send_messages(telegram):
  print 'Ready to chat: \n'
  while True:
    try:
      telegram.send(raw_input())
    except (KeyboardInterrupt, SystemExit):
      telegram.cleanup()
      print '\n Shutting down Chatterfox'
      sys.exit(2)
    except:
      raise # show the error; easier to debug and fix

def client_handler(address = None):
  remote_address = get_remote_address() if address == None else address
  try:
    telegram = Message(remote_address)
    telegram.buddies[remote_address] = raw_input('Enter nickname for buddy: ')
    start_thread(receive_messages, ([telegram]))
    send_messages(telegram)
  except socket.gaierror:
    print 'Invalid address. Shutting down Chatterfox.'
    sys.exit(1)
  except:
    raise # show the error; easier to debug and fix
