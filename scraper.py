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
    "--disable-dev-shm-usage"
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
email = driver.find_element_by_class_name('mailtext').get_attribute('value')

# Tạo một bộ sưu tập dữ liệu trống để lưu trữ tiêu đề
data = [['Tiêu đề của trang']]

# Thêm tiêu đề vào bộ sưu tập dữ liệu
data.append([email])

# Mở tệp CSV để ghi dữ liệu
with open('google_title.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Đóng trình duyệt web
driver.quit()
