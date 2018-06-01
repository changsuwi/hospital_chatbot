# coding=utf-8

from ..json_fb import json_mainbutton, json_message
from db import upload_flag


def postback_control(messaging_event, sender_id):
    # Get start

    if messaging_event["postback"]["payload"] == 'GET_STARTED_PAYLOAD':
        upload_flag(0, sender_id)
        json_message(sender_id, "您好，我是醫護助理聊天機器人，請問需要什麼服務呢?")
        json_mainbutton(sender_id)

    elif messaging_event["postback"]["payload"] == 'main_button1':
        upload_flag(1, sender_id)
        json_message(sender_id, "您的身體哪裡不舒服?")

    elif messaging_event["postback"]["payload"] == 'main_button2':
        upload_flag(2, sender_id)

    elif messaging_event["postback"]["payload"] == 'main_button3':
        upload_flag(3, sender_id)

    elif messaging_event["postback"]["payload"] == 'main_button4':
        upload_flag(4, sender_id)

    elif messaging_event["postback"]["payload"] == 'main_button5':
        upload_flag(5, sender_id)
