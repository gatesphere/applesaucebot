## applesaucebot
## Jacob Peck
## 

# standard lib
import traceback
import sys
import os
import time
import pickle
import random
import re
import logging

# botlib
import botlib

# configuration file
config_file = 'bot.conf'
log_file = 'bot.log'

class ApplesauceBot(botlib.Bot):
  commands = { }
  moduledir = 'modules'
  regex = ''
  
  def __init__(self, server, channel, nick, password=None, admin_password=None):
    """ constructor, builds an IRC bot with the correct configuration, 
        connects to a channel, loads commands
    """
    logging.basicConfig(filename=log_file, level=logging.DEBUG)
    logging.info('Bot starting up at %s' % time.strftime("%H:%M:%S %Y-%m-%d", time.localtime()))
    self.admin_pw = admin_password
    self.load_commands()
    botlib.Bot.__init__(self, server, 6667, channel, nick)
    if password != None:
      self.protocol.privmsg("nickserv", "identify %s" % password)
    logging.info('Connected to channel %s with nick %s' % (self.channel, self.nick))
    self.regex = regex = re.compile("^(\?|%s:|%s,)" % (self.nick, self.nick), re.IGNORECASE)

  def __actions__(self):
    """ action dispatcher """
    botlib.Bot.__actions__(self)
    logging.info("Recieved data = %s" % self.data)
    if botlib.check_found(self.data, "identified for"):
      logging.info('Identified for %s' % self.nick)
    if self.check_found_regex(self.get_message_data(), self.regex):
      username = self.get_username()
      cmdtime = time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
      d = self.get_message_data().lower().split()
      command, args = None, None 
      try:
        if d[0].startswith(self.nick.lower()):
          command, args = d[1], d[2:]
        else:
          command, args = d[0][1:], d[1:]
      except:
        self.unknown_command(username, cmdtime, None, None)
      logging.info("%s - %s is trying to get my attention: %s" % (cmdtime, username, self.data))
      if command:
        self.do_command(username, cmdtime, command.lower(), args)
    if self.joined:
      self.check_joined()
    
  def check_joined(self):
    logging.info("Check joined...")
    #if not self.joined:
    #  return
    self.protocol.send("WHO %s" % self.channel)
    info = ""
    while not botlib.check_found(info, "End of /WHO list"):
      info += self.protocol.recv()
      logging.info(info)
    if not botlib.check_found(info, "H :0  %s" % self.nick):
      self.protocol.join(self.channel)

  def register_action(self, name, fn):
    ''' add a command '''
    self.commands[name] = fn

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
    self.commands['reload'] = self.reload
    lst = os.listdir(self.moduledir)
    for m in lst:
      s = os.path.abspath(self.moduledir) + os.sep + m
      exec(open(s).read())
      logging.info('Loading module: %s' % s)
    
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
      logging.info(traceback.format_exc())
      self.unknown_command(username, cmdtime, command, args)
      return
    
  def unknown_command(self, username, cmdtime, command, args):
    logging.info('%s - Unknown command %s %s from user %s' % (cmdtime, command, args, username))
    self.protocol.privmsg(username, "%s: I do not understand %s %s" % (username, command, args))

if __name__ == "__main__":
  """ run the bot, reading in configuration from a config file """
  f = open(config_file, 'rb')
  c = pickle.load(f)
  f.close()
  ApplesauceBot(c[0], c[1], c[2], c[3], c[4]).run()

