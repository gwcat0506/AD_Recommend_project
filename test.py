
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup as bs, PageElement
import time

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

year = '2022'
year_ = Select(driver.find_element(By.XPATH, r'//*[@id="sDateYear"]'))
year_.select_by_visible_text(year)

month = 1
driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/select').click()

month_ = Select(driver.find_element(By.XPATH, r'//*[@id="sDateMonth"]'))
month_.select_by_index(month-1)

driver.find_element(By.XPATH, r'//*[@id="BtnSearchSubmit"]').click()


driver.implicitly_wait(5)

# 텍스트 파싱
# 광고링크 

# print(soup)
san_up_l = []
ad_title_l= []
ad_sub_title_l= []
ad_date_l = []
ad_link_l = []
san_up = ['정보통신','전기전자','자동차/정유','음료/기호식품','식품제과','생활/가정용품','화장품','패션/스포츠','제약/의료/복지','금융/보험','아파트/건설','출판/교육/문화','서비스/유통/레저','관공서/단체/공익/기업PR']

for j in range(14):
    # # 산업 선택

    time.sleep(1)
    driver.find_element(By.XPATH, r'//*[@id="ItemPum"]').click()
    driver.find_element(By.XPATH, r'//*[@id="ItemPum"]/dl/dd/ul[1]/li['+str(j+2)+']').click()
    time.sleep(10)
    # 최대 페이지 텍스트 구하기 ex-> 13page
    a = driver.find_element_by_xpath('//*[@id="_Page"]')
    max_page = a.get_attribute('max')
    print(max_page)
    for page in range(1,int(max_page)):
        time.sleep(3)
        for i in range(1,51):
            # try: 
            # 광고 동영상 링크
            a = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[5]/div[1]/ul/li['+str(i)+']/div/div[2]/a')
            ad_link = a.get_attribute('href')
            
            # 광고제목, 광고부제목, 광고일자
            ad_title = driver.find_element(By.XPATH, r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[1]').text
            ad_sub_title = driver.find_element(By.XPATH,r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[2]').text
            ad_date = driver.find_element(By.XPATH,r'//*[@id="ListAjax1"]/div[1]/ul/li['+str(i)+']/div/div[2]/a/div[3]').text
            ad_date = ad_date[1:-1]
            # print('ad_link',ad_link)
            print('ad_link',ad_link)
            print("ad_title",ad_title)
            print("ad_sub_title",ad_sub_title)
            print("ad_date",ad_date)

            san_up_l.append(san_up[j])
            ad_title_l.append(ad_title)
            ad_sub_title_l.append(ad_sub_title)
            ad_date_l.append(ad_date)
            ad_link_l.append(ad_link)
            # time.sleep(1)
            # except:
            #     print("종료")
            #     break
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.XPATH, r'//*[@id="_Page"]').click()
        driver.find_element(By.XPATH, r'//*[@id="_Page"]').clear()
        inputElement = driver.find_element(By.XPATH, r'//*[@id="_Page"]')
        inputElement.send_keys(str(page))
        time.sleep(3)
        inputElement.send_keys(Keys.RETURN)
        
        print(ad_link_l,len(ad_link_l))
        print(ad_sub_title_l,len(ad_sub_title_l))
        print(ad_date_l,len(ad_date_l))
        print(ad_link_l,len(ad_link_l))
    
df = pd.DataFrame((zip(san_up_l,ad_title_l,ad_sub_title_l,ad_date_l,ad_link_l)) ,columns = ['산업','광고제목','광고부제목','날짜','링크'])
df.to_csv('ad_data.csv',index=False)
print(df)


    





# //*[@id="ItemPum"]/dl/dd/ul[1]/li[2] -> 정보통신, li[3] -> 전기전자

# nation = Select(driver.find_element(By.XPATH, r'//*[@id="dropdown"]'))
# nation.select_by_visible_text(na)

