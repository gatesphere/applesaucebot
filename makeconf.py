## applesaucebot makeconf.py
## Jacob Peck
##

import sys
import pickle

filename = "bot.conf"

def sout(val):
  """ print a line without a following newline """
  sys.stdout.write(val)
  sys.stdout.flush()

def sin( ):
  """ read a line from stdin, and strip trailing whitespace """
  return sys.stdin.readline().rstrip()

if __name__ == "__main__":
  """ create configuration """
  sout("server? ")
  server = sin() 
  sout("channel? ")
  channel = sin()
  sout("nick? ")
  nick = sin()
  sout("password? ")
  password = sin()
  f = open(filename, 'w')
  pickle.dump((server, channel, nick, password), f)
  f.close()
  print "Configuration saved as %s" % filename

