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
#
from selenium.webdriver.common.keys import Keys

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
username, domain = email.split('@')

# Mở trang web 10minutemail.net
#driver.close()
driver.get("https://trumvpn.pro/#/register")
# Tìm phần tử với class là "tbclose-btn" và gọi hàm click() (nếu phần tử tồn tại)
try:
    driver.find_element_by_css_selector(".tbclose-btn").click()
    print('Đóng bảng thành công')
except:
    print('Đóng bảng ko thành công')
    pass

# Tìm phần tử input bằng placeholder và nhập chữ
inpute_element = driver.find_element("xpath", "//input[@placeholder='Email']")
inpute_element.send_keys(username)
print('user ok')
# Tìm phần tử input bằng placeholder 'Mật khẩu' và nhập chữ 
input1_element = driver.find_element("xpath", "//main[@id='main-container']/div/div/div/div/div[2]/div/div/div[2]/input")
input1_element.send_keys("63668890")
print('pa1 pass 1 ok')
    # Tìm phần tử input bằng placeholder và nhập chữ
input2_element = driver.find_element("xpath", "//main[@id='main-container']/div/div/div/div/div[2]/div/div/div[3]/input")
input2_element.send_keys("63668890")
print('pa1 pass 2 ok')

    
# Tìm phần tử button bằng nội dung và click vào nó
driver.find_element("xpath", "//main[@id='main-container']/div/div/div/div/div[2]/div/div[2]/button").click()
# Tìm phần tử button bằng nội dung và click vào nó
driver.find_element("xpath", "//button[text()='Nhấp vào đây để đồng bộ máy chủ']").click()
# Tìm phần tử button bằng nội dung và click vào nó
driver.find_element("xpath", "//button[text()='Sao chép liên kết']").click()
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
