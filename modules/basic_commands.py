def hello(self, username, cmdtime, command, args):
  """ greet the user """
  self.protocol.privmsg(self.channel, "Hello there, %s!" % username)

self.hello = types.MethodType(hello, None, ApplesauceBot)
self.commands['hello'] = self.hello
self.commands['hai?'] = self.hello
self.commands['hai'] = self.hello
self.commands['herro'] = self.hello

def time(self, username, cmdtime, command, args):
  """ get current system time """
  self.protocol.privmsg(self.channel, "%s: The current time is: %s" % (username, cmdtime))

self.time = types.MethodType(time, None, ApplesauceBot)
self.commands['time'] = self.time

def roll(self, username, cmdtime, command, args):
  """ roll dice """
  num = random.randrange(1,6+1)
  self.protocol.privmsg(self.channel, "%s rolled a d6: %d" % (username, num))

self.roll = types.MethodType(roll, None, ApplesauceBot)
self.commands['roll'] = roll

def flip(self, username, cmdtime, command, args):
  """ flip a coin """
  if bool(random.getrandbits(1)):
    coin = "heads"
  else:
    coin = "tails"
  self.protocol.privmsg(self.channel, "%s flipped a coin: %s" % (username, coin))

self.flip = types.MethodType(flip, None, ApplesauceBot)
self.commands['flip'] = self.flip
