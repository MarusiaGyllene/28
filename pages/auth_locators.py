from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    auth_title_l = WebElement(xpath = '//*[@id="page-left"]/div/div[2]/h2')
    auth_text_l = WebElement(xpath = '//*[@id="page-left"]/div/div[2]/p')
    logo_left = WebElement(xpath = '//*[@id="page-left"]/div/div[1]')
    auth_title_r = WebElement(xpath = '//*[@id="page-right"]/div/div/h1')
    tab_telephone = WebElement(xpath = '//*[@id="t-btn-tab-phone"]')
    tab_mail = WebElement(xpath = '//*[@id="t-btn-tab-mail"]')
    input_element = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    input_psw = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    tab_login = WebElement(xpath = '//*[@id="t-btn-tab-login"]')
    tab_ls = WebElement(xpath = '//*[@id="t-btn-tab-ls"]')
    forget_psw = WebElement(xath = '//*[@id="forgot_password"]')
    link_agreement = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/a')
    vk = WebElement(xpath = '//*[@id="oidc_vk"]')

    phone = WebElement(id='username')
    password = WebElement(id='password')
    btn_login = WebElement(id='kc-login')
    registration_link = WebElement(id='kc-register')


    invalid_attention = WebElement(xpath = '//*[@id="form-error-message"]')


    invalid_login_or_pswrd = WebElement(xpath = '//*[@id="form-error-message"]')





