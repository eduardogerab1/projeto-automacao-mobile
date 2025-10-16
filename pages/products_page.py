from appium.webdriver.common.appiumby import AppiumBy
from pages.methods_page import BaseMethods

class HomePage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "productTV"
        self.orange_backpack_xpath = '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[3]'
        self.expected_products_title = "Products"
        self.go_to_cart_btn_page = "com.saucelabs.mydemoapp.android:id/cartIV"

    def get_home_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.product_title_id)

    def product_title_is_shown_and_expected(self):
        return self.get_home_page_title() == self.expected_products_title

    def select_orange_backpack(self):
        self.click_element(AppiumBy.XPATH, self.orange_backpack_xpath)

    def go_to_cart_btn(self):
        self.click_element(AppiumBy.ID, self.go_to_cart_btn_page)
