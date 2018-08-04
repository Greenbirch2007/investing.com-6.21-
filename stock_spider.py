#! -*- coding:utf-8 -*-


import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import urllib.request
import time
from multiprocessing import Pool
proxies = { "https": "https://1.199.194.227"}
# full_url = "http://www.mzitu.com/xinggan/"
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0'}
def get_one_page(url):
    try:
        response = requests.get(url,proxies=proxies,headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            get_one_page()
    except HTTPError :
        pass

str_list = []

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def start_page():

    try:
        driver.get('https://cn.investing.com/stock-screener/?sp=country::37|sector::a|industry::a|equityType::a%3Ceq_market_cap;1')
        # time.sleep(6)
        # get_info()

    except TimeoutException:
        return start_page()
#还是要掌握js的写法！

# <a href="javascript:void(0);" " title=" 显示结果 51 到 100 / 3631" class="pagination" boundblank="">2</a>


# 翻页的类型也很多，有一般的，变换距离的，要执行js的
def next_page():
    try:
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="paginationWrap"]/div[3]/a')))
        submit.click()
        # get_info()
    except TimeoutException:
        next_page()

start_page()
next_page()
#
# def get_info():
#     driver.implicitly_wait(6)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.con > div > script:nth-child(2)')))
    # html = driver.page_source
    # patt = re.compile('data-id="(.*?)"', re.S)
    # items = re.findall(patt, html)
    # for ite1 in items:
    #     str_list.append(ite1)
    # for ite2 in iter(str_list):
    #     url = 'http://www.sesehezi.com/video/' + ite2
    #     big_list.append(url)