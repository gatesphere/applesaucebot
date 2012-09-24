## applesaucebot
## Jacob Peck
## 

import sys
import time
import pickle
import botlib
import random

class ApplesauceBot(botlib.Bot):
  def __init__(self, server, channel, nick, password=None):
    botlib.Bot.__init__(self, server, 6667, channel, nick)
    if password != None:
      self.protocol.privmsg("nickserv", "identify %s" % password)
    print "Connected to channel %s with nick %s" % (self.channel, self.nick)

  def __actions__(self):
    botlib.Bot.__actions__(self)
    username = self.get_username()
    if botlib.check_found(self.data, "?hello"):
      self.hello(username)
    if botlib.check_found(self.data, "?time"):
      self.time(username)
    if botlib.check_found(self.data, "?roll"):
      self.roll(username)
    if botlib.check_found(self.data, "?flip"):
      self.flip(username)

  def hello(self, username):
    self.protocol.privmsg(self.channel, "Hello %s!" % username)

  def time(self, username):
    t = time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
    self.protocol.privmsg(self.channel, "%s: The current time is: %s" % (username, t))

  def roll(self, username):
    num = random.randrange(1,6+1)
    self.protocol.privmsg(self.channel, "%s rolled a d6: %d" % (username, num))

  def flip(self, username):
    if bool(random.getrandbits(1)):
      coin = "heads"
    else:
      coin = "tails"
    self.protocol.privmsg(self.channel, "%s flipped a coin: %s" % (username, coin))

if __name__ == "__main__":
  f = open('bot.conf', 'r')
  c = pickle.load(f)
  f.close()
  ApplesauceBot(c[0], c[1], c[2], c[3]).run()

