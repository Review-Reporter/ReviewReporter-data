from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from openpyxl import Workbook
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

wb = Workbook(write_only=True) #엑셀에 데이터 입력을 활성화
ws = wb.create_sheet('무신사 트레이드 시리즈 백팩 블랙')
columns = ['날짜', '리뷰']
ws.append(columns)

options = webdriver.ChromeOptions()
#options.add_argument('headless') #창 띄우지 않고 크롤링하도록 하는 옵션 (개발할때는 옵션 주지 않기)

#'C:\selenium/chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)#다운받은 크롬드라이버 경로 입력해주기
driver.implicitly_wait(2)#웹자원 로드를 위해 대기

detail_url = 'https://store.musinsa.com/app/goods/472915'
driver.get(detail_url)#URL 입력

#스타일후기
i=0
while i<=5:
    i += 1
    locates = 'div.review-contents > div.review-contents__text'  # 댓글 locates
    date_locates = 'div.review-profile > div > div.review-profile__text > p.review-profile__date'  # 댓글 locates
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, locates)
    elements = elements[:10]
    date_elements = driver.find_elements(By.CSS_SELECTOR, date_locates)
    date_elements = date_elements[:10]
    for element, date_element in zip(elements, date_elements):
        print(element.text)
        print(date_element.text)
        row = [date_element.text, element.text] #엑셀에 넣어주기
        ws.append(row)
    if(i%5==0):
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,'#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').send_keys(Keys.ENTER)
    else:
        page = '#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a:nth-child(%d)'%((i%5)+3)
        print(page)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,page).send_keys(Keys.ENTER)

#상품후기
#driver.find_element(By.CSS_SELECTOR,'#estimate_photo').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#estimate_photo').click()
i=0
while i<=17:
    i += 1
    locates = 'div.review-contents > div.review-contents__text'  # 댓글 locates
    date_locates = 'div.review-profile > div > div.review-profile__text > p.review-profile__date'  # 날짜 locates
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, locates)
    elements = elements[:10]
    date_elements = driver.find_elements(By.CSS_SELECTOR, date_locates)
    date_elements = date_elements[:10]
    for element, date_element in zip(elements, date_elements):
        print(element.text)
        print(date_element.text)
        row = [date_element.text, element.text] #엑셀에 넣어주기
        ws.append(row)
    if(i%5==0):
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,'#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').send_keys(Keys.ENTER)
    else:
        page = '#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a:nth-child(%d)'%((i%5)+3)
        print(page)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,page).send_keys(Keys.ENTER)

#일반후기
#driver.find_element(By.CSS_SELECTOR,'#estimate_goods').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#estimate_goods').click()
i=0
while i<=37:
    i += 1
    locates = 'div.review-contents > div.review-contents__text'  # 댓글 locates
    date_locates = 'div.review-profile > div > div.review-profile__text > p.review-profile__date'  # 댓글 locates
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, locates)
    elements = elements[:10]
    date_elements = driver.find_elements(By.CSS_SELECTOR, date_locates)
    date_elements = date_elements[:10]
    for element, date_element in zip(elements, date_elements):
        print(element.text)
        print(date_element.text)
        row = [date_element.text, element.text] #엑셀에 넣어주기
        ws.append(row)
    if(i%5==0):
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,'#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').send_keys(Keys.ENTER)
    else:
        page = '#reviewListFragment > div.nslist_bottom > div.pagination.textRight > div > a:nth-child(%d)'%((i%5)+3)
        print(page)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,page).send_keys(Keys.ENTER)

wb.save('무신사 트레이드 시리즈 백팩 블랙.xlsx') #엑셀저장