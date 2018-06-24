# coding=utf-8

from ..json_fb import typingon_json, json_message, json_mainbutton
from .db import get_flag, upload_flag, match_sym
from .kcom_analy import kcom_analy
from .kcom_replace import kcom_replace


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

                # Guan Wen's code
                replace_mes = kcom_replace(message_text)
                print(replace_mes)
                total = kcom_analy(replace_mes)
                sym_list = []
                for period in total:
                    # add user's sym in list
                    sym_list = sym_list + period['sym']

                # do match_sym and return the meantime in hospital and Cresult
                result, meantime = match_sym(sym_list)
                if result != {}:
                    res_str = "平均在急診室的時間為" + str(meantime * 24) + "小時" + "\n"
                    for key, value in result.items():
                        # if probobility is small, ignore it
                        if value > 0.01:
                            res_str = res_str + key + ":" + str(value) + '\n'
                    json_message(sender_id, res_str)
