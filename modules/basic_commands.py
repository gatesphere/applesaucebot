def die(self, username, cmdtime, command, args):
  """ kill the bot """
  if args and args[0] == self.admin_pw:
    self.protocol.privmsg(self.channel, "Bye everybody.")
    os._exit(0)
  else:
    self.protocol.privmsg(self.channel, "%s: I can't let you do that." % username)

self.die = types.MethodType(die, None, ApplesauceBot)
self.commands['die'] = self.die

def help_listing(self, username, cmdtime, command, args):
  """ list commands """
  self.protocol.privmsg(self.channel, "%s, my current commands are: %s" % (username, self.commands.keys()))
  
self.help_listing = types.MethodType(help_listing, None, ApplesauceBot)
self.commands['help'] = self.help_listing


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
  diestring = ("1d6" if not args else args[0])
  #if not args:
  #  diestring = "1d6"
  #else:
  #  diestring = args[0]
  values = []
  diestring2 = diestring.replace("-", " -")
  diestring2 = diestring2.replace("+", " ")
  dice = diestring2.lower().split()
  for die in dice:
    if die.find('d') != -1:
      num = die[0:die.index('d')]
      num = (1 if num == '' else int(num))
      sides = int(die[die.index('d')+1:])
      for i in range(num):
        values.append(random.randrange(1, sides+1))
    else:
      values.append(int(die))
  self.protocol.privmsg(self.channel, "%s rolled %s: %d %s" % (username, diestring, sum(values), values))

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
