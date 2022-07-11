# selenium 관련 import
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import urllib.request,time,warnings,os     # url주소,경고창,os폴더생성

warnings.filterwarnings(action='ignore')    # 경고 무시

# 크롬창에서 F12누르면 html 작업창이 나옴.
# 크롬드라이버 옵션 설정, 2번째줄은 보안관련 해제해주는 옵션
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C://chromedriver.exe', options=options)

# 크롬실행 후 검색창에 keyword 입력
driver.get("https://finance.naver.com/sise/")           # 실행할 창 주소 넣어주세요.
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/ul/li[2]/a/span').click()
aa = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/a/span[2]').text
print(aa)
# elem = driver.find_element_by_name("q")                           # name으로 검색창 element 이름 가져와서 elem에 저장                        
# elem.send_keys('마동석')                                          # 검색창에 마동석이라고 key를 보냅니다.
# elem.send_keys(Keys.RETURN)                                       # 엔터누르는 작업

time.sleep(5)                                                     # 