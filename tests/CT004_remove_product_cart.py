from pageObject.LoginPage import LoginPage
from pageObject.YourCartPage import YourCartPage
class Test_CT004RemoveProductCart:

    def test_remove_product(self, setup):
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

        # Remover produto do carrinho
        home_page.verify_shopping_cart_qty()
        cart.remove_prod()