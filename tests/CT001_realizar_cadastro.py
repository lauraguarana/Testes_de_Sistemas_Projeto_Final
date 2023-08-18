from faker import Faker

from pageObject.RegisterPage import RegisterPage


class Test_CT001RealizarCadastro:

    def test_realizar_cadastro(self, setup):
        home_page = setup
        home_page.click_register_btn()
        register = RegisterPage(driver=home_page.driver)

        # Verificando se após o click a página continua a mesma
        assert register.is_url_register(), "A página mudou"

        fake = Faker()

        # Cadastrar usuário
        register.register_new_user(first_name=fake.name(), last_name=fake.last_name(), email=fake.email(), password="1234567", confirm_password="1234567"), "Usuário não cadastrado"

        # Validar usuário cadastrado com sucesso
        assert register.validate_register_message(), "A mensagem de confirmação de registro não foi exibida"