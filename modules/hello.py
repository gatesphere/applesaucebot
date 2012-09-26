def hello(self, username, cmdtime, command, args):
  """ greet the user """
  self.protocol.privmsg(self.channel, "Hello there, %s!" % username)

self.register_action('hello', hello)
self.register_action('hai?', hello)
self.register_action('hai', hello)
self.register_action('herro', hello)
