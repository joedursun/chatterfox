import sys, os
from message import Message
from threading import Thread

def start_thread(func, arguments):
  thread = Thread(target = func, args = arguments)
  thread.setDaemon(True)
  thread.start()

def get_remote_address():
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
      message = raw_input()
      telegram.send(message)
    except (KeyboardInterrupt, SystemExit):
      print '\n Shutting down Chatterfox'
      sys.exit(2)
    except:
      raise

def client_handler(address = None):
  remote_address = get_remote_address() if address == None else address
  telegram = Message(remote_address)
  try:
    start_thread(receive_messages, ([telegram]))
    send_messages(telegram)
  except:
    raise
