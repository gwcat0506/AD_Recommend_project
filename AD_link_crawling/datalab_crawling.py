# 네이버 데이터랩에서 분야에 따른 성별, 연령별 관심도 


from urllib.request import url2pathname
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.implicitly_wait(3)

base_url = "https://datalab.naver.com/shoppingInsight/sCategory.naver"
driver.get(base_url)
html = driver.page_source
soup = bs(html,'html.parser')

a= driver.find_element(By.XPATH, r'//*[@id="popupLineGraph"]/svg/g[1]/g[3]').text
print(a)

# print(soup)
# driver.implicitly_wait(5)



# driver.close()