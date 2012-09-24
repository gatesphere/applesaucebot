## applesaucebot makeconf.py
## Jacob Peck
##

import sys
import pickle

def sout(val):
  sys.stdout.write(val)
  sys.stdout.flush()

def sin( ):
  return sys.stdin.readline().rstrip()

if __name__ == "__main__":
  sout("server? ")
  server = sin() 
  sout("channel? ")
  channel = sin()
  sout("nick? ")
  nick = sin()
  sout("password? ")
  password = sin()
  f = open('bot.conf', 'w')
  pickle.dump((server, channel, nick, password), f)
  f.close()
  print "Configuration saved as bot.conf"

