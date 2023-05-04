#driver = Chrome
from selenium.webdriver import Chrome
#service
from selenium.webdriver.chrome.service import Service
#chrome_options
from selenium.webdriver.chrome.options import Options
#By.NAME
from selenium.webdriver.common.by import By

def test_google_search():
    # Khởi tạo Chrome Driver Service
    service = Service("/usr/bin/chromedriver")
    #service = Service("/usr/local/share/chrome_driver/chromedriver")
    service.start()
    #
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Khởi tạo trình duyệt Chrome
    driver = Chrome(service=service, options=chrome_options)
    # Mở trang Google
    driver.get('https://www.google.com')
    # Tìm ô tìm kiếm và nhập từ khóa "GitHub"
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('GitHub')
    search_box.submit()
    # Kiểm tra xem kết quả có chứa từ khóa "GitHub" không
    assert 'GitHub' in driver.title
    # Đóng trình duyệt
    driver.quit()

test_google_search()
