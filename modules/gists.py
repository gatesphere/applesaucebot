def gists(self, username, cmdtime, command, args):
  import json, urllib.request, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  if args:
    gist_count = 3
    args = " ".join(args)
    url = 'https://api.github.com/users/' + args + '/gists'
    content = urllib.request.urlopen(url).read().decode('utf-8')
    reg = re.compile(r'\\x(\w{2})')
    ascii_string = reg.sub(asciirepl, content)
    data = json.loads(ascii_string)
    if str(data).find('Not Found') != -1:
      self.protocol.privmsg(self.channel, "I couldn't find any gists for %s." % args)
      return
    for gist in data:
      g_description = gist['description']
      g_url = gist['html_url']
      self.protocol.privmsg(self.channel, "%s - %s" % (g_description, g_url))
      gist_count -= 1
      if gist_count == 0:
        return
      time.sleep(1)
    if gist_count == 3:
      self.protocol.privmsg(self.channel, "I couldn't find any gists for %s." % args)
  else:
    self.protocol.privmsg(self.channel, "%s, I need a username to search!" % username)

self.register_action('gists', gists)

