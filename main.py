#!/usr/bin/env python
# coding=utf-8
import requests
import threading
import random
import time

URL_PROXYS = "http://192.168.0.111:5010/get_all"

PROXYS = []
DST_URL = [
    "https://www.baidu.com"
]
TIME = 60 * 5
PROXIES_FILE = "./proxies.txt"

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

def refresh_urls(urls, proxies):
    list_count = []
    for url in urls:
        count = 0
        for proxy in proxies:
            h = random.uniform(0,10)
            m = random.uniform(0,60)
            s = random.uniform(0,60)
            ti = h * 10 + m * 2 + s
            time.sleep(ti)
            print(ti)
            try:
                r = requests.get(url, proxy)
                if r.status_code == 200:
                    count += 1
            except:
                print(url)
                print(proxy)
                print("filed!")
        list_count.append(count)

    return list_count
    

#timer = threading.Timer(1, timer_get_proxys, [URL_PROXYS, TIME])
#timer.start()

if __name__ == "__main__":
    
    print("hello world!")
    #timer_get_proxys(URL_PROXYS, TIME)
    get_proxys(URL_PROXYS)
    print(PROXYS)
    list_count = refresh_urls(DST_URL, get_proxies(PROXYS))
    print(list_count)



