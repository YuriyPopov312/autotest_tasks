from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseApp():

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except:
            self.driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

    def go_to_site(self, url):
        self.driver.get(url)
        return {}

    def find_element(self, locator, time=10):
        return WDW(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Елемент с локатором: {locator} - не найден")

    def find_elements(self, locator, time=10):
        return WDW(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Елементы с локатором: {locator} - не найдены ")

    def curr_url_is(self, url_chek):  # Ссылка по начатию "Картинки": https://yandex.ru/images/?utm_source=main_stripe_big.  
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_url = self.driver.current_url
        return new_url.startswith(url_chek)