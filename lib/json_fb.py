# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:50:20 2017
json_fb 此模組主要存放通用的json格式與打包
例如使用者輸入json ，template打包 ， main button 的json ，message的打包
@author: vicharm
"""
from .sendtofb_log import sendtofb, log
import json


def typingon_json(recipient_id):
    #  construct typing on json
    log("sending  typingon to {recipient}".format(recipient=recipient_id))
    data = json.dumps({"recipient": {"id": recipient_id},
                       "sender_action": "typing_on"})
    sendtofb(data)


def json_template(recipient_id):
    template = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                    ]
                }
            }
        }
    }
    return template


def json_mainbutton(recipient_id):
    log("sending mainbutton to {recipient}".format(recipient=recipient_id))
    data = json.dumps(
        {
            "recipient":
            {
                "id": recipient_id
            },
            "message":
            {
                "text": "你要選擇哪個呢？",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "病情諮詢",
                        "payload": "main_button1"
                    },
                    {
                        "content_type": "text",
                        "title": "與醫師對話",
                        "payload": "main_button2"
                    }
                ]
            }
        }
    )
    sendtofb(data)


def json_photo(recipient_id, url):
    log("sending photo to {recipient}".format(recipient=recipient_id))
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url
                }
            }
        }
    })
    sendtofb(data)


def json_message(recipient_id, message_text):  # construct message json

    log("sending message to {recipient}: {text}".format(
        recipient=recipient_id, text=message_text))
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    sendtofb(data)
