import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.kakao.com/")

start = "김포공항"
destination = "고려대 서울캠퍼스"
via = "서울역"

driver.find_element_by_xpath('//*[@id="search.tab2"]/a').send_keys(Keys.ENTER)

s_box = driver.find_element_by_css_selector('#info\.route\.waypointSuggest\.input0') 
s_box.send_keys(start)
s_box.send_keys(Keys.ENTER)
time.sleep(2)

# d_box = driver.find_element_by_id('info\.route\.waypointSuggest\.input1')
d_box = driver.find_element_by_css_selector('#info\.route\.waypointSuggest\.input1')
# driver.execute_script("arguments[0].click();", d_box)
d_box.send_keys(destination)
d_box.send_keys(Keys.ENTER)
time.sleep(1.5)

driver.find_element_by_xpath('//*[@id="info.route.searchBox.toggleVia"]').send_keys(Keys.ENTER)
time.sleep(1.5)

v_box = driver.find_element_by_css_selector('#info\.route\.waypointSuggest\.input1')
v_box.send_keys(via)
v_box.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="cartab"]').send_keys(Keys.ENTER)
# time.sleep(2)

# info = []

# # container = driver.find_elements_by_css_selector("div.contents")

# # for e in container:
# #     print(type(e))
# #     info.append(e.text)
# #     print(e.text)

# time = driver.find_elements_by_css_selector("span.time")
# distance = driver.find_elements_by_css_selector("span.distance").text
# fare = driver.find_elements_by_css_selector("span.taxi").text

# for t in time:
#     print(t.text)

# time = driver.find_elements_by_css_selector("span.time")
# for t in time:
#     info.append(t.text)
# #     print(t.text)
    
# distance = driver.find_elements_by_css_selector("span.distance")
# for d in distance:
#     info.append(d.text)
# #     print(d.text)
    
# fare = driver.find_elements_by_css_selector("span.taxi")
# for f in fare:
#     info.append(f.text)
# #     print(f.text)

# print(info)

# df = pd.DataFrame(info) # columns=['Time','Distance', 'Fare']
# df.to_csv("abc.csv")

# df = pd.DataFrame(info)
# df.to_csv("C:/Users/User/Desktop/abc.csv", header=False, index=False)