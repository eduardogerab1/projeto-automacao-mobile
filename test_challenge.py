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

print("abri o aplicativo")
time.sleep(4)
orange_bag = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)')
orange_bag.click()
print("cliquei na bolsa laranja")
time.sleep(4)

validate_product_name = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert validate_product_name.get_attribute("text") == "Sauce Labs Backpack (orange)"
print("O nome do produto é: ", validate_product_name.text)
time.sleep(4)

current_quantity = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV')
decrease_product = driver.find_element("accessibility id",'Decrease item quantity')
decrease_product.click()
updated_quantity = int(current_quantity.get_attribute("text"))
assert updated_quantity == int(current_quantity.get_attribute("text"))
print("a quantidade selecionada foi: ", updated_quantity)
time.sleep(4)

checking_button = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
button_state = checking_button.get_attribute("enabled")
assert button_state == "false"
print("o estado de enabled no botão do carrinho é: ", checking_button.get_attribute("enabled"))
time.sleep(4)

increase_product = driver.find_element("accessibility id",'Increase item quantity')
increase_product.click()
updated_quantity = int(current_quantity.get_attribute("text"))
assert updated_quantity == int(current_quantity.get_attribute("text"))
print("a quantidade selecionada foi: ", updated_quantity)
time.sleep(4)

checking_button_after_increase = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
button_state_after_increase = checking_button_after_increase.get_attribute("enabled")
assert button_state_after_increase == "true"
print("o estado de enabled no botão do carrinho é: ", checking_button_after_increase.get_attribute("enabled"))
time.sleep(4)

increase_product.click()
unit_price = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/priceTV').get_attribute("text")
updated_quantity = int(current_quantity.get_attribute("text"))
assert updated_quantity == int(current_quantity.get_attribute("text"))
print("a quantidade selecionada foi: ", updated_quantity)
time.sleep(4)
checking_button_after_increase.click()
print("cliquei no botão de adicionar ao carrinho")
time.sleep(4)

get_on_cart = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartTV')
number_on_cart = get_on_cart.get_attribute("text")
assert int(number_on_cart) == updated_quantity
print("o texto no círculo do carrinho é: ", number_on_cart)
time.sleep(4)

goto_cart_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartIV')
goto_cart_page.click()
print("cliquei no botão da página do carrinho")
time.sleep(4)

validate_cart_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert validate_cart_page.get_attribute("text") == "My Cart"
print("Estou na página: ", validate_cart_page.get_attribute("text"))
time.sleep(4)

validate_product_name = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/titleTV')
assert validate_product_name.get_attribute("text") == "Sauce Labs Backpack (orange)"
print("O nome do produto no carrinho é: ", validate_product_name.get_attribute("text"))
time.sleep(4)

validate_product_price = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/priceTV')
assert validate_product_price.get_attribute("text") == unit_price
print("O preço do produto no carrinho é: ", validate_product_price.get_attribute("text"))
time.sleep(4)

validate_product_quantity = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV')
assert int(validate_product_quantity.get_attribute("text")) == updated_quantity
print("A quantidade do produto no carrinho (embaixo da foto) é: ", validate_product_quantity.get_attribute("text"))
time.sleep(4)

validate_products_total = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/itemsTV')
expected_total_text = f"{updated_quantity} Items"
assert validate_products_total.get_attribute("text") == expected_total_text
print("O total de itens no carrinho (lá embaixo) é: ", validate_products_total.text)
time.sleep(4)

validate_price_total = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/totalPriceTV')
calculated_total = float(unit_price.replace("$", "").strip()) * updated_quantity
current_total_validation = validate_price_total.get_attribute("text")
current_total = float(current_total_validation.replace("$", "").strip())
assert current_total == calculated_total
print("O preço total no carrinho é: ", validate_price_total.text)
time.sleep(4)

proceed_to_checkout_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
proceed_to_checkout_btn.click()
print("cliquei no botão de proceed")
time.sleep(4)

