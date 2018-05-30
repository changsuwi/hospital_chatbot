# chatbot 架構
## app.py
主程式
## lib
### control
#### db.py
接db，目前只保留上傳使用者目前的操作狀態(flag)
#### imgur.py
圖床，如果改到老師的vm，這部分可砍掉
#### message_control.py
處理message類別的事件，未來可能會在這裡接冠文的斷詞跟分類系統，並將結果套到json_fb的function
#### postback_control.py
處理postback類別的事件(ex.快速回復)，並將結果套到json_fb的function
### json_fb.py
吃參數並打包成json，並將json套到sendtofb的function
### sendtofb.py
與messenger api 溝通，傳送json
