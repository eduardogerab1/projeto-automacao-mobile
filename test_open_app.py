import time
from appium import webdriver
from appium.options.common.base import AppiumOptions

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.saucelabs.mydemoapp.android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
	"appWaitDuration": 30000  # opcional, tempo de espera em ms (30s)
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

bolsa_preta = driver.find_element("xpath", '(//android.widget.ImageView[@content-desc="Product Image"])[1]')
bolsa_preta.click()
time.sleep(4)

cor_verde = driver.find_element("-android uiautomator", 'new UiSelector().description("Green color")')
cor_verde.click()
time.sleep(4)

acrescentar_produto = driver.find_element("xpath", '//android.widget.ImageView[@content-desc="Increase item quantity"]')
acrescentar_produto.click()
time.sleep(4)

adicionar_carrinho = driver.find_element("accessibility id", 'Tap to add product to cart')
adicionar_carrinho.click()
time.sleep(4)

abrir_carrinho = driver.find_element("accessibility id", 'Displays number of items in your cart')
abrir_carrinho.click()
time.sleep(4)

dimiuir_produto_no_carrinho = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/minusIV')
dimiuir_produto_no_carrinho.click()
time.sleep(4)

goto_checkout = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
goto_checkout.click()
time.sleep(4)

username_sign = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/nameET')
username_sign.send_keys("user_teste")
time.sleep(4)
driver.hide_keyboard()

password_sign = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/passwordET')
password_sign.send_keys("senha_teste")
time.sleep(4)
driver.hide_keyboard()

login_button = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/loginBtn')
login_button.click()
time.sleep(4)

full_name = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/fullNameET")')
full_name.send_keys("usuario de teste")
time.sleep(4)
driver.hide_keyboard()

address_line1 = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/address1ET")')
address_line1.send_keys("Rua dos testes, 123")
time.sleep(4)
driver.hide_keyboard()

address_line2 = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address2ET')
address_line2.send_keys("Casa")
time.sleep(4)
driver.hide_keyboard()

city = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/cityET")')
city.send_keys("Testelândia")
time.sleep(4)
driver.hide_keyboard()

state = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/stateET')
state.send_keys("Estado de Teste")
time.sleep(4)
driver.hide_keyboard()

zip_code = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipET')
zip_code.send_keys("12345-678")
time.sleep(4)
driver.hide_keyboard()

country = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/countryET')
country.send_keys("País de Teste")
time.sleep(4)
driver.hide_keyboard()

payment_button = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
payment_button.click()
time.sleep(4)

full_name_credit_card = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/nameET")')
full_name_credit_card.send_keys("cartão de crédito do usuário de teste")
time.sleep(4)
driver.hide_keyboard()

card_number = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cardNumberET')
card_number.send_keys("1234 5678 9012 3456")
time.sleep(4)
driver.hide_keyboard()

card_expiration_date = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/expirationDateET')
card_expiration_date.send_keys("11/26")
time.sleep(4)
driver.hide_keyboard()

cvv_number = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/securityCodeET')
cvv_number.send_keys("123")
time.sleep(4)
driver.hide_keyboard()

review_order_btn = driver.find_element("accessibility id", 'Saves payment info and launches screen to review checkout data')
review_order_btn.click()
time.sleep(4)

place_order_btn = driver.find_element("accessibility id", 'Completes the process of checkout')
place_order_btn.click()
time.sleep(4)

checkout_complete = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/completeTV')
assert checkout_complete.text == "Checkout Complete"
print("Teste concluído com sucesso!")
driver.quit()
