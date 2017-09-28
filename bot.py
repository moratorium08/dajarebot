#!/home/ubuntu/.pyenv/versions/slackbot/bin/python
import time
import sys
import os
from dajare import *
from secret import token, channel, user_name

from slackclient import SlackClient

icon_url = "https://pbs.twimg.com/profile_images/874516687650906112/4AI_gWjh_400x400.jpg"

api_interface = SlackClient(token)
if api_interface.rtm_connect():
    while True:
        data = api_interface.rtm_read()
        if len(data) >= 1 and "text" in data[0]:
            try:
                if "subtype" in data[0] and data[0]["subtype"] == "bot_message":
                    continue
                if "C04G7TLB7" != data[0]["channel"]:
                    continue
                h, s =  get_dajare(data[0]["text"])
                if len(h) > 0:
                    print(api_interface.api_call("chat.postMessage",
                        username=user_name, channel=channel, text=s,
                        icon_url=icon_url))
            except:
                print("error")


if __name__ == '__main__':
    pass
