import os
import sys
import time
import re
from slack import SlackClient

def do_preflight_checks():
    if not os.path.isfile('slackbot.conf'):
        gen_conf_file()
        print("A configuration file has been generated at \'./slackbot.conf\'."
                "Please fill this out and start the bot again.")
        sys.exit(0)