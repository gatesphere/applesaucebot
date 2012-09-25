## applesaucebot
## Jacob Peck
## 

# standard lib
import sys
import os
import time
import pickle
import random
import re
import types

# botlib
import botlib

# configuration file
config_file = 'bot.conf'

class ApplesauceBot(botlib.Bot):
  commands = { }
  moduledir = 'modules'
  regex = ''
  
  def __init__(self, server, channel, nick, password=None, admin_password=None):
    """ constructor, builds an IRC bot with the correct configuration, 
        connects to a channel, loads commands
    """
    self.admin_pw = admin_password
    self.load_commands()
    botlib.Bot.__init__(self, server, 6667, channel, nick)
    if password != None:
      self.protocol.privmsg("nickserv", "identify %s" % password)
    #print "Connected to channel %s with nick %s" % (self.channel, self.nick)
    self.regex = regex = re.compile("^(\?|%s:|%s,)" % (self.nick, self.nick), re.IGNORECASE)

  def __actions__(self):
    """ action dispatcher """
    botlib.Bot.__actions__(self)
    #print self.data
    #if botlib.check_found(self.data, "identified for"):
      #print "Identified for %s" % self.nick
    if self.check_found_regex(self.get_message_data(), self.regex):
      username = self.get_username()
      cmdtime = time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
      d = self.get_message_data().split()
      if d[0].startswith(self.nick):
        command, args = d[1], d[2:]
      else:
        command, args = d[0][1:], d[1:]
      #print "%s is trying to get my attention: %s" % (username, self.data)
      self.do_command(username, cmdtime, command.lower(), args)

  def check_found_regex(self, string, regex):
    """ check if string matches regex """
    if string != None:
      if re.search(regex, string) != None:
        return True
    return False

  def get_message_data(self):
    """ gets the "data" portion of the message """
    d = self.data
    d = d.split(":", 2)
    return (d[2] if len(d) == 3 else None)

  def load_commands(self):
    """ loads the commands into the dictionary """
    self.commands = { }
    lst = os.listdir(self.moduledir)
    for m in lst:
      s = os.path.abspath(self.moduledir) + os.sep + m
      execfile(s)
    self.commands['reload'] = self.reload
    
  def reload(self, ignorethis, username, cmdtime, command, args):
    if args and args[0] == self.admin_pw:
      self.load_commands()
      self.protocol.privmsg(self.channel, "%s: Reloaded all modules." % username)
    else:
      self.protocol.privmsg(self.channel, "%s: I can't let you do that." % username)

  def do_command(self, username, cmdtime, command, args):
    """ dispatch to a command by name """
    try:
      c = self.commands[command]
      c(self, username, cmdtime, command, args)
    except:
      self.unknown_command(username, cmdtime, command, args)
      return
    
  def unknown_command(self, username, cmdtime, command, args):
    self.protocol.privmsg(self.channel, "%s: I do not understand %s %s" % (username, command, args))

if __name__ == "__main__":
  """ run the bot, reading in configuration from a config file """
  f = open(config_file, 'r')
  c = pickle.load(f)
  f.close()
  ApplesauceBot(c[0], c[1], c[2], c[3], c[4]).run()

