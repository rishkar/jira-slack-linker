import os
import sys
import configparser

def do_preflight_checks():
    # Make sure our slackbot.conf and all its required values exist
    if not os.path.isfile('slackbot.conf'):
        gen_conf_file()
        print("A configuration file has been generated at \'./slackbot.conf\'."
            " Please fill this out and start the bot again.")
        sys.exit(0)
    else:
        conf_parser = configparser.ConfigParser()
        conf_parser.read('slackbot.conf')

        if not ('SLACK_CONF' in conf_parser or 'JIRA_CONF' in conf_parser):
            error("Invalid slackbot.conf. Either fix the errors, or delete"
                " the file and let this program regenerate it.")
        
        if not (conf_parser['SLACK_CONF']['SLACK_BOT_TOKEN']:
            error("Missing SLACK_BOT_TOKEN value in slackbot.conf. Please"
                " remediate and restart this program.")
        if not (conf_parser['SLACK_CONF']['SLACK_SIGN_SECRET']:
            error("Missing SLACK_SIGN_SECRET value in slackbot.conf. Please"
                " remediate and restart this program.")
        if not (conf_parser['JIRA_CONF']['JIRA_URL']:
            error("Missing JIRA_URL_TOKEN value in slackbot.conf. Please"
                " remediate and restart this program.")
        if not (conf_parser['JIRA_CONF']['JIRA_PREFIXES']:
            warning("Missing SLACK_BOT_TOKEN value in slackbot.conf. I will"
                " default to \"/([A-Z]+)-([0-9]+)/g\"")


        




def gen_conf_file():
    new_conf = open("slackbot.conf", "w")
    new_conf.write("[SLACK_CONF]\nSLACK_BOT_TOKEN=\"\"\n" \
                    "SLACK_SIGN_SECRET=\"\"\n\n" \
                    "[JIRA_CONF]\nJIRA_URL=\"\"\nJIRA_PREFIXES=\"\"\n")
