def die(self, username, cmdtime, command, args):
  """ kill the bot """
  if args and args[0] == self.admin_pw:
    self.protocol.privmsg(self.channel, "Bye everybody.")
    os._exit(0)
  else:
    self.protocol.privmsg(self.channel, "%s: I can't let you do that." % username)

self.register_action('die', die)
