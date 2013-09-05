# spellcheck plugin
# spells words for you
# requires pyenchant

def spell(self, username, cmdtime, command, args):
  import enchant

  if args:
    args = " ".join(args)
    e = enchant.Dict('en_US')
    if not e.check(args):
      words = e.suggest(args)
      self.protocol.privmsg(self.channel, "%s, here are some suggested spellings for '%s': %s" % (username, args, words))
    else:
      self.protocol.privmsg(self.channel, "%s, it looks as though '%s' is a valid word." % (username, args))
  else:
    self.protocol.privmsg(self.channel, "%s, I need a word to check!" % username)

self.register_action('spell', spell)

