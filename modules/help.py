def help_listing(self, username, cmdtime, command, args):
  """ list commands """
  self.protocol.privmsg(self.channel, "%s, my current commands are: %s" % (username, sorted(self.commands.keys())))

self.register_action('help', help_listing)
self.register_action('commands', help_listing)
