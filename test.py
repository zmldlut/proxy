#!/usr/bin/env python
# coding=utf-8
import requests
import time
import random

f = open("./proxies.txt", "r")

lines = f.readlines()

for line in lines:
    line = line.strip("\n")
    try:
        proxies = {'http': "http://" + line, 'https':"https://" + line}
        res = requests.get("http://www.icanhazip.com", proxies = proxies)
        print(res.text)
        h = random.uniform(0,10)
        m = random.uniform(0,60)
        ti = 10 * h + m
        print(ti)
        time.sleep(ti)
    except:
        print(proxies)
