from pageObject.LoginPage import LoginPage
from pageObject.SearchPage import SearchPage
from pageObject.ProductPage import ProductPage
from pageObject.WishlistPage import WishlistPage


class Test_CT006AddAndVerifyProductsInWishlist:

    def test_atualizar_qtd_produto(self, setup):
        home_page = setup
        home_page.click_login_btn()
        login = LoginPage(driver=home_page.driver)
        search_page = SearchPage(driver=home_page.driver)
        product_page = ProductPage(driver=home_page.driver)
        wishlist_page = WishlistPage(driver=home_page.driver)

        # Verificando se foi para a página de login
        assert login.is_url_login(), "A página mudou"

        # Inserir Usuário e Senha
        login.input_login()
        login.click_log_in_btn()

        # Verificando se o login foi feito
        assert login.verify_login()

        # Procurar produto
        home_page.search_product(product_name='Music')

        # Abrir produto
        search_page.open_product(product_name='Music')

        # Adicionar produto na wishlist
        product_name = product_page.get_product_name()
        product_page.click_add_wishlist_btn()

        # Validar mensagem de produto adicionado na wishlist
        product_page.validate_wishlist_message()

        # Abrir a wishlist
        home_page.click_wishlist_btn()

        # Validar produto na wishlist
        assert wishlist_page.search_element_in_table(product_name=product_name)


