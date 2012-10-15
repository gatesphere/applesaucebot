def quote(self, username, cmdtime, command, args):
  import urllib.request, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  gist_count = 3
  args = " ".join(args)
  url = 'http://www.iheartquotes.com/api/v1/random'
  content = urllib.request.urlopen(url).read().decode("utf-8", 'ignore')
  reg = re.compile(r'\\x(\w{2})')
  ascii_string = reg.sub(asciirepl, content).splitlines()
  ascii_string = " ".join(ascii_string).replace("&quot;", "\"").replace('\t', " ")
  self.protocol.privmsg(self.channel, "%s" % ascii_string)

self.register_action('quote', quote)

