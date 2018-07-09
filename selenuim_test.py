#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys
import time
import random

PROXY = "1.71.188.37:3128"
DST_URL = "http://luoyang.58.com/"

def detect_url(proxy = PROXY, dst_url = DST_URL):
    #try:
        #设置代理
        #firefox_options = options.Options()
        #firefox_options.add_argument("--proxy-server=" + proxy)

        #打开firefox浏览器
        #driver = webdriver.Firefox(firefox_options = firefox_options)
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get(dst_url)
        
        locator = (By.LINK_TEXT,"保洁")
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            #获取需要点击的链接
            panel = driver.find_element_by_class_name("rightSide")
            panel.find_element_by_link_text("保洁").click()
        except:
            print("打开保洁链接失败！")
            return 404

        #切换浏览器网站tab
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])

        time.sleep(random.uniform(5,10))
        print(handles)
        #try:
        #locator = (By.LINK_TEXT, "专业外墙瓷砖清洗")
        #WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            #获取需要点击的链接
        eles = driver.find_element_by_partial_link_text("专业外墙瓷砖清洗")
        print(eles)
        eles.click()
        #except:
        #    print("打开具体商家链接失败！")
        #    return 404

        return 200
    #except:
    #    print(proxy, " 访问 ", dst_url, "失败！")
    #    return 404
    #finally:
    #    driver.close()



if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        PROXY = sys.argv[1]
        DST_URL = sys.argv[2]
    detect_url(PROXY, DST_URL)
