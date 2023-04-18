from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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

# Mở trang web Google
driver.get("https://www.google.com")

# Lấy tiêu đề của trang
title = driver.title

# Tạo một bộ sưu tập dữ liệu trống để lưu trữ tiêu đề
data = [['Tiêu đề của trang']]

# Thêm tiêu đề vào bộ sưu tập dữ liệu
data.append([title])

# Mở tệp CSV để ghi dữ liệu
with open('google_title.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Đóng trình duyệt web
driver.quit()
