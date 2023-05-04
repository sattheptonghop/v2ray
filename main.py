#driver = 
from selenium.webdriver import Firefox
#service
from selenium.webdriver.firefox.service import Service
#_options
from selenium.webdriver.firefox.options import Options
#By.NAME
from selenium.webdriver.common.by import By

def test_google_search():
    # Khởi tạo Firefox Driver Service
    service = Service("/usr/bin/geckodriver")
    #service = Service("/usr/local/share/gecko_driver/geckodriver")
    service.start()
    #
    firefox_options = Options()
    firefox_options.headless = True
    # Khởi tạo trình duyệt Chrome
    driver = Firefox(service=service, options=firefox_options)
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
