import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# Cho 10minutemail.net
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Mở trang web 10minutemail.net
driver.get("https://10minutemail.net")

# Chờ cho trang web tải hoàn tất
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'mailtext')))

# Lấy địa chỉ email mới
email = driver.find_element("class name",'mailtext').get_attribute('value')

# Mở trang web 10minutemail.net
driver.get("https://trumvpn.pro/#/register")

# Tìm phần tử button bằng nội dung và click vào nó
button24h_element = driver.find_element("xpath", "//button[text()='Tắt trong 24h']")
button24h_element.click()
# Tìm phần tử input bằng placeholder và nhập chữ
inpute_element = driver.find_element("xpath", "//input[@placeholder='Email']")

inpute_element.send_keys(email)
# Tìm phần tử input bằng placeholder 'Mật khẩu' và nhập chữ 
input1_element = driver.find_element("xpath", "//input[@placeholder='Mật khẩu']")
input1_element.send_keys("63668890")
# Tìm phần tử input bằng placeholder và nhập chữ
input2_element = driver.find_element("xpath", "//input[@placeholder='Nhập lại mật khẩu']")
input2_element.send_keys("63668890")
# Tìm phần tử button bằng nội dung và click vào nó
buttondk_element = driver.find_element("xpath", "//button[text()='Đăng ký']")
buttondk_element.click()
# Tìm phần tử button bằng nội dung và click vào nó
buttondb_element = driver.find_element("xpath", "//button[text()='Nhấp vào đây để đồng bộ máy chủ']")
buttondb_element.click()
# Tìm phần tử button bằng nội dung và click vào nó
buttonsc_element = driver.find_element("xpath", "//button[text()='Sao chép liên kết']")
buttonsc_element.click()
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
driver.quit()
