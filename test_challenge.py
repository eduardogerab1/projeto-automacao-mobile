import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

full_name_value = "Teste da Silva"
address_line1_value = "Rua de Teste"
address_line2_value = "123"
city_value = "Cidade de Teste"
state_value = "Estado de Teste"
zip_code_value = "456"
country_value = "Teste"

full_credit_card_name = "Teste da Silva"
credit_card_number = "123456789"
expiration_date = "12/28"
security_code = "999"

card_full_name = "Silva do Teste"
card_address1 = "Testes das Ruas"
card_address2 = "Prédio"
card_city = "Testes das Cidades"
card_state = "Testes dos Estados"
card_zip_code = "890"
card_country = "Testes do País"

print("abri o aplicativo")
time.sleep(1)
orange_bag = driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)')
orange_bag.click()
print("cliquei na bolsa laranja")
time.sleep(1)

validate_product_name = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert validate_product_name.get_attribute("text") == "Sauce Labs Backpack (orange)"
print("O nome do produto é: ", validate_product_name.text)

before_quantity = int(driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV').get_attribute("text"))
decrease_product = driver.find_element("accessibility id",'Decrease item quantity')
decrease_product.click()
after_quantity = int(driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV').get_attribute("text"))
assert before_quantity-1 == after_quantity, f"O valor esperado era {before_quantity-1}, valor atual: {after_quantity}"
print("a quantidade selecionada foi: ", after_quantity)

checking_button = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
button_state = checking_button.get_attribute("enabled")
assert button_state == "false"
print("o estado de enabled no botão do carrinho é: ", checking_button.get_attribute("enabled"))

increase_product = driver.find_element("accessibility id",'Increase item quantity')
increase_product.click()
after_quantity = int(driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV').get_attribute("text"))
assert before_quantity == after_quantity, f"O valor esperado era {before_quantity}, valor atual: {after_quantity}"
print("a quantidade selecionada foi: ", after_quantity)

checking_button_after_increase = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
button_state_after_increase = checking_button_after_increase.get_attribute("enabled")
assert button_state_after_increase == "true"
print("o estado de enabled no botão do carrinho é: ", checking_button_after_increase.get_attribute("enabled"))

increase_product.click()
unit_price = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/priceTV').get_attribute("text")
after_quantity = int(driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV').get_attribute("text"))
assert before_quantity+1 == after_quantity, f"O valor esperado era {before_quantity+1}, valor atual: {after_quantity}"
print("a quantidade selecionada foi: ", after_quantity)
checking_button_after_increase.click()
print("cliquei no botão de adicionar ao carrinho")
time.sleep(1)

get_on_cart = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartTV')
number_on_cart = get_on_cart.get_attribute("text")
assert int(number_on_cart) == after_quantity
print("o texto no círculo do carrinho é: ", number_on_cart)

goto_cart_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartIV')
goto_cart_page.click()
print("cliquei no botão da página do carrinho")
time.sleep(1)

validate_cart_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert validate_cart_page.get_attribute("text") == "My Cart"
print("Estou na página: ", validate_cart_page.get_attribute("text"))

validate_product_name = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/titleTV')
assert validate_product_name.get_attribute("text") == "Sauce Labs Backpack (orange)"
print("O nome do produto no carrinho é: ", validate_product_name.get_attribute("text"))

validate_product_price = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/priceTV')
assert validate_product_price.get_attribute("text") == unit_price
print("O preço do produto no carrinho é: ", validate_product_price.get_attribute("text"))

validate_product_quantity = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noTV')
assert int(validate_product_quantity.get_attribute("text")) == after_quantity
print("A quantidade do produto no carrinho (embaixo da foto) é: ", validate_product_quantity.get_attribute("text"))

validate_products_total = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/itemsTV')
expected_total_text = f"{after_quantity} Items"
assert validate_products_total.get_attribute("text") == expected_total_text
print("O total de itens no carrinho (lá embaixo) é: ", validate_products_total.text)

validate_price_total = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/totalPriceTV')
calculated_total = float(unit_price.replace("$", "").strip()) * after_quantity
current_total_validation = validate_price_total.get_attribute("text")
current_total = float(current_total_validation.replace("$", "").strip())
assert current_total == calculated_total
print("O preço total no carrinho é: ", validate_price_total.text)

proceed_to_checkout_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cartBt')
proceed_to_checkout_btn.click()
print("cliquei no botão de proceed")
time.sleep(1)

validate_login_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/loginTV')
assert validate_login_page.get_attribute("text") == "Login"
print("estou na página: ", validate_login_page.get_attribute("text"))

login_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/loginBtn')
login_btn.click()
print("cliquei no botão de login sem inserir usuário e senha")
time.sleep(1)
login_error_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/nameErrorTV')
assert login_error_validation.get_attribute("text") == "Username is required"
print("validando login sem usuário e senha:", login_error_validation.get_attribute("text"))
time.sleep(1)

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
time.sleep(1)

usernames_list = driver.find_elements("xpath", '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/username1TV"]')
first_username = usernames_list[0].get_attribute("text")
username_field.clear()
username_field.send_keys(first_username)
print("o username usado foi:", first_username)

password_field = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/passwordET')
password_list = driver.find_elements("id",'com.saucelabs.mydemoapp.android:id/password1TV')
first_password = password_list[0].get_attribute("text")
password_field.clear()
password_field.send_keys(first_password)
print("a senha usada foi: ", first_password)
login_btn.click()
print("cliquei no botão de login com os dados corretos")
time.sleep(1)

validate_shipment_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterShippingAddressTV')
assert validate_shipment_page.get_attribute("text") == "Enter a shipping address"
print("Estou na página: ", validate_shipment_page.get_attribute("text"))
time.sleep(1)

payment_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
payment_btn.click()
print("cliquei no botão de payment sem inserir os dados corretamente")
time.sleep(1)

print("validando erros nos campos de shipping: ")
full_name_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/fullNameErrorTV')
address_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address1ErrorTV')
city_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cityErrorTV')
zip_code_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipErrorTV')
country_error = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/countryErrorTV')
assert full_name_error.get_attribute("text") == "Please provide your full name."
print("erro no nome: ", full_name_error.get_attribute("text"))
assert address_error.get_attribute("text") == "Please provide your address."
print("erro no endereço: ", address_error.get_attribute("text"))
assert city_error.get_attribute("text") == "Please provide your city."
print("erro na cidade: ", city_error.get_attribute("text"))
assert zip_code_error.get_attribute("text") == "Please provide your zip"
print("erro no cep: ", zip_code_error.get_attribute("text"))
assert country_error.get_attribute("text") == "Please provide your"
print("erro no país: ", country_error.get_attribute("text"))
time.sleep(1)

full_name_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/fullNameET')
full_name_field.send_keys(full_name_value)
address_line1_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address1ET')
address_line1_field.send_keys(address_line1_value)
address_line2_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address2ET')
address_line2_field.send_keys(address_line2_value)
city_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cityET')
city_field.send_keys(city_value)
zip_code_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipET')
zip_code_field.send_keys(zip_code_value)
state_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/stateET')
state_field.send_keys(state_value)
country_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/countryET')
country_field.send_keys(country_value)
payment_btn.click()
print("cliquei no botão de pagamento inserindo os dados corretamente")
time.sleep(1)

review_order_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
review_order_btn.click()
print("cliquei no botão de review sem inserir os dados corretamente")
time.sleep(1)

check_box = driver.find_element("id", "com.saucelabs.mydemoapp.android:id/billingAddressCB")
check_box.click()

print("validando erros nos campos de payment: ")
full_name_payment_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/nameErrorTV')
assert full_name_payment_error.get_attribute("text") == "Value looks invalid."
print("erro ao preencher nome completo: ", full_name_payment_error.get_attribute("text"))
card_number_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cardNumberErrorIV')
assert card_number_error.is_displayed()
print("erro ao preencher o número do cartão de crédito.")
expiration_date_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/expirationDateErrorTV')
assert expiration_date_error.get_attribute("text") == "Value looks invalid."
print("erro ao preencher a data do cartão de crédito: ", expiration_date_error.get_attribute("text"))
security_code_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/securityCodeErrorTV')
assert security_code_error.get_attribute("text") == "Value looks invalid."
print("erro ao preencher o cvv: ", security_code_error.get_attribute("text"))
time.sleep(1)

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
time.sleep(1)
review_order_btn.click()

time.sleep(1)

billing_address_name_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/fullNameErrorTV')
assert billing_address_name_error.get_attribute("text") == "Please provide your full name."
print("erro ao preencher campo de full name la embaixo: ", billing_address_name_error.get_attribute("text"))
billing_address1_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address1ErrorTV')
assert billing_address1_error.get_attribute("text") == "Please provide your address."
print("erro ao preencher campo de endereço 1 la embaixo", billing_address1_error.get_attribute("text"))
billing_city_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cityErrorTV')
assert billing_city_error.get_attribute("text") == "Please provide your city."
print("erro ao preencher o campo de cidade la embaixo: ", billing_city_error.get_attribute("text"))
billing_zip_code_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipErrorTV')
assert billing_zip_code_error.get_attribute("text") == "Please provide your zip"
print("erro ao preencher o campo de zip la embaixo: ", billing_zip_code_error.get_attribute("text"))
billing_country_error = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/countryErrorTV')
assert billing_country_error.get_attribute("text") == "Please provide your"
print("erro ao preencher o campo de país la embaixo", billing_country_error.get_attribute("text"))

size = driver.get_window_size()
screen_width = size['width']
screen_height = size['height']
driver.execute_script("mobile: scrollGesture", {
    "left": 0,
    "top": screen_height * 0.3,
    "width": screen_width,
    "height": screen_height * 0.5,
    "direction": "up",
    "percent": 1.0
})

validate_payment_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV')
assert validate_payment_page.get_attribute("text") == "Enter a payment method"
print("Estou na página", validate_payment_page.get_attribute("text"))

full_credit_card_name_field = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/nameET')
full_credit_card_name_field.send_keys(full_credit_card_name)
credit_card_number_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cardNumberET')
credit_card_number_field.send_keys(credit_card_number)
expiration_date_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/expirationDateET')
expiration_date_field.send_keys(expiration_date)
security_code_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/securityCodeET')
security_code_field.send_keys(security_code)

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

card_full_name_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/fullNameET')
card_full_name_field.send_keys(card_full_name)
card_address1_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address1ET')
card_address1_field.send_keys(card_address1)
card_address2_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/address2ET')
card_address2_field.send_keys(card_address2)
card_city_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/cityET')
card_city_field.send_keys(card_city)
card_state_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/stateET')
card_state_field.send_keys(card_state)
card_zip_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/zipET')
card_zip_field.send_keys(card_zip_code)
card_country_field = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/countryET')
card_country_field.send_keys(card_country)

print("a checkbox está selecionada: ", check_box.get_attribute("checked"))

review_order_btn.click()
print("cliquei no botão de review order inserindo os dados corretamente")

validate_review_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/enterShippingAddressTV')
assert validate_review_page.get_attribute("text") == "Review your order"
print("Estou na página: ", validate_review_page.get_attribute("text"))
time.sleep(1)

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
time.sleep(1)

expected_deliver_address = [
    full_name_value,
    address_line1_value,
    address_line2_value,
    f"{city_value}, {state_value}",
    f"{country_value}, {zip_code_value}"
]

expected_payment_method = [
    full_credit_card_name,
    credit_card_number,
    f"Exp: {expiration_date}"
]

expected_billing_address = [
    card_full_name,
    card_address1,
    card_address2,
    f"{card_city}, {card_state}",
    f"{card_zip_code}, {card_country}"
]

deliver_elements = driver.find_elements(
    "xpath",
    "//android.widget.TextView[@text='Deliver Address']/following-sibling::android.widget.TextView"
)
billing_elements = driver.find_elements(
    "xpath",
    "//android.widget.TextView[@text='Billing Address']/following-sibling::android.widget.TextView"
)
deliver_texts = [el.get_attribute("text") for el in deliver_elements]
print("deliver address capturado: ", deliver_texts)
assert deliver_texts == expected_deliver_address, \
     f"Deliver Address não bateu! Esperado: {expected_deliver_address} | Encontrado: {deliver_texts}"

billing_texts = [el.get_attribute("text") for el in billing_elements]
print("Billing Address capturado:", billing_texts)
assert billing_texts == expected_billing_address, \
    f"Payment Method não bateu! Esperado: {expected_billing_address} | Encontrado: {billing_texts}"

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
time.sleep(1)

dhl_standard_delivery_format = float(dhl_standard_delivery_value.replace("$", "").strip())
purchase_price = calculated_total + dhl_standard_delivery_format
expected_purchase_price = f"${purchase_price:.2f}"
wait = WebDriverWait(driver, 10)
purchase_price_validation = wait.until(
    EC.presence_of_element_located(("id", "com.saucelabs.mydemoapp.android:id/totalAmountTV"))
)
purchase_price_validation_value = purchase_price_validation.get_attribute("text")
found_purchase_price = float(purchase_price_validation_value.replace("$", "").strip())
assert found_purchase_price == purchase_price, \
    f"Valor esperado: {purchase_price} | Encontrado: {found_purchase_price}"

print("O valor total da compra realmente foi: ", purchase_price_validation_value)
time.sleep(1)

place_order_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/paymentBtn')
place_order_btn.click()
print("cliquei no botão de place order")
time.sleep(1)

checkout_complete_page = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/completeTV')
assert checkout_complete_page.get_attribute("text") == "Checkout Complete"
print("estou na tela de: ", checkout_complete_page.get_attribute("text"))
time.sleep(1)

continue_shopping_btn = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/shoopingBt')
continue_shopping_btn.click()
print("cliquei no botão de continue")
time.sleep(1)

product_page_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/productTV')
assert product_page_validation.get_attribute("text") == "Products"
print("Estou na tela de: ", product_page_validation.get_attribute("text"))
time.sleep(1)

open_cart_btn = driver.find_element("id",'com.saucelabs.mydemoapp.android:id/cartIV')
open_cart_btn.click()
time.sleep(1)
cart_page_validation = driver.find_element("id", 'com.saucelabs.mydemoapp.android:id/noItemTitleTV')
assert cart_page_validation.get_attribute("text") == "No Items"
print("o carrinho tem: ", cart_page_validation.get_attribute("text"))
print("testes concluídos!")