from pages.methods_page import BaseMethods
from appium.webdriver.common.appiumby import AppiumBy
from utils.logger import log

class LoginPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page_title = "com.saucelabs.mydemoapp.android:id/loginTV"
        self.login_page_title_text = "Login"
        self.login_btn = "com.saucelabs.mydemoapp.android:id/loginBtn"
        self.username_error = "com.saucelabs.mydemoapp.android:id/nameErrorTV"
        self.username_error_text = "Username is required"
        self.password_error = "com.saucelabs.mydemoapp.android:id/passwordErrorTV"
        self.password_error_text = "Enter Password"
        self.username_field = "com.saucelabs.mydemoapp.android:id/nameET"
        self.password_field = "com.saucelabs.mydemoapp.android:id/passwordET"
        self.username_list = "com.saucelabs.mydemoapp.android:id/username1TV"
        self.password_list = "com.saucelabs.mydemoapp.android:id/password1TV"

    def get_login_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.login_page_title)
    
    def login_title_is_shown_and_expected(self):
        return self.get_login_page_title() == self.login_page_title_text
    
    def click_login_btn(self):
        self.click_element(AppiumBy.ID, self.login_btn)
        
    def validate_username_error(self):
        return self.get_element_text(AppiumBy.ID, self.username_error)
    
    def username_error_is_shown_and_expected(self):
        return self.validate_username_error() == self.username_error_text
    
    def fill_username(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.username_field, text)

    def validate_password_error(self):
        return self.get_element_text(AppiumBy.ID, self.password_error)
    
    def password_error_is_shown_and_expected(self):
        return self.validate_password_error() == self.password_error_text
    
    def log_with_username_from_list(self):
        self.clear_field(AppiumBy.ID, self.username_field)
        usernames = self.get_elements_text(AppiumBy.ID, self.username_list)
        first_username = usernames[0]
        log.info(f"Logando com o usuário: {first_username}")
        return self.send_keys_to_element(AppiumBy.ID, self.username_field, first_username)
    
    def log_with_password_from_list(self):
        self.clear_field(AppiumBy.ID, self.password_field)
        passwords = self.get_elements_text(AppiumBy.ID, self.password_list)
        first_password = passwords[0]
        log.info(f"Inserindo a senha...")
        return self.send_keys_to_element(AppiumBy.ID, self.password_field, first_password)

    
