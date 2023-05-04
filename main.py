from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

def test_google_search():
    # Khởi tạo Chrome Driver Service
    service = Service("/usr/bin/chromedriver")
    #service = Service("/usr/local/share/chrome_driver/chromedriver")
    service.start()
    # Khởi tạo trình duyệt Chrome
    driver = Chrome()
    # Mở trang Google
    driver.get('https://www.google.com')
    # Tìm ô tìm kiếm và nhập từ khóa "GitHub"
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('GitHub')
    search_box.submit()
    # Kiểm tra xem kết quả có chứa từ khóa "GitHub" không
    assert 'GitHub' in driver.title
    # Đóng trình duyệt
    driver.quit()

test_google_search()
