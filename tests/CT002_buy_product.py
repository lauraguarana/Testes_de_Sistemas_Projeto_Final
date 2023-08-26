from pageObject.LoginPage import LoginPage
from pageObject.YourCartPage import YourCartPage
from pageObject.CheckoutCartPage import CheckoutCartPage
from pageObject.CheckoutCompleteCartPage import CheckoutCompleteCartPage


class Test_CT002BuyProduct:

    def test_buy_product(self, setup):
        home_page = setup
        home_page.click_login_btn()
        login = LoginPage(driver=home_page.driver)
        cart = YourCartPage(driver=home_page.driver)
        checkoutCartPage = CheckoutCartPage(driver=home_page.driver)
        checkoutCompleteCartPage = CheckoutCompleteCartPage(driver=home_page.driver)

        # Verificando se foi para a página de login
        assert login.is_url_login(), "A página mudou"

        # Inserir Usuário e Senha
        login.input_login()
        login.click_log_in_btn()

        # Verificando se o login foi feito
        assert login.verify_login()

        # Adicionar produto
        home_page.add_product_to_cart()
        assert home_page.verify_bar_notification()

        # Ir para o carrinho de compras
        home_page.click_shopping_cart_btn()

        # Verificando se foi para a página do carrinho
        assert cart.check_cart_page(), "A página mudou"

        # Ir para o checkout
        cart.click_checkout()

        # Validar informações da página de Checkout
        checkoutCartPage.billing_address()
        checkoutCartPage.shipping_address()
        checkoutCartPage.shipping_method()
        checkoutCartPage.payment_method()
        checkoutCartPage.payment_information()
        checkoutCartPage.confirm_order()

        # Confirmar compra efetuada com sucesso
        checkoutCompleteCartPage.check_checkout_complete_page()
        assert checkoutCompleteCartPage.check_thank_message()
