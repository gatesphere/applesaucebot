def wiki(self, username, cmdtime, command, args):
  import wikipedia

  if args:
    arg = " ".join(args)
    result_count = 3
    summary_length = 250
    results = wikipedia.search(arg,results=result_count)
    if len(results) == 0:
      self.protocol.privmsg(self.channel, "No Wikipedia results for '%s'!" % arg)
    else:
      for r in results:
        page = wikipedia.page(r)
        summary = page.summary[:summary_length] + '...'
        name = page.title
        url = page.url
        self.protocol.privmsg(self.channel, "%s -- %s (%s)" % (name, summary, url))
  else:
    self.protocol.privmsg(self.channel, "%s, I need something to search!" % username)

self.register_action('wiki', wiki)

