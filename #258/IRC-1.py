#------------------------------------------------------------
# Challenge #258: "IRC: Responding To Commands"
# Difficulty: Intermediate
# March 16, 2016
# Brandon Newbright
#------------------------------------------------------------

import socket

class IRCClient(object):
  def __init__(self, nickname, username, realname):
    self.nickname = nickname
    self.username = username
    self.realname = realname
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect(self, address, port):
    self.socket.connect((address, port))
    self.send('NICK %s' % self.nickname)
    self.send('USER %s 0 * :%s' % (self.username, self.realname))
    print('Connected to: %s, port %d' % (address, port))

  def send(self, data):
    self.socket.send((data + '\r\n').encode())

  def poll(self):
    buffer = ""
    while True:
      buffer += self.socket.recv(8192).decode()
      while "\r\n" in buffer:
        line, buffer = buffer.split("\r\n", maxsplit=1)
        print(line)
        command, *params = line.split()
        if command == "PING":
            self.send("PONG %s" % params[0])

client = IRCClient('newtzor', 'newtzor', 'newtzor')
client.connect("chat.freenode.net", 6667)
client.poll()