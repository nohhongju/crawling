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
# driver.maximize_window()
# '가정 살림', '경제 경영', '만화/라이트노벨', '수험서 자격증', '소실/시/희곡',
# '에세이', '여행', '유아', '자기계발', 'IT 모바일'   , 3, 6, 8, 9, 11, 12, 15, 18, 24

Genre = [1]

list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []



# 경제/ 경영 탭 클릭
for category in Genre:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{category}]/a'))).click()
    for page in range(3, 4):
        driver.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/p/a[2]').click()
        driver.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/p/a[{page}]').click()
        time.sleep(3)
        for title in range(1, 40, 2):
            title1 = driver.find_element(By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{title}]/td[3]/p[1]/a[1]').text
            print(f'**********************{title1}**********************')
            for i in range(1, 40, 2):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).click()
                for review_page in range(1, 4):
                    try:
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    f'//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[{review_page}]'))).click()
                        for i in range(1, 7):
                            try:
                                review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((
                                                                                                          By.CSS_SELECTOR,
                                                                                                          f'#infoset_oneCommentList > div.infoSetCont_wrap.rvCmtRow_cont.clearfix > div:nth-child({i}) > div.cmtInfoBox > div.cmt_cont > span'))).text
                                title = driver.find_element(By.XPATH,
                                                            '/html/body/div/div[4]/div[1]/div/span/em/img').get_attribute(
                                    'alt')
                                # review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[3]/div[{i}]/div[1]/div[2]/span'))).get_attribute("innerHTML")
                                if category == '1':
                                    list0.append({title: review})
                                elif category == '3':
                                    list1.append({title: review})
                                elif category == '6':
                                    list2.append({title: review})
                                elif category == '8':
                                    list3.append({title: review})
                                elif category == '10':
                                    list4.append({title: review})
                                elif category == '11':
                                    list5.append({title: review})
                                elif category == '12':
                                    list6.append({title: review})
                                elif category == '15':
                                    list7.append({title: review})
                                elif category == '18':
                                    list8.append({title: review})
                                elif category == '24':
                                    list9.append({title: review})
                            except:
                                break
                    except:
                        break
                # 뒤로 가기
                driver.back()
    if category == '1':
        review_list = pd.Series(list0)
        review_list.to_csv(f'save/reviews/살림가정.csv', encoding='utf-8', index=False)
    elif category == '3':
        review_list = pd.Series(list1)
        review_list.to_csv(f'save/reviews/경제경영.csv', encoding='utf-8', index=False)
    elif category == '6':
        review_list = pd.Series(list2)
        review_list.to_csv(f'save/reviews/만화라이트노벨.csv', encoding='utf-8', index=False)
    elif category == '8':
        review_list = pd.Series(list3)
        review_list.to_csv(f'save/reviews/소설시희곡.csv', encoding='utf-8', index=False)
    elif category == '10':
        review_list = pd.Series(list4)
        review_list.to_csv(f'save/reviews/어린이.csv', encoding='utf-8', index=False)
    elif category == '11':
        review_list = pd.Series(list5)
        review_list.to_csv(f'save/reviews/에세이.csv', encoding='utf-8', index=False)
    elif category == '12':
        review_list = pd.Series(list6)
        review_list.to_csv(f'save/reviews/여행.csv', encoding='utf-8', index=False)
    elif category == '15':
        review_list = pd.Series(list7)
        review_list.to_csv(f'save/reviews/유아.csv', encoding='utf-8', index=False)
    elif category == '18':
        review_list = pd.Series(list8)
        review_list.to_csv(f'save/reviews/자기계발.csv', encoding='utf-8', index=False)
    elif category == '24':
        review_list = pd.Series(list9)
        review_list.to_csv(f'save/reviews/IT모바일.csv', encoding='utf-8', index=False)