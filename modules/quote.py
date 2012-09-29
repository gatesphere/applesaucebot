def quote(self, username, cmdtime, command, args):
  import urllib, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  gist_count = 3
  args = " ".join(args)
  url = 'http://www.iheartquotes.com/api/v1/random'
  content = urllib.urlopen(url).read()
  reg = re.compile(r'\\x(\w{2})')
  ascii_string = reg.sub(asciirepl, content).decode('ascii', 'ignore').splitlines()
  self.protocol.privmsg(self.channel, "%s" % " ".join(ascii_string))

self.register_action('quote', quote)

