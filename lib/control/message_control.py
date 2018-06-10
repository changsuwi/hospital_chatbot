# coding=utf-8

from ..json_fb import typingon_json, json_message, json_mainbutton
from db import get_flag, upload_flag
from kcom_analy import kcom_analy


def message_control(messaging_event, sender_id):
    if("text" in messaging_event["message"]):
        message_text = messaging_event["message"][
            "text"]  # the message's text
        print(sender_id)  # test
        if message_text == u'hello' or message_text == u'Hello':
            upload_flag(0, sender_id)
            json_message(sender_id, "您好，我是醫護助理聊天機器人，請問需要什麼服務呢?")
            json_mainbutton(sender_id)
        else:
            if "quick_reply" in messaging_event["message"]:
                if messaging_event["message"]["quick_reply"]["payload"] == "main_button1":
                    upload_flag(1, sender_id)
                    json_message(sender_id, "您的身體哪裡不舒服?")

            elif get_flag(sender_id) == 1:
                json_message(
                    sender_id, "目前正在搜查比對資料庫 請稍後")
                total = kcom_analy(message_text)
                for period in total:
                    print('時間： %s' % period['time'].encode('utf-8'))
                    print('症狀： %s' % ','.join(period['sym']).encode('utf-8'))
                print('\n')

                '''
                接冠文的code
                '''
