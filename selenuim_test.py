#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys
import getopt
import time
import random

proxy = "1.71.188.37:3128"
dst = "洛阳58"
se_url = "https://www.baidu.com/"
business_kw = "专业外墙瓷砖清洗"

def detect_url(proxy = proxy, se_url = se_url, dst = dst, business_kw = business_kw):
    try:
        #设置代理
        #firefox_options = options.Options()
        #firefox_options.add_argument("--proxy-server=" + proxy)

        #打开firefox浏览器
        #driver = webdriver.Firefox(firefox_options = firefox_options)
        driver = webdriver.Firefox()
        driver.get(se_url)
        try:
            time.sleep(random.uniform(1,3))
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
            driver.find_element_by_id("kw").send_keys(dst)
            driver.find_element_by_id("su").click()
        except:
            print("通过百度搜索洛阳58同城失败！")


        try:
            time.sleep(random.uniform(1,3))
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "1")))
            driver.find_element_by_id("1").find_elements_by_tag_name("a")[0].click()
        except:
            print("通过百度打开58同城失败！")


        time.sleep(1)
        driver.switch_to_window(driver.window_handles[-1])
        
        try:
            time.sleep(random.uniform(1, 3))
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "rightSide")))
            #获取需要点击的链接
            panel = driver.find_element_by_class_name("rightSide")
            panel.find_element_by_link_text("保洁").click()
        except:
            print("打开保洁链接失败！")
            return 404

        #切换浏览器网站tab
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[-1])

        try:
            time.sleep(random.uniform(1, 3))
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "img")))
            #获取需要点击的链接
            eles = driver.find_elements_by_partial_link_text(business_kw)
            eles[0].click()
        except:
            print("打开具体商家链接失败！")
            return 404
    except:
        print(proxy, " 访问 ", dst, "失败！")
        return 404
    finally:
        try:
            time.sleep(random.uniform(1, 2)) #此处延时超过5秒或关闭不了
            driver.quit()
            print(driver)
        except:
            print("failed!")
        return 404


if __name__ == "__main__":
    
    opts, args = getopt.getopt(sys.argv[1:], "hb:d:p:")
    for op, value in opts:
        if op == "-b":
            business_kw = value
        elif op == "-d":
            dst = value
        elif op == "-p":
            proxy = value
    detect_url(dst = dst, business_kw = business_kw)

