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
username, domain = email.split('@')

# Mở trang web 10minutemail.net
#driver.close()
driver.get("https://trumvpn.pro/#/register")
# Tìm phần tử với class là "tbclose-btn" và gọi hàm click() (nếu phần tử tồn tại)
try:
    close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tbclose-btn")))
    close_button.click()
    print('Đóng bảng thành công')
except:
    print('Đóng bảng ko thành công')
    pass
try:
    lang_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-dropdown-trigger btn btn-black mr-1")))
    lang_button.click()
    langvn_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "Tiếng Việt")))
    langvn_button.click()
    print('Chuyển tiếng việt thành công')
except:
    print('Chuyển tiếng việt ko thành công')
    pass

# Tìm phần tử input bằng placeholder và nhập chữ
inpute_element = driver.find_element("xpath", "//input[@placeholder='Email']")
inpute_element.send_keys(username)
print('user ok')
#try:
    # Tìm phần tử input bằng placeholder 'Mật khẩu' và nhập chữ 
    #input1_element = driver.find_element("xpath", "//input[@placeholder='password']")
    #input1_element.send_keys("63668890")
    #print('pa1 pass 1 ok')
    # Tìm phần tử input bằng placeholder và nhập chữ
    #input2_element = driver.find_element("xpath", "//input[@placeholder='password']")[2]
    #input2_element.send_keys("63668890")
    #print('pa1 pass 2 ok')
#except:
Keys.current_frame.send_keys(Keys.TAB)
Keys.current_frame.send_keys(Keys.TAB)
Keys.current_frame.send_keys(Keys.TAB)
Keys.current_frame.send_keys("63668890")
print('pa2 pass 1 ok')
Keys.current_frame.send_keys(Keys.TAB)
Keys.current_frame.send_keys("63668890")
print('pa2 pass 2 ok')
    #pass
    
# Tìm phần tử button bằng nội dung và click vào nó
buttondk_element = driver.find_element("xpath", "//button[text()='Register']")
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
