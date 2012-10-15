oswegocsa-applesaucebot
=======================

An IRC bot for Freenode #OswegoCSA


How to use
----------
First, make a configuration file:

    $ python3 makeconf.py

  - `password` is the password that will be sent to NickServ after login.
  - `admin` is the administrator password.

Then, start the bot:

    $ python3 applesaucebot.py &

There's a logfile created at bot.log, which logs most communications that the bot recieves.

Issuing commands:
-----------------
applesaucebot responds to commands in 3 formats, either `?command args`, `botnick: command args`, or `botnick, command args`, where `botnick` is the bot's nick (provided in the configuration file), `command` is a command, and `args` is a space separated list of arguments to the command.

Admin commands:
---------------
Admin commands require the admin password to execute.  Send this as the first argument to the command.  It's advised to send these in a private message to the bot.

    die - shut down the bot
    reload - reload all modules

Enjoy.
