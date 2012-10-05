## applesaucebot makeconf.py
## Jacob Peck
##

import sys
import pickle

filename = "bot.conf"

if __name__ == "__main__":
  """ create configuration """
  server = input("server? ") 
  channel = input("channel? ")
  nick = input("nick? ")
  password = input("password? ")
  admin = input("admin password? ")
  f = open(filename, 'wb')
  pickle.dump((server, channel, nick, password, admin), f)
  f.close()
  print("Configuration saved as %s" % filename)

