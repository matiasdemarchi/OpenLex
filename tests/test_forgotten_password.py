# Este es un testing de una solicitud por contraseña olvidada.
# Genera un error al cargar una dirección de e-mail registrada, pero con un servidor ficticio. Ya fue reportado como issue.

def test_passwordchange(page):
    # Go to main page
    page.goto("http://127.0.0.1:8020/OpenLex/")

    # Click text=Log In
    page.click("text=Log In")

    # Click text=¿Olvidó la contraseña?
    page.click("text=¿Olvidó la contraseña?")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index"

    # Click text=Solicitar reinicio de contraseña
    page.click("text=Solicitar reinicio de contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index#"

    # Triple click input[name="email"]
    page.click("input[name=\"email\"]", click_count=3)

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")

    # Click text=Solicitar reinicio de contraseña
    page.click("text=Solicitar reinicio de contraseña")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/request_reset_password?_next=/OpenLex/default/index#"

    # Close page
    page1.close()

    # Close page
    page.close()
