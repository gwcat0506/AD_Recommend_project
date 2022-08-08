# 교통카드 데이터 다운로드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup as bs, PageElement
from selenium.webdriver import ActionChains
import time
import pyautogui

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

# # 산업 선택


driver.find_element(By.XPATH, r'//*[@id="ItemPum"]').click()
b = driver.find_element(By.XPATH, r'//*[@id="ItemPum"]/dl/dd/ul[1]/li[2]')
ActionChains(driver).move_to_element(b).perform()
# print(pyautogui.position())
# pyautogui.move(100, 50, duration=1) 
# driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[4]/div/dl/dt/a').click()

# 첫번째 방법
# sample = driver.find_element_by_css_select('//*[@id="ItemPum"]')
# sample.send_keys('\n')



# na = '전자전기'
# Select(driver.execute_element(By.XPATH, r'//*[@id="ItemNation"]'))
# driver.execute_script('document.querySelector("#ItemPum > dl > dt > a")')
# inputElement = driver.find_element(By.XPATH, r'//*[@id="SubmenuPum"]')
# driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[4]/div/dl/dt/a').click()
# 
# inputElement.send_keys(na)

# 두 번째 방법
time.sleep(20)
# sample = Select(driver.find_element(By.XPATH, r'//*[@id="ItemPum"]/dl/dt/a'))
# driver.execute_script("arguments[0].click();", sample)


