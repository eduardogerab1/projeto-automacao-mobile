from pages.methods_page import BaseMethods
from appium.webdriver.common.appiumby import AppiumBy

class CartPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_page_title = "com.saucelabs.mydemoapp.android:id/productTV"
        self.cart_page_title_text = "My Cart"
        self.product_name = "com.saucelabs.mydemoapp.android:id/titleTV"
        self.product_name_text = "Sauce Labs Backpack (orange)"
        self.product_price = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.qtd_under_pic = "com.saucelabs.mydemoapp.android:id/noTV"
        self.qtd_page_footer = "com.saucelabs.mydemoapp.android:id/itemsTV"
        self.total_price = "com.saucelabs.mydemoapp.android:id/totalPriceTV"
        self.shipping_btn = "com.saucelabs.mydemoapp.android:id/cartBt"

    def get_cart_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.cart_page_title)
    
    def cart_page_title_is_shown_and_expected(self):
        return self.get_cart_page_title() == self.cart_page_title_text
    
    def get_product_name(self):
        return self.get_element_text(AppiumBy.ID, self.product_name)
    
    def product_name_is_shown_and_expected(self):
        return self.get_product_name() == self.product_name_text
    
    def get_string_product_price(self):
        return self.get_element_text(AppiumBy.ID, self.product_price)
    
    def get_float_product_price(self):
        return float(self.get_string_product_price().replace("$", "").strip())

    def get_qtd_under_pic(self):
        return self.get_element_text(AppiumBy.ID, self.qtd_under_pic)
    
    def get_qtd_page_footer(self):
        return self.get_element_text(AppiumBy.ID, self.qtd_page_footer)
    
    def get_string_total_price(self):
        return self.get_element_text(AppiumBy.ID, self.total_price)

    def get_float_total_price(self):
        return float(self.get_string_total_price().replace("$", "").strip())

    def shipping_click(self):
        self.click_element(AppiumBy.ID, self.shipping_btn)
