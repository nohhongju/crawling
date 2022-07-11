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
# '에세이', '여행', '유아', '자기계발', 'IT 모바일'

Genre = [1, 3, 6, 8, 9, 11, 12, 15, 18, 24]

review = []


# 경제/ 경영 탭 클릭
for i in Genre:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{i}]/a'))).click()
    for page in range(1, 3):
        driver.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/p/a[2]').click()
        driver.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/p/a[{page}]').click()
        time.sleep(3)
        for title in range(1, 41, 3):
            title1 = driver.find_element(By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{title}]/td[3]/p[1]/a[1]').text
            print(f'**********************{title1}**********************')
            for book in range(1, 41, 3):
                driver.find_element(By.XPATH,
                                    f'//*[@id="category_layout"]/tbody/tr[{book}]/td[3]/p[1]/a[1]').click()
                time.sleep(3)
                for page1 in range(1, 12):
                    try:
                        driver.find_element(By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[{page1}]').click()
                        time.sleep(2)
                        for review in range(1, 7):
                            try:
                                review1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'#infoset_oneCommentList > div.infoSetCont_wrap.rvCmtRow_cont.clearfix > div:nth-child({review}) > div.cmtInfoBox > div.cmt_cont > span'))).text
                                time.sleep(2)
                                print(f'\n{review1}')
                            except:
                                break
                    except:
                        continue

                driver.back()


    '''
    for 페이지 in 전체페이지:
        for 책 in 페이지 안에 있는 모든 책:
            urllib.request.urlertrieve(imgUrl, f'{path}/data/{장르}{책제목}.jpg')

            for 리뷰 in 책 1권:

        driver.find_element(By.XPATH,f'~~~~~~~~').click()
    '''

time.sleep(5)
print(review)