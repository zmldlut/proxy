#!/usr/bin/env python
# coding=utf-8
import requests
import threading
import random
import time
import os

import selenuim_test

URL_PROXYS = "http://127.0.0.1:5010/get_all"

PROXYS = []
TIME = 60 * 5
PROXIES_FILE = "./proxies.txt"
BUSSINES_KEYS = ["大树", "专业外墙瓷砖清洗"]

def get_proxys(url = URL_PROXYS):
    
    f = open(PROXIES_FILE, "w")

    r = requests.get(url)
    lines = r.text.split("\n")
    for line in lines:
        if "\"" in line:
            proxy = line.strip()[1:-2]
            PROXYS.append(proxy)
            f.write(proxy + "\n")

    print(PROXYS)
    f.close()
    return PROXYS

def timer_get_proxys(url = URL_PROXYS, time = 60 * 5):
    global timer
    get_proxys(url)
    timer = threading.Timer(time, timer_get_proxys,[url, time])
    timer.start()
    


def get_proxies(proxys = PROXYS):
    proxies = []
    for proxy in proxys:
        proxies.append({'http': "http://" + proxy, 'https': "https://" + proxy})
    return proxies

def refresh_urls(proxies):
    list_count = []
    for proxy in proxies:
        try:
            #r = requests.get(url, proxy)
            #r = selenuim_test.detect_url(proxy, url)
            for keys in BUSSINES_KEYS:
                os.system("python selenuim_test.py -b " + keys + " -p " + proxy )
            #if r == 200:
            #    count += 1
        except:
            print(proxy)
            print("filed!")

    return list_count
    

#timer = threading.Timer(1, timer_get_proxys, [URL_PROXYS, TIME])
#timer.start()

if __name__ == "__main__":
    
    #每个5分钟获取一次proxys
    #timer_get_proxys(URL_PROXYS, TIME)
    
    #单次获取proxys
    list_count = refresh_urls(get_proxys(URL_PROXYS))
    print(list_count)



