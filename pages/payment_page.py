from pages.methods_page import BaseMethods
from appium.webdriver.common.appiumby import AppiumBy

class PaymentPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_title = "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV"
        self.payment_title_text = "Enter a payment method"
        self.review_btn = "com.saucelabs.mydemoapp.android:id/paymentBtn"
        self.fullname_card_field = "com.saucelabs.mydemoapp.android:id/nameET"
        self.card_number_field = "com.saucelabs.mydemoapp.android:id/cardNumberET"
        self.expiration_date_field = "com.saucelabs.mydemoapp.android:id/expirationDateET"
        self.security_code_field = "com.saucelabs.mydemoapp.android:id/securityCodeET"
        self.fullname_card_error = "com.saucelabs.mydemoapp.android:id/nameErrorTV"
        self.expiration_date_error = "com.saucelabs.mydemoapp.android:id/expirationDateErrorTV"
        self.security_code_error = "com.saucelabs.mydemoapp.android:id/securityCodeErrorTV"
        self.error_msg = "Value looks invalid."
        
    def click_review_btn(self):
        self.click_element(AppiumBy.ID, self.review_btn)
    
    def validate_full_name_card_error(self):
        return self.get_element_text(AppiumBy.ID, self.fullname_card_error)
    
    def full_name_card_error_is_shown_and_expcted(self):
        return self.validate_full_name_card_error() == self.error_msg
    
    def validate_expiration_date_error(self):
        return self.get_element_text(AppiumBy.ID, self.expiration_date_error)
    
    def expiration_date_error_is_shown_and_expected(self):
        return self.validate_expiration_date_error() == self.error_msg
    
    def validate_security_code_error(self):
        return self.get_element_text(AppiumBy.ID, self.security_code_error)
    
    def security_code_error_is_shown_and_expected(self):
        return self.validate_security_code_error() == self.error_msg