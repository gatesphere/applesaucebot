def time(self, username, cmdtime, command, args):
  """ get current system time """
  self.protocol.privmsg(self.channel, "%s: The current time is: %s" % (username, cmdtime))

self.register_action(b'time', time)
