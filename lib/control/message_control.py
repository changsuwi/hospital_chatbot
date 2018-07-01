# coding=utf-8

from ..json_fb import typingon_json, json_message, json_mainbutton, json_photo
from .db import get_flag, upload_flag, match_sym
from .kcom_analy import kcom_analy
from .kcom_replace import kcom_replace
import matplotlib.pyplot as plt
from .imgur import upload_photo


def message_control(messaging_event, sender_id):
    if("text" in messaging_event["message"]):
        message_text = messaging_event["message"][
            "text"]  # the message's text
        print(sender_id)  # test
        if message_text == u'hello' or message_text == u'Hello':
            upload_flag(0, sender_id)
            json_message(
                sender_id, "您好，我是醫護助理聊天機器人，我可以提供快速有效的急診病情諮詢與結果比例，也可以幫您轉接醫師諮詢，請問需要什麼服務呢?")
            json_mainbutton(sender_id)
        else:
            if "quick_reply" in messaging_event["message"]:
                if messaging_event["message"]["quick_reply"]["payload"] == "main_button1":
                    upload_flag(1, sender_id)
                    json_message(sender_id, "您的身體哪裡不舒服?")
                elif messaging_event["message"]["quick_reply"]["payload"] == 'main_button2':
                    upload_flag(2, sender_id)
                    json_message(sender_id, "聯絡醫師中，請稍候")

            elif get_flag(sender_id) == 1:
                json_message(
                    sender_id, "目前正在搜查比對資料庫 請稍後")

                # Guan Wen's code
                replace_mes = kcom_replace(message_text)
                print(replace_mes)
                total = kcom_analy(replace_mes)
                print("finish analy")
                print(total)
                sym_list = []
                key_list = []
                value_list = []
                for period in total:
                    # add user's sym in list
                    sym_list = sym_list + period['sym']
                # do match_sym and return the meantime in hospital and Cresult
                result, meantime = match_sym(sym_list)
                if result != {}:
                    res_str = "平均在急診室的時間為" + \
                        str(format(meantime * 24, 3)) + \
                        "小時" + "\n" + "急診後結果比例分布\n"
                    count = 1
                    for key, value in result.items():
                        # if probobility is small, ignore it
                        if value > 0.01:
                            key_list.append(str(count))
                            value = format(value, 3)
                            value_list.append(value * 100)
                            res_str = res_str + str(count) + "." + key + ":" + str(value * 100) + "%" + '\n'
                            count = count + 1
                    plot(key_list, value_list, sender_id)
                    json_message(sender_id, res_str)


def plot(key_list, value_list, sender_id):
    plt.figure(figsize=(6, 9))  # 调节图形大小
    labels = key_list  # 定义标签
    sizes = value_list  # 每块值
    explode = None  # 将某一块分割出来，值越大分割出的间隙越大
    patches, text1, text2 = plt.pie(sizes,
                                    explode=explode,
                                    labels=labels,
                                    autopct='%f%%',  # 数值保留固定小数位
                                    shadow=False,  # 无阴影设置
                                    startangle=90,  # 逆时针起始角度设置
                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
    # patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.savefig('testplot.png')
    url = upload_photo('./testplot.png')
    json_photo(sender_id, url)


def format(f, n):
    if round(f) == f:
        m = len(str(f)) - 1 - n
        if f / (10**m) == 0.0:
            return f
        else:
            return float(int(f) / (10**m) * (10**m))
    return round(f, n - len(str(int(f)))) if len(str(f)) > n + 1 else f
