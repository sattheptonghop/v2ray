import csv
import pytest
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
    "--window-size=800,1200",
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
driver.set_window_size(800, 1200)
driver.get("https://10minutemail.net")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'mailtext')))
email = driver.find_element("class name",'mailtext').get_attribute('value')
username, domain = email.split('@')
# Mở trang web trumvpn.pro
driver.get("https://trumvpn.pro/#/register")
try:
    driver.find_element(By.CSS_SELECTOR, ".tbclose-btn").click()
except:
    pass
#driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
driver.find_element(By.XPATH, "//main[@id='main-container']/div/div/div/div/div[2]/div/div/div/div/input").send_keys(username)
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("63668890")
driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control").send_keys("63668890")
try:
    driver.find_element(By.XPATH, "(//button[@type=\'button\'])[3]").click()
    print ("andk=pa1")
except:
    element = driver.find_element(By.XPATH, "//main[@id='main-container']/div/div/div/div/div[2]/div/div[2]/button")
    driver.execute_script("arguments[0].click();", element)
    print ("andk=pa2")
    pass
print (driver.current_url)
try:
    # 14 | mouseOver | css=.row:nth-child(1) .font-size-base | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .font-size-base")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    print("ko co xpath=//h5[contains(.,'Hướng dẫn đăng ký nền tiktok Free 7 ngày')]")
except:
    pass
# 15 | runScript | window.scrollTo(0,306) | 
driver.execute_script("window.scrollTo(0,306)")
# 16 | click | linkText=Nhấp vào đây để đồng bộ máy chủ | 
try:
    driver.find_element(By.XPATH, "//a[contains(.,'Nhấp vào đây để đồng bộ máy chủ')]").click()
    print("getdk=1")
except:
    pass
try:
    driver.find_element(By.XPATH, "//div[2]/div/div[2]/a").click()
    print("getdk=2")
except:
    pass
try:
    driver.find_element(By.XPATH, "//main[@id='main-container']/div/div[2]/div/div/div[2]/div/div[2]/a").click()
    print("getdk=3")
except:
    pass
# 17 | mouseOver | linkText=Sao chép liên kết | 
element = driver.find_element(By.LINK_TEXT, "Sao chép liên kết")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 17 | mouseOver | linkText=Sao chép liên kết | 
element = driver.find_element(By.LINK_TEXT, "Sao chép liên kết")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 18 | mouseOut | linkText=Sao chép liên kết | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 19 | click | linkText=Sao chép liên kết | 
driver.find_element(By.LINK_TEXT, "Sao chép liên kết").click()
# 20 | mouseOver | css=.fa-angle-down | 
element = driver.find_element(By.CSS_SELECTOR, ".fa-angle-down")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 21 | mouseOver | css=.ant-dropdown-trigger:nth-child(5) | 
element = driver.find_element(By.CSS_SELECTOR, ".ant-dropdown-trigger:nth-child(5)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 22 | click | linkText=Đăng xuất | 
driver.find_element(By.LINK_TEXT, "Đăng xuất").click()

# Lấy giá trị từ bộ nhớ ra và gán vào biến result
result = driver.execute_script("return window.getSelection().toString();")
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
