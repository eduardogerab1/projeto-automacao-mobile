from pages.products_page import HomePage
from pages.backpack_page import OrangeBackpack
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.shipping_page import ShippingPage

def test_case(driver):
    home_page = HomePage(driver)
    orange_backpack = OrangeBackpack(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    shipping_page = ShippingPage(driver)

    expected_qtd = 2
    expected_price = 29.99
    expected_total_price = expected_price * expected_qtd

    #valida que está na página de produtos (quando abre o app)
    assert home_page.product_title_is_shown_and_expected()

    print("\n abri a pagina de produtos")
    # depois que abrir o app, clica na bolsa laranja
    home_page.select_orange_backpack()

    # #valida que realmente abriu a bolsa laranja
    assert orange_backpack.backpack_title_is_shown_and_expected()
    print("nome do produto validado! o nome é: ", orange_backpack.get_item_title())

    # diminui em 1 e checa a quantidade
    quant_inicial = orange_backpack.get_quantity()
    orange_backpack.decrease_quantity()
    quant_atual = orange_backpack.get_quantity()
    assert int(quant_atual) == int(quant_inicial) - 1
    print("Diminuiu quantidade em 1")

    # diminui para 0 usando while e checa se o botão está inativo
    orange_backpack.decrease_to_zero()
    quant_atual = orange_backpack.get_quantity()
    assert quant_atual == 0 and orange_backpack.is_cart_btn_enabled() is False
    print("quantidade é zero E o botão está ativo")

    # aumenta a quantidade em 1
    orange_backpack.increase_quantity()
    assert int (orange_backpack.get_quantity()) == int(quant_atual) + 1 and orange_backpack.is_cart_btn_enabled() is True
    print("quantidade aumentou em 1 E o botão está ativo")

    # aumenta em 1 de novo, checa se está em 2 e adiciona produtos ao carrinho
    orange_backpack.increase_quantity()
    assert int(orange_backpack.get_quantity()) == int(quant_atual) + 2
    orange_backpack.add_to_cart_btn()
    print("adicionou 2 unidades ao carrinho")

    # certifica que o texto no carrinho mostra a quantidade de produtos desejada
    badge = orange_backpack.cart_badge_qtd()
    assert int(badge) == 2
    print(f"o círculo no carrinho mostra {badge} produtos")

    # clica no botão do carrinho e trocar de página
    home_page.go_to_cart_btn()
    print("abri a tela do carrinho")

    # certifica que está na página correta
    assert cart_page.cart_page_title_is_shown_and_expected()
    print("título da página validado!")

    # certifica que o nome do produto é o selecionado
    assert cart_page.product_name_is_shown_and_expected()
    print("nome do produto validado! o nome é: ", cart_page.get_product_name())

    product_price = cart_page.get_float_product_price()
    assert product_price == expected_price
    print("preço do produto validado! o preço é: ", product_price)

    qtd_under_pic = cart_page.get_qtd_under_pic()
    assert int(qtd_under_pic) == 2
    print("quantidade no campo é: ", qtd_under_pic)

    total_items_txt = cart_page.get_qtd_page_footer()
    expected_text = f"{expected_qtd} Items"
    assert expected_text in total_items_txt, f"Esperado '{expected_text}' em '{total_items_txt}'"
    print(f"total de itens validado foi: {expected_qtd}")

    total_price = cart_page.get_float_total_price()
    assert total_price == expected_total_price
    print("preço validado! o preço total foi: ", total_price)
    
    cart_page.shipping_click()
    print("cliquei no botão de prosseguir para login!")

    assert login_page.login_title_is_shown_and_expected()
    print("título da página validado! estou na página de: ", login_page.get_login_page_title())

    login_page.click_login_btn()
    print("cliquei no botão sem inserir nenhum dado")
    
    assert login_page.username_error_is_shown_and_expected()
    print("erro de usuário validado!")

    login_page.fill_username("teste")

    login_page.click_login_btn()
    print("cliquei no botão com usuário mas sem inserir senha")

    assert login_page.password_error_is_shown_and_expected()
    print("erro de senha validado!")

    login_page.log_with_username_from_list()
    print("logando com o primeiro usuário da lista...")
    login_page.log_with_password_from_list()
    print("inserindo a senha do primeiro usuário da lista...")

    login_page.click_login_btn()
    print("cliquei no botão de login com os dados corretos!")

    shipping_page.click_payment_btn()
    print("cliquei no botão de pagamento sem inserir os dados")

    assert shipping_page.full_name_error_is_shown_and_expected()
    print("erro de nome validado!")

    assert shipping_page.address_error_is_shown_and_expected()
    print("erro de endereço validado!")

    assert shipping_page.city_error_is_shown_and_expected()
    print("erro de cidade validado!")

    assert shipping_page.zip_error_is_shown_and_expected()
    print("erro de cep validado!")

    assert shipping_page.country_error_is_shown_and_expected()
    print("erro de país validado!")

    print("começando preenchimento dos campos...")
    shipping_page.fill_full_name("teste da silva")
    shipping_page.fill_address1("rua dos testes")
    shipping_page.fill_address2("123")
    shipping_page.fill_city("cidade dos testes")
    shipping_page.fill_state("estado dos testes")
    shipping_page.fill_zip_code("999")
    shipping_page.fill_country("país dos testes")
    print("preenchimento dos campos efetuado!")

    shipping_page.click_payment_btn()
    print("botão de pagamento clicado com os dados certos!")

    



    





    


