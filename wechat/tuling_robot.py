#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
When got text message from wechat user, reply with tuling robot.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: tuling_robot.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Sun 16 Oct 2016 01:53:46 AM EDT

DETAILS:
    http://www.tuling123.com
    Read the doc from tuling website.
    Use json format and HTTP POST to post data to tuling and return data with json format.

    Send to tuling:
        {
            "key": "APIKEY",
            "info": "Your content",
            "userid": "wechat user openid, not support for booking account."
        }

    Receive from tuling:
        {
            "code": "your code",
            "text": "your content",
            "url": "url for link",

            "list": [
            {
                "article": "article1 for news",
                "source": "news from where",
                "icon": "",
                "detailurl": "url for news"
            },
            ...
            ],

            "list": [
            {
                "name": "food name for cookbook",
                "icon": "",
                "info": "food information.",
                "detailurl": "url for cookbook"
            },
            ...
            ]
        }

    code means what kind of message you got from tuling:
        100000: text
        200000: link
        302000: news
        308000: cookbok
"""
import json

# TPL
import requests

API = "http://www.tuling123.com/openapi/api"
APIKEY = "b4987475ebed4c4c9684237ffc1d6dc0"
SECRET = "6eaf872d2311e5ab"


def tuling_robot(content):
    s = requests.session()
    data = {"key": APIKEY, "info": content}
    data = json.dumps(data)
    response = s.post(API, data=data)
    resp_data = json.loads(response.text)
    # resp_data = eval(response.text)
    print(resp_data)
    code = resp_data['code']
    text = resp_data['text']
    print(code)
    print(text)
    if code == 100000:
        resp_content = resp_data['text']
    elif code == 200000:
        resp_content = resp_data['text'] + resp_data['url']
    elif code == 302000:
        resp_content = resp_data['text'] + resp_data['list'][0]['article'] + resp_data['list'][0]['source'] + resp_data['list'][0]['detailurl']
    elif code == 308000:
        resp_content = resp_data['text'] + resp_data['list'][0]['name'] + + resp_data['list'][0]['info'] + resp_data['list'][0]['detailurl']
    else:
        resp_content = "听不懂鸟语，请说人话"
    return resp_content


def handle_tuling_robot(content):
    try:
        resp_content = tuling_robot(content)
    except Exception:
        resp_content = "别瞎BB"
    finally:
        return resp_content

if __name__ == "__main__":
    print(handle_tuling_robot("天气", ""))