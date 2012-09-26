def define(self, username, cmdtime, command, args):
  import json, urllib, binascii

  def asciirepl(match):
    s = match.group()
    return '\\u00' + match.group()[2:]
 
  if args:
    defn_count = 3
    for word in args:
      url = 'http://www.google.com/dictionary/json?callback=a&q=' + word + '&sl=en&tl=en&restrict=pr,de&client=te' 
      content = urllib.urlopen(url).read()[2:-10]
      reg = re.compile(r'\\x(\w{2})')
      ascii_string = reg.sub(asciirepl, content).decode('ascii', 'ignore')
      data = json.loads(ascii_string)
      if 'primaries' in data:
        for bunch in data['primaries']:
          for i in range(len(bunch['entries'])):
            if bunch['entries'][i]['type'] != 'meaning': continue          
            meaning = bunch['entries'][i]['terms'][0]['text']
            self.protocol.privmsg(self.channel, "%s - %s (from google)" % (word, meaning))
            defn_count -= 1
            if defn_count == 0: return
            time.sleep(1)
      if 'webDefinitions' in data:
        for entry in data['webDefinitions'][0]['entries']:
          meaning = entry['terms'][0]['text']
          source = entry['terms'][1]['text']
          source = source[source.find(">")+1:source.rfind("<")]
          self.protocol.privmsg(self.channel, "%s - %s (from %s)" % (word, meaning, source))      
          defn_count -= 1
          if defn_count == 0: return
          time.sleep(1)
      if defn_count == 3:
        self.protocol.privmsg(self.channel, "I couldn't find a definition for %s." % word)
  else:
    self.protocol.privmsg(self.channel, "%s, I need at least one word to define!" % username)

self.register_action('define', define)

