from pageObject.LoginPage import LoginPage
from pageObject.YourCartPage import YourCartPage
class Test_CT003UpdateQtyProduct:

    def test_update_product(self, setup):
        home_page = setup
        home_page.click_login_btn()
        login = LoginPage(driver=home_page.driver)
        cart = YourCartPage(driver=home_page.driver)

        # Verificando se foi para a página de login
        assert login.is_url_login(), "A página mudou"

        # Inserir Usuário e Senha
        login.input_login()
        login.click_log_in_btn()

        # Verificando se o login foi feito
        assert login.verify_login()

        # Validar quantidade de produto no carrinho
        home_page.verify_shopping_cart_qty()

        # Ir para o carrinho de compras
        home_page.click_shopping_cart_btn()

        # Validar quantidade de produto no carrinho
        home_page.verify_shopping_cart_qty()

        # Verificando se foi para a página do carrinho
        assert cart.check_cart_page(), "A página mudou"

        # Salvar quantidade de produtos e atualizar a quantidade
        actual_qty = cart.get_quantity()
        cart.update_prod_qty()

        # Validar se a quantidade foi atualizada
        expected_qty = cart.get_quantity()
        cart.compare_qty(actual=actual_qty, expected=expected_qty)