validate_login_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/loginTV')
assert validate_login_page.get_attribute("text") == "Login"
print("estou na página: ", validate_login_page.get_attribute("text"))
time.sleep(4)
login_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/loginBtn')
login_btn.click()
print("cliquei no botão de login sem inserir usuário e senha")
time.sleep(4)
login_error_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/nameErrorTV')
assert login_error_validation.get_attribute("text") == "Username is required"
print("validando login sem usuário e senha:", login_error_validation.get_attribute("text"))
time.sleep(4)

username_field = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/nameET')
username_field.clear()
username_field.send_keys("teste")
print("o usuário usado foi: ", username_field.get_attribute("text"))
login_btn.click()
print("cliquei no botão de login sem inserir senha")
time.sleep(2)
password_error_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/passwordErrorTV')
assert password_error_validation.get_attribute("text") == "Enter Password"
print("validando login sem senha: ", password_error_validation.get_attribute("text"))
time.sleep(4)

usernames_list = driver.find_elements("xpath", '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/username1TV"]')
first_username = usernames_list[0].get_attribute("text")
username_field.clear()
username_field.send_keys(first_username)
print("o username usado foi:", first_username)
time.sleep(4)

password_field = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/passwordET')
password_list = driver.find_elements("id",'com.saucelabs.mydemoapp.android:id/password1TV')
first_password = password_list[0].get_attribute("text")
password_field.clear()
password_field.send_keys(first_password)
print("a senha usada foi: ", first_password)
time.sleep(4)
login_btn.click()
print("cliquei no botão de login com os dados corretos")
time.sleep(2)

validate_shipment_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterShippingAddressTV')
assert validate_shipment_page.get_attribute("text") == "Enter a shipping address"
print("Estou na página: ", validate_shipment_page.get_attribute("text"))
time.sleep(4)
full_name_value = "Teste da Silva"
address_line1_value = "Rua de Teste"
address_line2_value = "123"
city_value = "Cidade de Teste"
state_value = "Estado de Teste"
zip_code_value = "456"
country_value = "Teste"
full_name_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/fullNameET')
full_name_field.send_keys("Teste da Silva")
time.sleep(2)
address_line1_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address1ET')
address_line1_field.send_keys("Rua de Teste")
time.sleep(2)
address_line2_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address2ET')
address_line2_field.send_keys("123")
time.sleep(2)
city_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cityET')
city_field.send_keys("Cidade de Teste")
time.sleep(2)
zip_code_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipET')
zip_code_field.send_keys("456")
time.sleep(2)
state_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/stateET')
state_field.send_keys("Estado de Teste")
time.sleep(2)
country_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/countryET')
country_field.send_keys("Teste")
time.sleep(2)
payment_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
payment_btn.click()
print("cliquei no botão de pagamento")
time.sleep(2)

validate_payment_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV')
assert validate_payment_page.get_attribute("text") == "Enter a payment method"
print("Estou na página", validate_payment_page.get_attribute("text"))
time.sleep(4)
card_name_value = "Teste da Silva"
card_number_value = "123456789"
expiration_date_value = "12/28"
security_code_value = "999"
full_credit_card_name = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/nameET')
full_credit_card_name.send_keys("Teste da Silva")
credit_card_number = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cardNumberET')
credit_card_number.send_keys("123456789")
expiration_date = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/expirationDateET')
expiration_date.send_keys("12/28")
security_code = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/securityCodeET')
security_code.send_keys("999")
check_box = driver.find_element("id", "com.saucelabs.mydemoapp.android:id/billingAddressCB")
if check_box.get_attribute("checked") == "false":
    check_box.click()
    assert check_box.get_attribute("checked") == "true"
    print("o if foi executado")
else:
	assert check_box.get_attribute("checked") == "true"

print("a checkbox está selecionada: ", check_box.get_attribute("checked"))
time.sleep(4)

review_order_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
review_order_btn.click()
print("cliquei no botão de review order")
time.sleep(4)

validate_review_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterShippingAddressTV')
assert validate_review_page.get_attribute("text") == "Review your order"
print("Estou na página: ", validate_review_page.get_attribute("text"))
time.sleep(6)

size = driver.get_window_size()
screen_width = size['width']
screen_height = size['height']

