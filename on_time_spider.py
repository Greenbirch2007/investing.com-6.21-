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




driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

# 要打开页面，登录 ,太慢了，还不如单独爬去单个标的的数据再拼凑？ 如果单独来请求，就直接寻找专业的信息员就好！Investing还是太慢了

def start_page(url):

    driver.get(url)
    html = driver.page_source
    print(html)
    # driver.find_element_by_xpath('//*[@id="loginFormUser_email"]').clear()
    # driver.find_element_by_xpath('//*[@id="loginFormUser_email"]').send_keys('291109028@qq.com')
    # driver.find_element_by_xpath('//*[@id="loginForm_password"]').clear()
    # driver.find_element_by_xpath('//*[@id="loginForm_password"]').send_keys('mingyifan2007')
    # driver.find_element_by_xpath('//*[@id="signup"]/a').click()
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="navMenu"]/ul/li[10]/a').click()    # 点击投资组合
    # driver.find_element_by_xpath('//*[@id="portfolioEdit_908687"]/input').click()  # 点击us组合
    # driver.find_element_by_xpath('//*[@id="portfolioEdit_4023483"]/input').click()  #点击J组合
    # driver.find_element_by_xpath('//*[@id="portfolioEdit_4023483"]/input').click()  #点击HK组合
    # get_info()
    # driver.close()


#投资组合















def get_info():
    html = driver.page_source
    print(html)
    # patt = re.compile('data-id="(.*?)"', re.S)
    # items = re.findall(patt, html)



if __name__ =='__main__':
    url = 'https://cn.investing.com/equities/mori-trust-sogo-reit'
    start_page(url)