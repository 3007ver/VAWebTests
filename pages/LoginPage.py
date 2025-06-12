from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
        self.find_element(LoginPageLocators.RECOVERY_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
         self.attach_screenshot()
         self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле "Логин"')
    def set_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()