driver.execute_script("mobile: scrollGesture", {
    "left": 0,
    "top": screen_height * 0.3,
    "width": screen_width,
    "height": screen_height * 0.5,
    "direction": "down",
    "percent": 1.0
})
time.sleep(6)
expected_deliver_address = [
    full_name_value,
    address_line1_value,
    f"{city_value}, {state_value}",
    f"{country_value}, {zip_code_value}"
]

expected_payment_method = [
    card_name_value,
    card_number_value,
    f"Exp: {expiration_date_value}",
    "Billing address is the same as shipping address"
]


deliver_elements = driver.find_elements(
    "xpath",
    "//android.widget.TextView[@text='Deliver Address']/following-sibling::android.widget.TextView"
)
deliver_texts = [el.get_attribute("text") for el in deliver_elements]
print("Deliver Address capturado:", deliver_texts)

assert deliver_texts == expected_deliver_address, \
    f"Deliver Address não bateu! Esperado: {expected_deliver_address} | Encontrado: {deliver_texts}"

# Captura os textos da seção Payment Method
payment_elements = driver.find_elements(
    "xpath",
    "//android.widget.TextView[@text='Payment Method']/following-sibling::android.widget.TextView"
)
payment_texts = [el.get_attribute("text") for el in payment_elements]
print("Payment Method capturado:", payment_texts)

assert payment_texts == expected_payment_method, \
    f"Payment Method não bateu! Esperado: {expected_payment_method} | Encontrado: {payment_texts}"

time.sleep(6)
driver.execute_script("mobile: scrollGesture", {
    "left": 0,
    "top": screen_height * 0.3,
    "width": screen_width,
    "height": screen_height * 0.5,
    "direction": "up",
    "percent": 1.0
})
time.sleep(6)

product_name_on_cart = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/titleTV')
assert product_name_on_cart.get_attribute("text") == "Sauce Labs Backpack (orange)"
print("o nome do produto realmente é: ", product_name_on_cart.get_attribute("text"))

product_price_on_cart = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/priceTV')
assert product_price_on_cart.get_attribute("text") == unit_price
print("o preço do produto realmente é: ", product_price_on_cart.get_attribute("text"))

time.sleep(6)
driver.execute_script("mobile: scrollGesture", {
    "left": 0,
    "top": screen_height * 0.3,
    "width": screen_width,
    "height": screen_height * 0.5,
    "direction": "down",
    "percent": 1.0
})
time.sleep(6)

dhl_standard_delivery = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/amountTV')
dhl_standard_delivery_value = dhl_standard_delivery.get_attribute("text")
assert dhl_standard_delivery_value == "$5.99"
print("O frete é realmente: ", dhl_standard_delivery_value)
time.sleep(4)

dhl_standard_delivery_format = float(dhl_standard_delivery_value.replace("$", "").strip())
purchase_price = calculated_total + dhl_standard_delivery_format
expected_purchase_price = f"${purchase_price:.2f}"
purchase_price_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/totalAmountTV')
purchase_price_validation_value = purchase_price_validation.get_attribute("text")
found_purchase_price = float(purchase_price_validation_value.replace("$", "").strip())
assert found_purchase_price == purchase_price, \
    f"Valor esperado: {purchase_price} | Encontrado: {found_purchase_price}"

print("O valor total da compra realmente foi: ", purchase_price_validation_value)
time.sleep(4)

place_order_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
place_order_btn.click()
print("cliquei no botão de place order")
time.sleep(4)

checkout_complete_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/completeTV')
assert checkout_complete_page.get_attribute("text") == "Checkout Complete"
print("estou na tela de: ", checkout_complete_page.get_attribute("text"))
time.sleep(4)

continue_shopping_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/shoopingBt')
continue_shopping_btn.click()
print("cliquei no botão de continue")
time.sleep(4)

product_page_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert product_page_validation.get_attribute("text") == "Products"
print("Estou na tela de: ", product_page_validation.get_attribute("text"))
time.sleep(4)

open_cart_btn = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/cartIV')
open_cart_btn.click()
time.sleep(4)
cart_page_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noItemTitleTV')
assert cart_page_validation.get_attribute("text") == "No Items"
print("o carrinho tem: ", cart_page_validation.get_attribute("text"))
print("testes concluídos!")