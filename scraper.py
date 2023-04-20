import csv
import pytest
import time
import json
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# Cho 10minutemail.net
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
chrome_options = Options()
options = [
	"--headless",
	"--window-size=800,1200",
	"start-maximized",
	"disable-infobars",
	"--disable-gpu",
	"--ignore-certificate-errors",
	"--disable-extensions",
	"--no-sandbox",
	"--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 1 | setWindowSize | 500x1200 | 
driver.set_window_size(360, 720)
# 2 | open | https://trumvpn.pro/ | 
#driver.get("https://trumvpn.pro/")
driver.get("https://trumvpn.pro/#/register")
# 3 | click | css=.tbclose-btn | 
driver.implicitly_wait(10)
try:
	element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
	element.click()
	print('dong thong bao')
except:
	pass
	
# 4 | click | linkText=Đăng ký | 
#try:
#	element = driver.find_element(By.LINK_TEXT, "Đăng ký")
#	element.click()
#	print('an dang ky')
#except:
#	pass
#driver.implicitly_wait(10)

# 7 | executeScript | return Math.random(). toString(36).substring(2,16) | ticket
ticket = driver.execute_script("return Math.random(). toString(36).substring(2,16)")
# 8 | type | css=.input-group > .form-control | ${ticket}
driver.find_element(By.CSS_SELECTOR, ".input-group > .form-control").send_keys(ticket)
# 10 | type | css=.form-group:nth-child(2) > .form-control | 63668890
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("63668890")
# 12 | type | css=.form-group:nth-child(3) > .form-control | 63668890
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control").send_keys("63668890")
# 13 | click | xpath=(//button[@type='button'])[3] | 
print('Đăng ký và đăng nhập')
while driver.current_url != "https://trumvpn.pro/#/dashboard":
	try:
		element = driver.find_element(By.XPATH, "(//button[@type=\'button\'])[3]")
		element.location_once_scrolled_into_view
		element.click()
		print('pa1')
		print(driver.current_url)
	except:
		element = driver.find_element(By.XPATH, "(//button[@type=\'button\'])[3]")
		driver.execute_script("arguments[0].scrollIntoView();", element)
		driver.execute_script("arguments[0].click();", element)
		print('pa2')
		print(driver.current_url)
		pass
	# 8 | type | css=.input-group > .form-control | ${ticket}
	try:
		driver.implicitly_wait(10)
		driver.find_element(By.CSS_SELECTOR, ".input-group > .form-control").send_keys("1")
	except:
		pass
print('Đăng ký và đăng nhập thành công')

try:
	driver.find_element(By.CSS_SELECTOR, ".tbclose-btn").click()
except Exception as e:
	print(e)
	pass
try:
	# 14 | mouseOver | css=.row:nth-child(1) .font-size-base | 
	element = driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .font-size-base")
	actions = ActionChains(driver)
	actions.move_to_element(element).perform()
	# 15 | runScript | window.scrollTo(0,306) | 
	driver.execute_script("window.scrollTo(0,306)")
	# 16 | click | xpath=//main[@id='main-container']/div/div[2]/div/div/div[2]/div/div[2]/a | 
	driver.find_element(By.XPATH, "//main[@id=\'main-container\']/div/div[2]/div/div/div[2]/div/div[2]/a").click()
	# 17 | mouseOver | linkText=Clash | 
	element = driver.find_element(By.LINK_TEXT, "Chuyển đến Clash For Android")
	url = element.get_attribute("href")
	result = url.split("url=")[1].split("&name=")[0]
	print("result=")
	print(result)
except Exception as e:
	print(e)
	pass

# 20 | mouseOver | css=.fa-angle-down | 
#element = driver.find_element(By.CSS_SELECTOR, ".fa-angle-down")
#actions = ActionChains(driver)
#actions.move_to_element(element).perform()
# 21 | mouseOver | css=.ant-dropdown-trigger:nth-child(5) | 
#element = driver.find_element(By.CSS_SELECTOR, ".ant-dropdown-trigger:nth-child(5)")
#actions = ActionChains(driver)
#actions.move_to_element(element).perform()
# 22 | click | linkText=Đăng xuất | 
#driver.find_element(By.LINK_TEXT, "Đăng xuất").click()

# Tạo một bộ sưu tập dữ liệu trống để lưu trữ tiêu đề
data = [['V2ray trumvpn.pro']]
# Thêm tiêu đề vào bộ sưu tập dữ liệu
data.append([result])
# Mở tệp CSV để ghi dữ liệu
with open('google_title.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# Đóng trình duyệt web
driver.close()
driver.quit()
