from pages.methods_page import BaseMethods
from appium.webdriver.common.appiumby import AppiumBy

class OrangeBackpack(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "productTV"
        self.orange_backpack_xpath = "//android.widget.TextView[@content-desc='Product Title' and @text='Sauce Labs Backpack (orange)']/../android.widget.ImageView"
        self.backpack_title = "Sauce Labs Backpack (orange)"
        self.decrease_quantity_id = "com.saucelabs.mydemoapp.android:id/minusIV"
        self.increase_quantity_id = "com.saucelabs.mydemoapp.android:id/plusIV"
        self.cart_btn_id = "com.saucelabs.mydemoapp.android:id/cartBt"
        self.quantity_value = "com.saucelabs.mydemoapp.android:id/noTV"
        self.cart_badge = "com.saucelabs.mydemoapp.android:id/cartTV"

    def get_item_title(self):
        return self.get_element_text(AppiumBy.ID, self.product_title_id)

    def backpack_title_is_shown_and_expected(self):
        return self.get_item_title() == self.backpack_title
    
    def decrease_quantity(self):
        self.click_element(AppiumBy.ID, self.decrease_quantity_id)

    def increase_quantity(self):
        self.click_element(AppiumBy.ID, self.increase_quantity_id)

    def get_quantity(self):
        return int(self.get_element_text(AppiumBy.ID, self.quantity_value))
    
    def decrease_to_zero(self):
        while self.get_quantity() != 0:
            self.decrease_quantity()
    
    def is_cart_btn_enabled(self):
        return self.is_enabled(AppiumBy.ID, self.cart_btn_id)

    def cart_badge_qtd(self):
        return self.get_element_text(AppiumBy.ID, self.cart_badge)

    def add_to_cart_btn (self):
        self.click_element(AppiumBy.ID, self.cart_btn_id)

