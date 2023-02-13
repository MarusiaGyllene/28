import pytest
from pages.auth_locators import AuthPage
from pages.reg_locators import RegPage
from settings import *
from selenium import webdriver

#Тест 1
#Проверка элементов в левом блоке страницы Авторизация
def test_left_page(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.auth_title_r.get_text() == 'Авторизация'
    assert auth_page.tab_telephone.is_clickable()
    assert auth_page.tab_mail.is_clickable()
    assert auth_page.tab_login.is_clickable()
    assert auth_page.tab_ls.is_clickable()
    assert auth_page.btn_login.is_clickable()
    assert auth_page.link_agreement.is_clickable()
    assert auth_page.registration_link.is_clickable()

#Тест 2
#Проверка элементов в правом блоке страницы Авторизация
def test_right_page(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.logo_left.is_presented()
    assert auth_page.auth_title_l.get_text() == 'Личный кабинет'
    assert auth_page.auth_text_l.get_text() == 'Персональный помощник в цифровом мире Ростелекома'


#Тест 3
#Проверка названия вкладки "Номер"
@pytest.mark.skip(reason="Наименование Таба выбора аутентификации по номеру не соотвествует ТЗ")
def test_phone(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_telephone.get_text() == 'Номер'
    assert auth_page.input_element.get_text() == 'Номер'
    assert auth_page.input_psw.get_text() == 'Пароль'


#Тест 4
#Проверка названия вкладки "Почта"
@pytest.mark.skip(reason="Наименование формы ввода для почты не соотвествует ТЗ")
def test_mail(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_mail.get_text() == 'Почта'
    auth_page.tab_mail.click()
    assert auth_page.input_element.get_text() == 'Логин'
    assert auth_page.input_psw.get_text() == 'Пароль'

#Тест 5
#Проверка названия вкладки "Логин"
@pytest.mark.skip(reason="Наименование формы ввода для логина не соотвествует ТЗ")
def test_login(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_login.get_text() == 'Логин'
    auth_page.tab_login.click()
    assert auth_page.input_element.get_text() == 'Почта'
    assert auth_page.input_psw.get_text() == 'Пароль'

#Тест 6
#Проверка названия вкладки "Лицевой счет"
def test_ls(web_browser):
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_ls.get_text() == 'Лицевой счёт'
    auth_page.tab_ls.click()
    assert auth_page.input_element.get_text() == 'Лицевой счёт'
    assert auth_page.input_psw.get_text() == 'Пароль'

#Тест 7
#Проверка Авторизации - ввод неверного номера и пароля
def test_wrong(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.phone.send_keys('yerafop764@otanhome.com')
    auth_page.password.send_keys('password')
    auth_page.btn_login.click()
    assert auth_page.invalid_attention.get_text() == 'Неверный логин или пароль'
    #assert auth_page.invalid_attention.get_text() == 'Неверно введен текст с картинки'


#Тест 8
#Проверка элементов в левом блоке страницы Регистрация
@pytest.mark.skip(reason="Содержание не соотвествует ТЗ")
def test_left_page_reg(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.logo_left.is_presented()
    assert reg_page.auth_title_l.get_text() == 'Личный кабинет'
    assert reg_page.auth_text_l.get_text() == 'Персональный помощник в цифровом мире Ростелекома'

#Тест 9
#Проверка элементов в правом блоке страницы Регистрация
def test_right_page_reg(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.header_text_l.get_text() == 'Регистрация'
    assert reg_page.name_field.get_text() == 'Имя'
    assert reg_page.last_name_field.get_text() == 'Фамилия'
    assert reg_page.region_name_field.get_text() == 'Регион'
    assert reg_page.email_or_phone_name_field.get_text() == 'E-mail или мобильный телефон'
    assert reg_page.password_field.get_text() == 'Пароль'
    assert reg_page.conf_password_field.get_text() == 'Подтверждение пароля'
    assert reg_page.register_btn.is_clickable()
    assert reg_page.link_agreement_r.is_clickable()

#Тест 10
#Проверка названия Кнопки
@pytest.mark.skip(reason="Наименование кнопки на странице Регистрация не соотвествует ТЗ")
def test_btn_right_page_reg(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.register_btn.get_text() == 'Продолжить'

#Тест 11
#Проверка Регистрации пользователя с пустым полем "Имя", появление текста с подсказкой об ошибке
def test_name_absence(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys('')
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.name_absence.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Тест 12
#Проверка Регистрации пользователя с пустым полем "Фамилия", появление текста с подсказкой об ошибке
def test_last_name_absence(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys('')
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.last_name_absence.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Тест 13
#Проверка Регистрации пользователя с пустым полем "E-mail или мобильный телефон", появление текста с подсказкой об ошибке
def test_email_or_phone_name_absence(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys('')
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.email_or_phone_name_absence.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Тест 14
#Проверка Регистрации пользователя с пустым полем "Пароль", появление текста с подсказкой об ошибке
def test_password_absence(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys('')
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.password_absence.get_text() == 'Длина пароля должна быть не менее 8 символов'

#Тест 15
#Проверка Регистрации пользователя с пустым полем "Подтверждение пароля", появление текста с подсказкой об ошибке
def test_conf_password_absence(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys('')
    reg_page.register_btn.click()
    assert reg_page.conf_password_absence.get_text() == 'Длина пароля должна быть не менее 8 символов'

#Тест 16
#Проверка Регистрации пользователя со значением в поле "Имя" меньше 2 символов, появление текста с подсказкой об ошибке
def test_name_less(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(bad_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.name_absence.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Тест 17
#Проверка Регистрации пользователя со значением в поле Фамилия" превышающим 30 символов,, появление текста с подсказкой об ошибке
def test_last_name_more(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(bad_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.last_name_absence.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Тест 18
#Проверка Регистрации пользователя с с невалидным значением поля "E-mail или мобильный телефон", появление текста с подсказкой об ошибке
def test_mail_invalid(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(bad_mail)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.email_or_phone_name_absence.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Тест 19
#Проверка Регистрация пользователя с уже зарегистрированным E-mail, появление оповещения, что пользователь существует
def test_mail_exist(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(valid_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(example_password)
    reg_page.register_btn.click()
    assert reg_page.mail_exist.get_text() == 'Учётная запись уже существует'

#Тест 20
#Проверка Регистрация пользователя со значением в поле "Пароль" менее 8 символов, появление текста с подсказкой об ошибке
def test_password_less(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(short_password)
    reg_page.conf_password_input_field.send_keys(short_password)
    reg_page.register_btn.click()
    assert reg_page.password_absence.get_text() == 'Длина пароля должна быть не менее 8 символов'


#Тест 21
#Проверка Регистрация пользователя со значением в поле "Пароль" только латинские буквы, появление текста с подсказкой об ошибке
def test_password_only_latin(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(latin_password)
    reg_page.conf_password_input_field.send_keys(latin_password)
    reg_page.register_btn.click()
    assert reg_page.password_symbol.get_text() == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'


#Тест 22
#Проверка Регистрация пользователя со значением в поле "Пароль" только буквы кириллицы, появление текста с подсказкой об ошибке
def test_password_only_cyrilic(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(cyrilic_password)
    reg_page.conf_password_input_field.send_keys(cyrilic_password)
    reg_page.register_btn.click()
    assert reg_page.password_cyrylic.get_text() == 'Пароль должен содержать только латинские буквы'


#Тест 23
#Проверка Регистрация пользователя со значением в поле "Пароль" только латинские буквы и цифры, появление текста с подсказкой об ошибке
def test_password_lowcase(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(lowcase_password)
    reg_page.conf_password_input_field.send_keys(lowcase_password)
    reg_page.register_btn.click()
    assert reg_page.password_cyrylic.get_text() == 'Пароль должен содержать хотя бы одну заглавную букву'


#Тест 24
#Проверка Регистрация пользователя с разными паролями, появление текста с подсказкой об ошибке
def test_different_password(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(example_password)
    reg_page.conf_password_input_field.send_keys(texample_password)
    reg_page.register_btn.click()
    assert reg_page.password_repeat.get_text() == 'Пароли не совпадают'


#Тест 25
#Проверка Регистрация пользователя со значением в поле "Пароль" только буквы кириллицы цифры, появление текста с подсказкой об ошибке
def test_valid_cyrilic_password(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name.send_keys(example_name)
    reg_page.last_name.send_keys(example_last_name)
    reg_page.email_or_phone_name.send_keys(example_email)
    reg_page.password_input_field.send_keys(cyr_password)
    reg_page.conf_password_input_field.send_keys(cyr_password)
    reg_page.register_btn.click()
    assert reg_page.password_real_cyr.get_text() == 'Пароль должен содержать только латинские буквы'

