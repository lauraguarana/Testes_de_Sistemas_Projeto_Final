from pageObject.LoginPage import LoginPage
from pageObject.YourCartPage import YourCartPage
class Test_CT003UpdateQtyProduct:

    def test_atualizar_qtd_produto(self, setup):
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

        # Verificando se foi para a página do carrinho
        assert cart.check_cart_page(), "A página mudou"

        # Quantidade de produtos atual
        print(cart.get_quantity())
        actual_qty = cart.get_quantity()

        # Atualizar quantidade de produtos
        cart.update_prod_qty()

        # Quantidade de produtos final
        print(cart.get_quantity())
        final_qty = cart.get_quantity()

        # Validar se a quantidade de produto foi atualizada
        assert cart.compare_qty(actual_qty, final_qty)