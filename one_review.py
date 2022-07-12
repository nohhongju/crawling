import pandas as pd
from selenium import webdriver
import urllib3
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException, ElementNotInteractableException,NoSuchWindowException, NoSuchFrameException

import time
import re
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
유아 15, 자기계발 18, IT모바일 24
, '3', '6', '8', '10', '11', '12', '15', '18', '24'
'''
categoreis = ['1']
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []

# 장르 클릭
for category in categoreis:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{category}]/a'))).click()
    for page in range(1, 11):
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[{page}]'))).click()
            # 도서 클릭
            for i in range(1, 40, 2):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).click()
                for review_page in range(1, 4):
                    try:
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[{review_page}]'))).click()
                        for i in range(1, 7):
                            try:
                                review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'#infoset_oneCommentList > div.infoSetCont_wrap.rvCmtRow_cont.clearfix > div:nth-child({i}) > div.cmtInfoBox > div.cmt_cont > span'))).text
                                title = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div/span/em/img').get_attribute('alt')
                                # review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[3]/div[{i}]/div[1]/div[2]/span'))).get_attribute("innerHTML")
                                if category == '1':
                                    list0.append({title: review})
                                elif category == '3':
                                    list1.append({title: review})
                                elif category == '6':
                                    list2.append({title: review})
                                elif category == '10':
                                    list3.append({title: review})
                                elif category == '11':
                                    list4.append({title: review})
                                elif category == '12':
                                    list5.append({title: review})
                                elif category == '15':
                                    list6.append({title: review})
                                elif category == '18':
                                    list7.append({title: review})
                            except:
                                break
                    except:
                        break
                # 뒤로 가기
                driver.back()
        except:
            continue
    if category == '1':
        review_list = pd.Series(list0)
        review_list.to_csv(f'save/reviews/살림가정.csv', encoding='utf-8', index=False)
    elif category == '3':
        review_list = pd.Series(list1)
        review_list.to_csv(f'save/reviews/경제경영.csv', encoding='utf-8', index=False)
    elif category == '6':
        review_list = pd.Series(list2)
        review_list.to_csv(f'save/reviews/만화라이트노벨.csv', encoding='utf-8', index=False)
    elif category == '10':
        review_list = pd.Series(list3)
        review_list.to_csv(f'save/reviews/어린이.csv', encoding='utf-8', index=False)
    elif category == '11':
        review_list = pd.Series(list4)
        review_list.to_csv(f'save/reviews/에세이.csv', encoding='utf-8', index=False)
    elif category == '12':
        review_list = pd.Series(list5)
        review_list.to_csv(f'save/reviews/여행.csv', encoding='utf-8', index=False)
    elif category == '15':
        review_list = pd.Series(list6)
        review_list.to_csv(f'save/reviews/유아.csv', encoding='utf-8', index=False)
    elif category == '18':
        review_list = pd.Series(list7)
        review_list.to_csv(f'save/reviews/자기계발.csv', encoding='utf-8', index=False)
    elif category == '24':
        review_list = pd.Series(list8)
        review_list.to_csv(f'save/reviews/IT모바일.csv', encoding='utf-8', index=False)

