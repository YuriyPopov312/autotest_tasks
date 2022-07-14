from YandexPage import WorkTools


def test_number_one():
    yandex_page = WorkTools()
    yandex_page.go_to_site("https://yandex.ru/")                 # Переход на ссайт яндекса.  
    yandex_page.query_entry("тензор")                            # Ввод в строку поиска запроса "тензор".  
    assert yandex_page.check_suggest() == True                   # Проверка отображения подсказок на экране.  
    yandex_page.confirm_search()                                 # Подтверждение ввода, нажатием "Enter".  
    assert yandex_page.check_search_result_table() == True       # Проверка отображения таблицы результата запроса.  
    assert yandex_page.check_where_link("tensor.ru") == True     # Проверка того, что первая ссылка "tensor.ru".  

def test_number_two():
    yandex_page = WorkTools()
    yandex_page.go_to_site("https://yandex.ru/")                                            # Переход на ссайт яндекса.  
    assert yandex_page.check_text("Картинки") == True                                       # Проверка отображения "Картинки" на экране.  
    yandex_page.click_to_pictures()                                                         # Кликаем по ссылке.  
    assert yandex_page.curr_url_is("https://yandex.ru/images/") == True                     # Проверяем, что перешли на url https://yandex.ru/images/. 
    yandex_page.click_first_category()                                                      # открываем первую категорию.  
    assert yandex_page.search_field_valid(yandex_page.selected_name_category()) == True     # Проверяем, что название категории отображается в поле поиска.  
    yandex_page.click_first_picture()                                                       # Открываем первую картинку.  
    picture_from_step_8 = yandex_page.get_link_picture_and_check_is_open()                  # Проверяем открылась ли картинка(если нет, ошибка - NoSuchElementException) и берем его src на будущее.  
    yandex_page.click_btn_next()                                                            # Нажимаем кнопку вперед.  
    assert yandex_page.is_picture_change(picture_from_step_8) == True                       # Проверяем поменялась ли картинка(путем сравнения src это картинки и прошлой).  
    yandex_page.click_btn_back()                                                            # Нажимаем кнопку назад.  
    assert yandex_page.is_open_picture(picture_from_step_8) == True                         # Проверяем, что вернулась картинка из шага 8.   


