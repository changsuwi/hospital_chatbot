# coding=utf-8

from ..json_fb import typingon_json, json_message


def message_control(messaging_event, sender_id):
    if("text" in messaging_event["message"]):
        message_text = messaging_event["message"][
            "text"]  # the message's text
        print(sender_id)  # test
        if message_text == u'hello':
            json_message(
                sender_id, "hello")
