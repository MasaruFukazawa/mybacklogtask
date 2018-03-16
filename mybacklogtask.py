#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json


API_URL = "" # 課題取得URL
API_KEY = "" # APIキー

USERID  = "" # 対象ユーザID

ISSUES_NUM = 100  # 件名

STATUSES = [
    1, # 未対応
    2, # 処理中
    3, # 処理済み
    4, # 完了
]

params = {
    "apiKey": API_KEY,
    "assigneeId[]": USERID,
    "statusId[]": STATUSES,
    "count": ISSUES_NUM,
    "sort": "issueType",
}

def main():
    """
    """
    r = requests.get(API_URL, params=params)

    for issue in json.loads(r.content):
        print(issue["issueKey"] + " " + issue["summary"])
    

if __name__ == "__main__":
    main()
