# 環境
1. python 2.7
2. mongodb
3. ngrok
# 使用方法
1. 在localhost開mongodb，匯入最新版本的csv
2. 把匯入的資料表取名為kcom
3. 開啟終端機，cd到hospital_chatbot，執行指令來開啟ngrok
```
./ngrok http 5000
```
4. ngork已開啟，另開新的終端機，cd到hospital_chatbot，接著執行app.py
ˋˋˋ
python app.py
ˋˋˋ
5. 程式正常執行在port 5000，回到ngrok，copy web interface欄位的網址，ngrok會生成兩個tunnel url
6. 點擊 https的url，看到hello world 代表app.py正常執行
7. 進入facebook for developer，點擊我的應用程式，選擇hospital_chatbot，左邊有一個webhook按鈕，點擊進去
8. 按下edit subscription 把ngrok 生成的 https 網址貼到回呼網址的欄位， 把我們messenger群組的名字貼到驗證權杖欄位，按下驗證並儲存
9. 如果沒跳出任何錯誤訊息，則現在就可以從messenger跟chatbot做互動
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
