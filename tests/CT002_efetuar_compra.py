from pageObject.LoginPage import LoginPage
class Test_CT002EfetuarCompra:

    def test_efetuar_compra(self, setup):
        home_page = setup
        home_page.click_login_btn()
        login = LoginPage(driver=home_page.driver)

        # Verificando se foi para a página de login
        assert login.is_url_login(), "A página mudou"

        # Inserir Usuário e Senha
        login.input_login()
        login.click_log_in_btn()

        # Verificando se o login foi feito
        assert login.verify_login()

        #Adicionar produto
        home_page.add_product_to_cart()
        assert home_page.verify_bar_notification()

        #Ir para o carrinho de compras
        assert home_page.click_shopping_cart_btn()
        home_page.click_shopping_cart_btn()

        # Verificando se foi para a página do carrinho
        assert cart.check_cart_page(), "A página mudou"


        #Ir para o checkout

