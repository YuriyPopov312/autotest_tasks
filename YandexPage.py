from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 

from BasePage import BaseApp


class ElementLocators():
    LOCATOR_YANDEX_SEARCH_STRING = (By.XPATH, '//*[@id="text"]')
    LOCATOR_YANDEX_SUGGEST = (By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile.mini-suggest__popup_visible")
    LOCATOR_YANDEX_SEARCH_RESULT_TABLE = (By.ID, "search-result")
    LOCATOR_YANDEX_FIRST_RESULT = (By.XPATH, '//*[@id="search-result"]/li[1]')
    LOCATOR_YANDEX_TEXT_PICTURES = (By.XPATH, '//*[@data-id="images"]/div[contains(@class,"services-new__item-title")]')
    LOCATOR_YANDEX_LINK_PICTURES = (By.XPATH, '//*[@data-id="images"]')
    LOCATOR_FIRST_CATEGORY_PICTURES = (By.CSS_SELECTOR, "div.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a")
    LOCATOR_NAME_CATEGORY = (By.XPATH, "/html/body")
    LOCATOR_FIRST_PICTURE = (By.XPATH, "//div[contains(@class,'serp-item_pos_0')]")
    LOCATOR_BUTTON_NEXT = (By.XPATH, "//div[contains(@class,'MediaViewer_theme_fiji-ButtonNext')]/i")
    LOCATOR_BUTTON_BACK = (By.XPATH, "//div[contains(@class,'MediaViewer_theme_fiji-ButtonPrev')]/i")
    LOCATOR_OPEN_PICTURE = (By.XPATH, "//img[contains(@class,'MMImage-Origin')]")


class WorkTools(BaseApp):

    def query_entry(self, query):
        search_string = self.find_element(ElementLocators.LOCATOR_YANDEX_SEARCH_STRING)
        search_string.click()
        search_string.send_keys(query)
        return search_string

    def confirm_search(self):
        search_string = self.find_element(ElementLocators.LOCATOR_YANDEX_SEARCH_STRING).send_keys(Keys.RETURN)

    def check_suggest(self):
        try:
            suggest = self.find_element(ElementLocators.LOCATOR_YANDEX_SUGGEST)
        except NoSuchElementException:
            return False
        return True

    def check_search_result_table(self):
        try:
            result_table = self.find_element(ElementLocators.LOCATOR_YANDEX_SEARCH_RESULT_TABLE)
        except NoSuchElementException:
            return False
        return True

    def check_where_link(self, link):
        try:
            first_result = self.find_element(ElementLocators.LOCATOR_YANDEX_FIRST_RESULT)
            searched_link = first_result.find_element(By.XPATH, f'//a[contains(@href,"https://{link}/")]').get_attribute("href") #проверяем наличие тега с ссылкой tensor.ru
        except NoSuchElementException:
            return False
        return True

    def check_text(self, text_link):
        pictures_text = self.find_element(ElementLocators.LOCATOR_YANDEX_TEXT_PICTURES).get_attribute('innerHTML') #ищем "Картинки" на странице
        if text_link == str(pictures_text):
            return True
        else:
            return False

    def click_to_pictures(self):
        pictures_link = self.find_element(ElementLocators.LOCATOR_YANDEX_LINK_PICTURES)
        pictures_link.click()

    def click_first_category(self):
        first_category = self.find_element(ElementLocators.LOCATOR_FIRST_CATEGORY_PICTURES)
        first_category.click()

    def selected_name_category(self):
        first_category = self.find_element(ElementLocators.LOCATOR_FIRST_CATEGORY_PICTURES)
        name_category = first_category.find_element(By.XPATH, "//div[contains(@class,'PopularRequestList-SearchText')]").get_attribute('innerHTML')
        return str(name_category)

    def search_field_valid(self, name_category):
        full_text = self.find_element(ElementLocators.LOCATOR_NAME_CATEGORY).get_attribute("innerHTML")
        index = str(full_text).find(f'SearchText">{name_category}')  # Проверяем название выбранной категории путем вхождения строки в html стрницу.  
        if index != -1:  # Обычно шаблон находит около 9000 - ого символа.  
            return True
        else:
            return False

    def click_first_picture(self):
        picture = self.find_element(ElementLocators.LOCATOR_FIRST_PICTURE)
        picture.click()

    def get_link_picture_and_check_is_open(self):
        try:
            src_picture = self.find_element(ElementLocators.LOCATOR_OPEN_PICTURE).get_attribute("src")  # Если сработало исключение, картинка не нашлась (не открылась).  
            return src_picture
        except NoSuchElementException:
            return False


    def click_btn_next(self):
        btn_next = self.find_element(ElementLocators.LOCATOR_BUTTON_NEXT)
        btn_next.click()

    def click_btn_back(self):
        btn_back = self.find_element(ElementLocators.LOCATOR_BUTTON_BACK)
        btn_back.click()

    def is_open_picture(self, src_picture):
        open_picture = self.find_element(ElementLocators.LOCATOR_OPEN_PICTURE)
        src_open = open_picture.get_attribute("src")
        if str(src_picture) == str(src_open):  # Сравнение ресурсов для проверки соответствия страницы необходимой.  
            return True
        else:
            return False

    def is_picture_change(self, src_past_picture):
        current_picture = self.find_element(ElementLocators.LOCATOR_OPEN_PICTURE)
        src_current_picture = current_picture.get_attribute("src")
        if str(src_current_picture) != str(src_past_picture):  # Сравниваем ресурсы чтобы убедиться, что картинка на экране поменялась.  
            return True
        else:
            return False