def flip(self, username, cmdtime, command, args):
  """ flip a coin """
  if bool(random.getrandbits(1)):
    coin = "heads"
  else:
    coin = "tails"
  self.protocol.privmsg(self.channel, "%s flipped a coin: %s" % (username, coin))

self.register_action('flip', flip)
