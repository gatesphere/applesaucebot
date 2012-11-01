def acronym(self, username, cmdtime, command, args):
  import urllib.request, urllib.parse, binascii
  import xml.etree.ElementTree as etree

  if args:
    baseurl = "http://acronyms.silmaril.ie/cgi-bin/uncgi/xaa?"
    defcount = 3
    arg = "".join(args).strip()
    searchurl = baseurl + urllib.parse.quote(arg) 
    idlist = urllib.request.urlopen(searchurl).read().decode("utf-8", 'ignore')
    tree = etree.fromstring(idlist)
    ids = tree.find('found').findall('acro')
    acros = []
    for id in ids:
      acros.append(id.find("expan").text)
      defcount -= 1
      if defcount == 0:
        break
 
    if defcount == 3:
      self.protocol.privmsg(self.channel, "%s, I couldn't find any acronym expansions for %s" % (username, arg))
      return None
  
    for acro in acros:  
      self.protocol.privmsg(self.channel, "%s -- %s" % (arg, acro))
  else: 
    self.protocol.privmsg(self.channel, "%s, I need a name to search!" % username)

self.register_action('acronym', acronym)

