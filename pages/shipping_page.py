from pages.methods_page import BaseMethods
from appium.webdriver.common.appiumby import AppiumBy

class ShippingPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.shipping_title = "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV"
        self.shipping_title_text = "Enter a shipping address"
        self.payment_btn = "com.saucelabs.mydemoapp.android:id/paymentBtn"
        self.full_name_field = "com.saucelabs.mydemoapp.android:id/fullNameET"
        self.address_line1_field = "com.saucelabs.mydemoapp.android:id/address1ET"
        self.address_line2_field = "com.saucelabs.mydemoapp.android:id/address2ET"
        self.city_field = "com.saucelabs.mydemoapp.android:id/cityET"
        self.state_field = "com.saucelabs.mydemoapp.android:id/stateET"
        self.zip_field = "com.saucelabs.mydemoapp.android:id/zipET"
        self.country_field = "com.saucelabs.mydemoapp.android:id/countryET"
        self.full_name_error = "com.saucelabs.mydemoapp.android:id/fullNameErrorTV"
        self.full_name_error_text = "Please provide your full name."
        self.address_error = "com.saucelabs.mydemoapp.android:id/address1ErrorTV"
        self.address_error_text = "Please provide your address."
        self.city_error = "com.saucelabs.mydemoapp.android:id/cityErrorTV"
        self.city_error_text = "Please provide your city."
        self.zip_error = "com.saucelabs.mydemoapp.android:id/zipErrorTV"
        self.zip_error_text = "Please provide your zip"
        self.country_error = "com.saucelabs.mydemoapp.android:id/countryErrorTV"
        self.country_error_text = "Please provide your"

    def click_payment_btn(self):
        self.click_element(AppiumBy.ID, self.payment_btn)

    def validate_full_name_error(self):
        return self.get_element_text(AppiumBy.ID, self.full_name_error)

    def full_name_error_is_shown_and_expected(self):
        return self.validate_full_name_error() == self.full_name_error_text

    def validate_address_error(self):
        return self.get_element_text(AppiumBy.ID, self.address_error)

    def address_error_is_shown_and_expected(self):
        return self.validate_address_error() == self.address_error_text
    
    def validate_city_error(self):
        return self.get_element_text(AppiumBy.ID, self.city_error)
    
    def city_error_is_shown_and_expected(self):
        return self.validate_city_error() == self.city_error_text
    
    def validate_zip_error(self):
        return self.get_element_text(AppiumBy.ID, self.zip_error)
    
    def zip_error_is_shown_and_expected(self):
        return self.validate_zip_error() == self.zip_error_text
    
    def validate_country_error(self):
        return self.get_element_text(AppiumBy.ID, self.country_error)
    
    def country_error_is_shown_and_expected(self):
        return self.validate_country_error() == self.country_error_text
    
    def fill_full_name(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.full_name_field, text)

    def fill_address1(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.address_line1_field, text)

    def fill_address2(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.address_line2_field, text)

    def fill_city(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.city_field, text)

    def fill_state(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.state_field, text)

    def fill_zip_code(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.zip_field, text)

    def fill_country(self, text):
        return self.send_keys_to_element(AppiumBy.ID, self.country_field, text)
    

    
