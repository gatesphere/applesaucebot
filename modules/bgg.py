def bgg(self, username, cmdtime, command, args):
  import urllib.request, urllib.parse, binascii
  import xml.etree.ElementTree as etree

  if args:
    baseurl = "http://www.boardgamegeek.com/xmlapi/" 
    searchurl = baseurl + "search?search="
    gameurl = baseurl + "boardgame/"
     
    gamecount = 3
    arg = " ".join(args).strip()
    searchurl = searchurl + urllib.parse.quote(arg) 
    idlist = urllib.request.urlopen(searchurl).read().decode("utf-8", 'ignore')
    tree = etree.fromstring(idlist)
    ids = tree.findall('boardgame')
    gameids = []
    for id in ids:
      gameids.append(id.attrib["objectid"])
      gamecount = 3 - len(gameids)
      if gamecount <= 0: break
    
    if gamecount == 3:
      self.protocol.privmsg(self.channel, "%s, I couldn't find any games for %s" % (username, arg))
      return None
    
    gameurl = gameurl + urllib.parse.quote(",".join(gameids))
    gamelist = urllib.request.urlopen(gameurl).read().decode("utf-8", 'ignore')
    tree = etree.fromstring(gamelist)
    games = tree.findall('boardgame')
    for game in games:
      name = game.find("name").text
      desc = game.find("description").text[:300] + " ..."
      link = "http://boardgamegeek.com/" + game.attrib["objectid"]
      self.protocol.privmsg(self.channel, "%s -- %s (on bgg: %s)" % (name, desc, link))
  else:
    self.protocol.privmsg(self.channel, "%s, I need a name to search!" % username)

self.register_action('bgg', bgg)

