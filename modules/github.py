def github(self, username, cmdtime, command, args):
  import json, urllib.request, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  if args:
    repo_count = 3
    args = " ".join(args)
    url = 'https://api.github.com/legacy/repos/search/' + args
    content = urllib.request.urlopen(url).read().decode("utf-8")
    reg = re.compile(r'\\x(\w{2})')
    ascii_string = reg.sub(asciirepl, content)
    data = json.loads(ascii_string)['repositories']
    for repo in data:
      r_name = repo['name']
      r_language = repo['language']
      r_owner = repo['owner']
      r_description = repo['description']
      r_url = "https://github.com/%s/%s" % (r_owner, r_name)
      self.protocol.privmsg(self.channel, "%s - language: %s - owner: %s - %s" % (r_name, r_language, r_owner, r_description))
      self.protocol.privmsg(self.channel, "%s" % r_url)
      repo_count -= 1
      if repo_count == 0:
        return
      time.sleep(1)
    if repo_count == 3:
      self.protocol.privmsg(self.channel, "I couldn't find any repos for %s." % args)
  else:
    self.protocol.privmsg(self.channel, "%s, I need at least a keyword to search!" % username)

self.register_action('github', github)

