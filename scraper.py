import csv
#import pytest
import time
import json
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
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--lang=vi"
]
for option in options:
    chrome_options.add_argument(option)
#driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# Mở trang web 10minutemail.net
driver.get("https://10minutemail.net")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'mailtext')))
email = driver.find_element("class name",'mailtext').get_attribute('value')
username, domain = email.split('@')
# Mở trang web trumvpn.pro
driver.get("https://trumvpn.pro/#/register")
driver.find_element(By.XPATH, "//div[@onclick=\'dong24h()\']").click()
#driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.XPATH, "//main[@id='main-container']/div/div/div/div/div[2]/div/div/div/div/input").send_keys(username)
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("63668890")
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control").send_keys("63668890")
driver.find_element(By.XPATH, "(//button[@type=\'button\'])[3]").click()
driver.execute_script("window.scrollTo(0,0)")
#loi {"method":"css selector","selector":"a > .text-center > div:nth-child(1)"}
wait = WebDriverWait(driver, 10)
element = driver.find_element(By.XPATH, "//main[@id='main-container']/div/div[2]/div/div/div[2]/a/div/div")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.LINK_TEXT, "Nhấp vào đây để đồng bộ máy chủ").click()
element = driver.find_element(By.LINK_TEXT, "Nhấp vào đây để đồng bộ máy chủ")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.LINK_TEXT, "Sao chép liên kết").click()

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
