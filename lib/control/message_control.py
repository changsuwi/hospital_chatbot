# coding=utf-8

from ..json_fb import typingon_json, json_message
from db import get_flag


def message_control(messaging_event, sender_id):
    if("text" in messaging_event["message"]):
        message_text = messaging_event["message"][
            "text"]  # the message's text
        print(sender_id)  # test
        flag = get_flag(sender_id)
        if message_text == u'hello':
            json_message(
                sender_id, "hello")
        elif flag == 1:
            json_message(sender_id, "資料庫批配中，請稍後")
            '''
            接冠文的code
            '''
