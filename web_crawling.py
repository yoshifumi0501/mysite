#!/usr/bin/env python
# coding: utf-8

# In[4]:


# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import sys
import warnings
import time
warnings.simplefilter('ignore')



def crawling(url, retries_count, executable_path) :
    for _ in range(retries_count):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        #ヘッドレスオプションを実装するとブラウザ画面が表示されない
#         options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--user-agent=hogehoge')

        try:
	    # 失敗しそうな処理
            time.sleep(0.2)
            driver = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
            driver.implicitly_wait(30)
            driver.get(url)
            WebDriverWait(driver,30).until(EC.presence_of_all_elements_located)
            # HTMLを文字コードをUTF-8に変換してから取得します。
            html = driver.page_source.encode('utf-8')
            # BeautifulSoupで扱えるようにパースします
            soup = BeautifulSoup(html, "html.parser")
        except Exception as e :
	    # エラーメッセージを格納する
            print(url)
            print(e)
            time.sleep(5)

        else:
	    # 失敗しなかった場合は、ループを抜ける
            time.sleep(0.2)
            driver.close()
            time.sleep(0.2)
            driver.quit()

            break
    else:
        error = "エラー"
        #アカウント認証
#         account= ''
#         password = ''
#         # 送受信先
#         to_email = ""
#         from_email = ''
#         sendgmail(account, password, to_email, from_email, error) 
        driver.quit()
        time.sleep(5)
        # プログラムを強制終了する
        sys.exit(1)

    return soup


# In[6]:


# url = "https://www.google.co.jp/"
# retries_count=5
# #クロームドライバーのパスを指定
# executable_path = "/Users/hogehoge/Project/chromedriver"
# crawling(url,retries_count,executable_path)


# In[ ]:




