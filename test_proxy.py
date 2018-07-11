from selenium import webdriver

import time

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

firefox = webdriver.Firefox()
firefox.get("https://sslvpn.bnu.edu.cn/,DanaInfo=www.cnki.net,SSO=U+")

time.sleep(3)

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

table = firefox.find_elment_by_class_name("GridTableContent")
rows = table.finde_elements_by_tag_name("tr")[1:]

f = open("dict.txt", "w")


for row in rows:
    cols = row.find_elements_by_tag_name("td")
    title = cols[1].getText()
    author = cols[2].getText()
    time = cols[4].getText().split("-")[0]
    f.write(title + " " + author + " " + time + "\n")
    row.find_element_by_class_name("briefDL_D").click()
