import os
import sys
import time
import re

def do_preflight_checks():
    if not os.path.isfile('slackbot.conf'):
        gen_conf_file()
        print("A configuration file has been generated at \'./slackbot.conf\'."
                "Please fill this out and start the bot again.")
        sys.exit(0)

def gen_conf_file():
    new_conf = open("slackbot.conf", "w")
    new_conf.write("[SLACK_CONF]\nSLACK_BOT_TOKEN=\"\"\n" \
                    "SLACK_SIGN_SECRET=\"\"\n\n" \
                    "[JIRA_CONF]\nJIRA_URL=\"\"\nJIRA_PREFIXES=\"\"\n")
