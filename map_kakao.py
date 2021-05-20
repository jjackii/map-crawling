from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(5)

driver.get("https://map.kakao.com/")


def call(point):
    # 길찾기 btn
    driver.find_element_by_css_selector('#search\.tab2 > a').send_keys(Keys.ENTER)

    # 경유지 추가
    for i in range(2, len(point)):
        driver.find_element_by_xpath('//*[@id="info.route.searchBox.toggleVia"]').send_keys(Keys.ENTER)
        time.sleep(1.5)

    # 경유지 입력
    for i in range(len(point)):
        try:
            box = driver.find_element_by_css_selector('#info\.route\.waypointSuggest\.input'+str(i))
            box.send_keys(point[i])
            box.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            pass

    # 차로 이동
    driver.find_element_by_xpath('//*[@id="cartab"]').send_keys(Keys.ENTER)
    time.sleep(2)

    # 시간
    via_time = driver.find_elements_by_css_selector("span.time")

    for t in via_time:
        return t.text
    
point = input("> ").split()
call(point)