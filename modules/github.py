def github(self, username, cmdtime, command, args):
  import json, urllib, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  if args:
    repo_count = 3
    args = " ".join(args)
    url = 'https://api.github.com/legacy/repos/search/' + args
    content = urllib.urlopen(url).read()
    reg = re.compile(r'\\x(\w{2})')
    ascii_string = reg.sub(asciirepl, content).decode('ascii', 'ignore')
    data = json.loads(ascii_string)['repositories']
    for repo in data:
      r_name = repo['name']
      r_language = repo['language']
      r_owner = repo['owner']
      r_description = repo['description']
      self.protocol.privmsg(self.channel, "%s - language: %s - owner: %s - %s" % (r_name, r_language, r_owner, r_description))
      repo_count -= 1
      if repo_count == 0:
        return
      time.sleep(1)
    if repo_count == 3:
      self.protocol.privmsg(self.channel, "I couldn't find any repos for %s." % args)
  else:
    self.protocol.privmsg(self.channel, "%s, I need at least a keyword to search!" % username)

self.register_action('github', github)

