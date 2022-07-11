import os, shutil, numpy as np, pandas as pd, time, urllib.request, warnings, cv2
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
warnings.filterwarnings(action='ignore')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C://chromedriver.exe', options=options)

driver.get("https://www.paxnet.co.kr/")      
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="layerPopup"]/div[2]/button').click()   
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div/ul/li[4]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[5]/div/div/ul/li[10]/span/a').click()
elem = driver.find_element_by_name("kwd")      
elem.send_keys('비트코인')                                                                                                                              
driver.find_element_by_xpath('//*[@id="frmData"]/div[3]/ul/li[2]/div/span[2]/button').click() 
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[1]/th[2]').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/thead/tr/th[1]/i').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr/td/span[4]').click()  # 끝에 4가 4월 의미
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[5]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="frmData"]/div[3]/ul/li[2]/div/span[3]/button').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/table/tbody/tr[2]/td[3]').click()    # 220405 클릭.
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="frmData"]/div[3]/ul/li[3]/div[1]/label[2]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="frmData"]/div[3]/ul/li[4]/div/span/label[4]').click()
time.sleep(0.5)
elem.send_keys(Keys.RETURN)              
driver.find_element_by_xpath('//*[@id="frmData"]/div[4]/div/p[1]/label[2]').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath('//*[@id="frmData"]/div[5]/div/a[4]').click()      # 제일 마지막 페이지로 이동.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

headline = []
datetime = []
emotion = []
while True:
    page_num = len(driver.find_elements_by_css_selector("#frmData > div.board-thumbnail > div > ul > li"))  # 현재페이지에서 소분류페이지의 수

    for j in range(page_num):   # 페이지 수만큼 역순반복 

        infor_list = driver.find_elements_by_css_selector("#frmData > div.board-thumbnail > ul > li")   # 현재 페이지에서 뉴스의 개수.

        for i in range(len(infor_list)):
            headline.append(driver.find_element_by_xpath(f'//*[@id="frmData"]/div[5]/ul/li[{len(infor_list)-i}]/dl/dt/a').text)
            datetime.append(driver.find_element_by_xpath(f'//*[@id="frmData"]/div[5]/ul/li[{len(infor_list)-i}]/dl/dd[2]/span[2]').text.split(' ')[0])
            
        if page_num - (j + 1) == 0 :    # 0쪽 뒤로는 없으니까 이전의 5페이지 로드하기버튼 클릭
            driver.find_element_by_xpath('//*[@id="frmData"]/div[5]/div/a[2]').click()
            break
        driver.find_element_by_xpath(f'//*[@id="frmData"]/div[5]/div/ul/li[{page_num - (j+1)}]/a').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    if len(headline) == int(driver.find_element_by_xpath('//*[@id="frmData"]/div[4]/mark[2]').text.replace(",","")) : 
        break

datetime_df = pd.DataFrame(datetime,columns=['datetime'])
headline_df = pd.DataFrame(headline,columns=['headline'])
emotion_df = pd.DataFrame(emotion,columns=['emotion'])

emotion_df = pd.concat([datetime_df,headline_df,emotion],axis=1)
emotion_df.to_csv('감정분석.csv',index=False,encoding='utf-8')