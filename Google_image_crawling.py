import os, shutil, numpy as np, pandas as pd, time, urllib.request, warnings, cv2
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

warnings.filterwarnings(action='ignore')

path = os.path.dirname(os.path.realpath(__file__))
os.makedirs(path + '/data',exist_ok=True)

word_list = {'토이스토리 우디':'woody','토이스토리 버즈':' buzz','토이스토리 보핍':'boopeep'}      # 폴더명을 한글로 저장하면 에러가 발생해서 영어로 작성해야함. 
n = 10                                                              # 저장할 사진의 장수
errorcode = []                                                      # 다운로드받다가 발생한 에러를 담는 list.

for keyword, saveword in word_list.items():
    
    os.makedirs(f'{path}/data/{saveword}',exist_ok=True)
        

    ne = round(n/20)                                               # 사진다운받다가 에러터질경우 여유사진 로드하기위해 추가해주는 변수                                  

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C://chromedriver.exe', options=options)
    
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")                                          
    elem = driver.find_element_by_name("q")                                                                   
    elem.send_keys(f'{keyword}')                                                                        
    elem.send_keys(Keys.RETURN)  
    driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div').click()      # 도구-모든크기-큼
    driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[1]/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]/div').click()
    
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")           # 검색하자마자 로드 된 이미지의 수.      
    
    if len(images) < n+ne:                                                  # 만약 내가 다운받고 싶은 사진이 로드 된 이미지 수보다 적다면.                                                    
        while True:                                                         # 무한대로 실행하겠다.                             
            last_height = driver.execute_script("return document.body.scrollHeight")                   
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")                    
            time.sleep(1)                                                                                    
            new_height = driver.execute_script("return document.body.scrollHeight")                    
            images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")               # 스크롤을 내리고 사진 장수를 다시 구함.                     
            print(f'{keyword}사진 현재{len(images)}장 로드, {n+ne}장까지 로드하기 위해 스크롤 중................') 
            
            if len(images) >= n+ne:                                         # 스크롤을 내려서 구한 사진이 내가 원하는 사진보다 많다면.                                                            
                print(f'.........................................현재{len(images)}장까지 로드하여 이제 저장을 시작합니다')
                break   # 끊겠다.                                                                                    
            else:       # 아니라면 스크롤을 또 내림                                                                               
                if new_height == last_height:                                                           
                    try:                                                                                        
                        driver.find_element_by_css_selector('.mye4qd').click()    # 결과 더보기 버튼을 클릭해라.                      
                    except:                                                                                     
                        errorcode.append('스크롤 오류. 더 로드할 사진이 없습니다.')   # 사진이 더이상 없으면    
                        break                                                        # 끊겠다.                            
                last_height = new_height   
                                                                            
    time.sleep(3)     # 네트워트 속도가 느려서 혹시 모르니까 3초 일단 기다리겠다.
    
    count = 1         # 사진 다운받는 장수 세주기 위한 변수.
    
    totalstart = time.time()
    for image in images:
        try:                      
            image.click()             # 이미지 클릭 -> 큰 이미지가 오른쪽에 뜸.          
            start = time.time()
            imgUrl = driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')                
            print(f'{count} / {n}, {keyword}사진 다운로드 중......... Download time : '+str(time.time() - start)[:5]+' 초')                                  
            urllib.request.urlretrieve(imgUrl, f"{path}/data/{saveword}/{count:0{len(str(n))}d}.jpg")   # 사진 저장. 
            time.sleep(1)                                                     
        
            if count == n :    # 저장된 사진수와 내가 요구한 사진수가 같으면         
                break          # 끊겠다.
            count += 1         # 1장 다운로드하고 +1해서 2장째로 count함.   
                   
        except:                    
            errorcode.append(f'{count}번째 저장오류 다음사진을 저장합니다.')    # 사진 다운로드하다가 에러터지면 넘겨줌.  
            print(f'{count}장째 에러') 
            
    totalend = str(time.time() - totalstart)[:5]   

    if count < n:          
        errorcode.append(f'더 이상의 사진이 없기때문에 {n}장까지 다운로드하지 못하고 {count-1}장까지만 저장했습니다.')      
    
    print(f'------------------다운로드시간 {totalend}초-----------------------')
    driver.close()
    print(f'-------------{saveword} 폴더생성이 완료되었습니다.-----------------')

