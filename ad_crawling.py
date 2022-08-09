
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup as bs, PageElement
import os
import time
import re

#driver mount
driver = webdriver.Chrome(r"./chromedriver.exe") # 크롬드라이버 필요! (경로)
driver.implicitly_wait(7)
driver.get('https://tvcf.co.kr/Worked/CF/')

html = driver.page_source
soup = bs(html,'html.parser')




# 국가 선택
na = '대한민국'
nation = Select(driver.find_element(By.XPATH, r'//*[@id="ItemNation"]'))
nation.select_by_visible_text(na)


# 날짜 선택
driver.find_element(By.XPATH, r'//*[@id="periodDateText"]/button').click()

year = '2021'
year_ = Select(driver.find_element(By.XPATH, r'//*[@id="sDateYear"]'))
year_.select_by_visible_text(year)

month = 8
driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/select').click()

month_ = Select(driver.find_element(By.XPATH, r'//*[@id="sDateMonth"]'))
month_.select_by_index(month-1)

driver.find_element(By.XPATH, r'//*[@id="BtnSearchSubmit"]').click()


driver.implicitly_wait(5)

# 텍스트 파싱
# 광고링크 

# print(soup)
san_up_l = []
san_up_l2 =[]
ad_title_l= []
ad_sub_title_l= []
ad_date_l = []
ad_link_l = []
ad_time_l = []

# san_up = ['정보통신','전기전자','자동차/정유','음료/기호식품','식품제과','생활/가정용품','화장품','패션/스포츠','제약/의료/복지','금융/보험','아파트/건설','출판/교육/문화','서비스/유통/레저','관공서/단체/공익/기업PR']

# 산업선택
time.sleep(10)
# 최대 페이지 텍스트 구하기 ex-> 13page
a = driver.find_element_by_xpath('//*[@id="_Page"]')
max_page = a.get_attribute('max')
print(max_page)
for page in range(1,int(max_page)+1):
    time.sleep(3)
    if page==int(max_page):
        num = 33
    else:
        num = 51
    
    
    for i in range(1,num):
        # try: 
        # 광고 동영상 링크
        a = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[5]/div[1]/ul/li['+str(i)+']/div/div[2]/a')
        ad_link = a.get_attribute('href')
        
        # 광고제목, 광고부제목, 광고일자, 광고시간
        ad_title = driver.find_element(By.XPATH, r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[1]').text
        ad_sub_title = driver.find_element(By.XPATH,r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[2]').text
        ad_date = driver.find_element(By.XPATH,r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[3]').text
        ad_time = driver.find_element(By.XPATH,r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[1]/div[4]/div').text
        
        # 광고일자 정규표현식으로 괄호 안 내용만 추출    
        ad_date = re.findall('\(([^)]+)',ad_date)
        # ad_date = ad_date[2:-2]
        # print('ad_link',ad_link)
        print('ad_link',ad_link)
        print("ad_title",ad_title)
        print("ad_sub_title",ad_sub_title)
        print("ad_date",ad_date[0])
        print("ad_time",ad_time)
        

        san_up_l.append('정보통신')
        san_up_l2.append('이동통신')
        ad_title_l.append(ad_title)
        ad_sub_title_l.append(ad_sub_title)
        ad_date_l.append(ad_date)
        ad_link_l.append(ad_link)
        ad_time_l.append(ad_time)
        # time.sleep(1)
        # except:
        #     print("종료")
        #     break
    
   
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, r'//*[@id="_Page"]').click()
    driver.find_element(By.XPATH, r'//*[@id="_Page"]').clear()
    inputElement = driver.find_element(By.XPATH, r'//*[@id="_Page"]')
    inputElement.send_keys(str(page+1))
    time.sleep(3)
    inputElement.send_keys(Keys.RETURN)
    
    # print(ad_link_l,len(ad_link_l))
    # print(ad_sub_title_l,len(ad_sub_title_l))
    # print(ad_date_l,len(ad_date_l))
    # print(ad_link_l,len(ad_link_l))

list_data = san_up_l

df = pd.DataFrame((zip(san_up_l,san_up_l2,ad_title_l,ad_sub_title_l,ad_date_l,ad_time_l,ad_link_l)) ,columns = ['산업','산업2','광고제목','광고부제목','날짜','시간','링크'])

    # .to_csv 
# 최초 생성 이후 mode는 append
if not os.path.exists('ad_data3.csv'):
    df.to_csv('ad_data3.csv', index=False, mode='w', encoding='utf-8-sig')
else:
    df.to_csv('ad_data3.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
