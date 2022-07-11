import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import urllib3


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# driver = webdriver.Chrome("C:\chromedriver.exe", options=options)

s = Service('C:\chromedriver.exe')
driver = webdriver.Chrome(service=s)

url = "http://www.yes24.com/24/Category/BestSeller"
driver.get(url)

'''
경제/경영 3, 만화/라이트노벨 6, 소설/시/희곡 8, 어린이 10, 에세이 11, 여행 12, 
유아 15, 자기계발 18, IT 모바일 24
, '3', '6', '8', '10', '11', '12', '15', '18', '24'
'''
categoreis = ['1']
review_list = []

# 장르 클릭
for category in categoreis:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{category}]/a'))).click()
    # 페이지 클릭
    for page in range(1, 11):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[{page}]'))).click()
        # 도서 클릭
        for i in range(1, 40, 2):
            title1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).text
            print(f'**********************{title1}**********************')
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).click()
            for page in range(1, 12):
                try:
                    driver.find_element(By.XPATH,f'//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[{page}]').click()
                    time.sleep(2)
                    for i in range(1, 7):
                        try:
                            review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'#infoset_oneCommentList > div.infoSetCont_wrap.rvCmtRow_cont.clearfix > div:nth-child({i}) > div.cmtInfoBox > div.cmt_cont > span'))).text
                            # review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[3]/div[{i}]/div[1]/div[2]/span'))).get_attribute("innerHTML")
                            review_list.append(review)
                            print(f'{review}')
                        except:
                            break
                except:
                    continue
            driver.back()


pd.DataFrame(review_list).to_csv('save/reviews.csv', index=False)