#! -*- coding:utf-8 -*-


import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E



# 网页有js渲染，selenium出动
def get_one_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=4hu00ltjtja67ou5rk52vcsap6; geoC=CN; adBlockerNewUserDomains=1529582697; StickySession=id.14211634542.498.cn.investing.com; _ga=GA1.2.1542595398.1529582706; _gid=GA1.2.1563365873.1529582708; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1529582708; __gads=ID=3bbccfb89689b3c5:T=1529582707:S=ALNI_MZRIyxz0CMhn04-wHc7oADDtRRhGQ; billboardCounter_6=0; nyxDorf=OT1kNWU3YyEwbjw5ZCk3PDRkP3owMjA2; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1529593201; _gat_allSitesTracker=1; _gat=1',
        'Host': 'cn.investing.com',
        'Referer': 'https://cn.investing.com/equities/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code ==200:
            print(response.text)
        else:
            print(response.status_code)
    except RequestException:
        None

    print(response.status_code)
# 要用selenium等待页面完全加载！

url = 'https://cn.investing.com/stock-screener/?sp=country::39|sector::a|industry::a|equityType::a%3Ceq_market_cap;1'


get_one_html(url)

