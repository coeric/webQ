#-*- coding:utf-8 -*-
import requests
import json

#律師個人資料API
url="https://api.tba.org.tw/FindLawyer/6669"


res=requests.get(url)

#把回應轉成json格式做判讀
data=json.loads(res.content)

#列出各欄位及資料
for row in data:
    print row,data[row]