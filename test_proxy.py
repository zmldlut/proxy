from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import os
import shutil

dict = {}

"""
ip = "1.71.188.37"
port = 3128

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
profile.set_preference('network.proxy.http', ip)
profile.set_preference('network.proxy.http_port', port)

profile.set_preference('network.proxy.ssl',ip)
profile.set_preference('network.proxy.ssl_port', port)
profile.update_preferences()
browser = webdriver.Firefox(profile)
browser.get("https://www.icanhazip.com")
"""


profile = webdriver.FirefoxProfile()
profile['browser.download.dir'] = "/home/zml/cxy"  
profile['browser.download.folderList'] = 2  
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
firefox = webdriver.Firefox(firefox_profile=profile)
firefox.get("https://sslvpn.bnu.edu.cn/,DanaInfo=www.cnki.net,SSO=U+")

time.sleep(1)

try:
    firefox.find_element_by_name("username").send_keys("201731080038")
    firefox.find_element_by_name("password").send_keys("cxy19901214")
    firefox.find_element_by_name("btnSubmit").click()
    time.sleep(1)
    firefox.find_element_by_name("btnContinue").click()
    time.sleep(1)
    firefox.find_element_by_name("txt_SearchText").send_keys("罗素 杜威")
    firefox.find_elements_by_class_name("search-btn")[0].click()
except:
    print("不需要登录！")


time.sleep(3)

form_s = firefox.find_element_by_id("Form1")
iframes = form_s.find_element_by_tag_name("iframe")

firefox.switch_to_frame(iframes)
table = firefox.find_element_by_class_name("GridTableContent")
rows = table.find_elements_by_tag_name("tr")[1:]

f = open("dict.txt", "w")


for row in rows:
    cols = row.find_elements_by_tag_name("td")
    title = cols[1].text
    author = cols[2].text
    ti = cols[4].text.split("-")[0]
    dict[author] = time
    f.write(title + " " + author + " " + ti + "\n")
    row.find_element_by_class_name("briefDl_D").click()
    break
    time.sleep(5)

f.close()

def f(in_dir, out_dir):
    for root, dirs, files in os.walk(in_dir, out_dir):
        for file in files:
            author = file.split(",")[0].split("_")[1]
            out = "其他"
            for key in dict.keys():
                if author in key:
                    out = dict[key]

            out = os.path.join(out_dir, out)
            if os.path.exists(out):
                pass
            else:
                os.makedirs(out)
            file_path = os.path.join(root,file)
            shutil.copy(file_path, out)



