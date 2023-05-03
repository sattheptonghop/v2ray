import os
import datetime
import csv
import time
import json
import re
import requests
from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
# 2 | open | https://tnetz.pro/#/register | 
driver.get("https://tnetz.pro/")

iLoop = 0
oweb = re.search(r"(.*/#/)", driver.current_url).group(0)
while re.search(r"/#/(.*)",driver.current_url).group(1) != "dashboard" and driver.execute_script("return document.readyState") == "complete":
	try:
		element = driver.find_element(By.CSS_SELECTOR, ".tbclose-btn")
		element.click()
		print('dong thong bao')
	except:
		pass
	# 4 | click | linkText=Đăng ký | 
	if re.search(r"/#/(.*)",driver.current_url).group(1) == "login" and driver.execute_script("return document.readyState") == "complete":
		print(driver.current_url)
		print('Thu chuyen toi trang dang ky')
		try:
			#element = driver.find_element(By.LINK_TEXT, "Đăng ký")
			element = driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)")
			element.click()
			print('an dang ky')
		except:
			print('ko an duoc nut dang ky, thu chay bang link')
			#driver.get(oweb + "register")
			driver.get("https://tnetz.pro/#/register")
			pass
		time.sleep(1)
			
	if re.search(r"/#/(.*)",driver.current_url).group(1) == "register" and driver.execute_script("return document.readyState") == "complete":
		print("dang o trang dang ky")
		print(driver.current_url)
		#iemail = driver.find_element(By.CSS_SELECTOR, ".input-group > .form-control")
		#ipass1 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
		#ipass2 = driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
		try:
			time.sleep(1)
			iemail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']")))
			ipass1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type=\'password\'])")))
			ipass2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type=\'password\'])[2]")))
			#driver.implicitly_wait(3)
			if iemail.get_attribute("value"):
				print('sua lai email')
				#for i in range(10):
					#iemail.send_keys(Keys.BACKSPACE)
					#time.sleep(1)
					#pass
				try:
					oemail = iemail.get_attribute("value")
					iemail.clear()
					iemail.send_keys(oemail.split("@")[0])
					iemail.send_keys("1")
					iemail.send_keys("@gmail.com")
					#iemail.send_keys(oemail.split("@")[1])
				except Exception as e:
					print(e)
					pass
			else:
				
				print('Đăng ký và đăng nhập')
				ticket = driver.execute_script("return Math.random(). toString(36).substring(2,16)")
				iemail.send_keys(ticket)
				iemail.send_keys("@gmail.com")
				ipass1.send_keys("63668890")
				ipass2.send_keys("63668890")
				print('nhập xong')
			#driver.implicitly_wait(3)
			try:
				element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type=\'button\'])[2]")))
				#element = driver.find_element(By.XPATH, "//div[2]/button")
				element.location_once_scrolled_into_view
				element.click()
				time.sleep(1)
				print('pa1 dang ky')
			except:
				element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/button")))
				#element = driver.find_element(By.XPATH, "(//button[@type=\'button\'])[3]")
				driver.execute_script("arguments[0].scrollIntoView();", element)
				driver.execute_script("arguments[0].click();", element)
				time.sleep(1)
				print('pa2 dang ky')
				pass
			print(driver.current_url)
		except Exception as e:
			print("khong co iemail")
			driver.refresh()
			print(e)
			pass

	if iLoop == 15:
		iLoop = iLoop + 1
		break
if re.search(r"/#/(.*)",driver.current_url).group(1) == "dashboard":
	print('Trang quan tri dashboard')

	try:
		WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tbclose-btn"))).click()
		#driver.find_element(By.CSS_SELECTOR, ".tbclose-btn").click()
	except Exception as e:
		print('ko co qc sau khi dang nhap')
		pass

	print('Lấy link clash')
	try:
		element = driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .font-size-base")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		driver.execute_script("window.scrollTo(0,306)")
		driver.find_element(By.XPATH, "//main[@id=\'main-container\']/div/div[2]/div/div/div[2]/div/div[2]/a").click()
		#element = driver.find_element(By.LINK_TEXT, "Chuyển đến Clash For Android")
		element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, "Chuyển đến Clash For Android")))
		url = element.get_attribute("href")
		result = url.split("url=")[1].split("&name=")[0]
		print("result=")
		print(result)
		
		# Mở tệp CSV để ghi dữ liệu
		today = datetime.datetime.now()
		with open('tltvpncom', mode='r', newline='') as vpn_file:
			reader = csv.reader(vpn_file)
			rows = list(reader)
			countrow = len(rows)
			print("countrow=", countrow)

		# Ghi file mới với nội dung đã chỉnh sửa
		with open('tltvpncom', 'w', newline='') as file:
			writer = csv.writer(file)
			if countrow >= 24:
				print("số dòng hơn 24")
				for row in rows[1:]:
					writer.writerow(row)
			else:
				print("số dòng ít hơn 24")
				for row in rows:
					writer.writerow(row)
			writer.writerow([result])
	except Exception as e:
		print(e)
		pass
	print('Xong Lấy link clash')
	try:
		print('Thử đăng xuất')
		# 20 | mouseOver | css=.fa-angle-down | 
		element = driver.find_element(By.CSS_SELECTOR, ".fa-angle-down")
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()
		# ko tim thay
		#driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
	except Exception as e:
		print('Thất bại đăng xuất')
		#print(e)
		pass
	
# Đóng trình duyệt web
driver.close()
driver.quit()
