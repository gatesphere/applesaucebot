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

self.register_action('roll', roll)
