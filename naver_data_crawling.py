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
ws = wb.create_sheet('네이버 스트레치엔젤스 리사이클 나일론 시티 호보백')
columns = ['날짜', '리뷰']
ws.append(columns)

options = webdriver.ChromeOptions()
#options.add_argument('headless') #창 띄우지 않고 크롤링하도록 하는 옵션 (개발할때는 옵션 주지 않기)

#'C:\selenium/chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)#다운받은 크롬드라이버 경로 입력해주기
driver.implicitly_wait(2)#웹자원 로드를 위해 대기

detail_url = 'https://search.shopping.naver.com/catalog/28925951387?query=%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%B9%98%EC%97%94%EC%A0%A4%EC%8A%A4%20%ED%98%B8%EB%B3%B4%EB%B0%B1&NaPm=ct%3Dl1dbvge8%7Cci%3Daa901c765ec8640332c1c5cd5d6ae1b9f9dc72ab%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D72e30a2a10dd481d9af4056f5915ed1a1c8af37f'
driver.get(detail_url)#URL 입력

driver.find_element_by_css_selector('#section_review > div.filter_sort_group__Y8HA1 > div.filter_filter_box__iKVkl > div.filter_sort_box__223qy > a:nth-child(3)').click() #최신순 정렬

#후기
i=0
while i<=2:
    i += 1
    locates = 'div.reviewItems_review__1eF8A > div > p'  # 댓글 locates
    date_locates = 'div.reviewItems_etc_area__2P8i3 > span:nth-child(4)'  # 날짜 locates
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, locates)
    elements = elements[:20]
    date_elements = driver.find_elements(By.CSS_SELECTOR, date_locates)
    date_elements = date_elements[:20]
    for element, date_element in zip(elements, date_elements):
        print(element.text)
        print(date_element.text)
        row = [date_element.text, element.text] #엑셀에 넣어주기
        ws.append(row)
    if(i!=3):
        page = '#section_review > div.pagination_pagination__2M9a4 > a:nth-child(%d)'%(i+1)
        #print(page)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,page).send_keys(Keys.ENTER)



wb.save('네이버 스트레치엔젤스 리사이클 나일론 시티 호보백.xlsx') #엑셀저장