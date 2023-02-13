from pages.base import WebPage
from pages.elements import WebElement


class RegPage(WebPage):
    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    header_text_l = WebElement(xpath = '//*[@id="page-right"]/div/div/h1')
    name_field = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    name = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    last_name_field = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    last_name = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    region_name_field = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    email_or_phone_name_field = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]')
    email_or_phone_name = WebElement(xpath = '//*[@id="address"]')
    password_field = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    password_input_field = WebElement(xpath = '//*[@id="password"]')
    conf_password_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    conf_password_input_field = WebElement(xpath = '//*[@id="password-confirm"]')
    register_btn = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/button')
    link_agreement_r = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[5]/a')
    logo_head = WebElement(xpath = '//*[@id="app-header"]/div/div/svg')

    name_absence = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    last_name_absence = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    email_or_phone_name_absence = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[3]/span')
    password_absence = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    conf_password_absence = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    mail_exist = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')
    password_symbol = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    password_cyrylic = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    password_repeat = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    password_real_cyr = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')











