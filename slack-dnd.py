#
# Copyright (c) 2022 Furkan Pehlivan
#

import requests
import rumps
from pathlib import Path
import os
import json

# Initial setup
home = str(Path.home())
slack_dnd_dir = Path(home + "/.slack-dnd")
conf = Path(home + "/.slack-dnd/config.json")

# Check if config directory exists
if slack_dnd_dir.is_dir():
    pass
else:
    os.makedirs(slack_dnd_dir)

# Check if config file exists
if conf.is_file():
    pass
else:
    # Create config file
    window = rumps.Window()
    window.icon = "icon.png"
    window.message = 'Welcome to Slack-DND 💤\n\nPlease enter your oauth token:'
    token = window.run()
    window.add_button('Cancel')
    if token.text == "":
        rumps.alert(message='No token entered. Please try again.', icon_path='./icon.png', title='Slack-DND Error')
        rumps.quit_application()
    else:
        resp = requests.get("https://slack.com/api/dnd.info", headers={'Authorization': 'Bearer ' + token.text})
        print(resp.json().get('ok'))
        if resp.json().get('ok') == True:
            print(resp.status_code)
            with open(conf, "w") as f:
                conf_data = "{" + '"oauth_token": "' + token.text + '"' + "}"
                f.write(conf_data)
        else:
            rumps.alert(message='Invalid token. Please try again.', icon_path='./icon.png',  title='Slack-DND Error')
            rumps.quit_application()

# Read config file
with open(home + "/.slack-dnd/config.json") as conffile:
	data = json.load(conffile)

oauth_token = data["oauth_token"]

# Check if token is valid and broken or not
resp = requests.get("https://slack.com/api/dnd.info", headers={'Authorization': 'Bearer ' + oauth_token})
if resp.json().get('ok') == True:
    pass
else:
    rumps.alert(message='Invalid token. Please try again.', icon_path='./icon.png',  title='Slack-DND Error')
    rumps.quit_application()

class SlackDnd(object):

    def __init__(self):
        self.config = {
            "app_name": "Slack DND",
            "icon": "icon.png",
            "quit_button": "❌",
            "dnd_on": "🔕",
            "dnd_off": "🔔"
        }

        self.app = rumps.App(name=self.config["app_name"], icon=self.config["icon"], quit_button=self.config["quit_button"])
        self.dnd_on_button = rumps.MenuItem(title=self.config["dnd_on"], callback=self.dnd_on)
        self.dnd_off_button = rumps.MenuItem(title=self.config["dnd_off"], callback=self.dnd_off)
        self.app.menu = [self.dnd_on_button, self.dnd_off_button]

    def dnd_on(self, callback):
        resp = requests.post("https://slack.com/api/dnd.setSnooze", headers={
                            "pretty": "1",
                            "Authorization": "Bearer " + oauth_token
                            }, params={"num_minutes": 60})
                            # TODO: Add custom time
        if resp.json().get('ok') == True:
            rumps.notification(title='Slack DND', subtitle='', message='DND is on for 60 minutes', icon='./icon.png')
        else:
            rumps.alert(message='Something went wrong\n' + resp.text, icon_path='./icon.png',  title='Slack-DND Error')
    
    def dnd_off(self, callback):
        resp = requests.post("https://slack.com/api/dnd.endDnd", headers={
                            "pretty": "1",
                            "Authorization": "Bearer " + oauth_token
                            })
        if resp.json().get('ok') == True:
            rumps.notification(title="Slack DND", subtitle="", message="DND is off", icon="./icon.png")
        else:
            rumps.alert(message='Something went wrong\n' + resp.text, icon_path='./icon.png',  title='Slack-DND Error')

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = SlackDnd()
    app.run()