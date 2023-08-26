from pageObject.LoginPage import LoginPage
from pageObject.SearchPage import SearchPage
class Test_CT005SearchProduct:

    def test_atualizar_qtd_produto(self, setup):
        home_page = setup
        home_page.click_login_btn()
        login = LoginPage(driver=home_page.driver)
        search_page = SearchPage(driver=home_page.driver)

        # Verificando se foi para a página de login
        assert login.is_url_login(), "A página mudou"

        # Inserir Usuário e Senha
        login.input_login()
        login.click_log_in_btn()

        # Verificando se o login foi feito
        assert login.verify_login()

        # Procurar produto
        home_page.search_product(product_name='Computing and Internet')

        # Validar a página de Search
        search_page.has_search_title()

        # Validar resultado da busca
        search_page.validate_search_result(expected_result='Computing and Internet')
