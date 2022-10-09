from pages.home_page import HomePage

def test_saucedemo (driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_products() == "PRODUCTS"
    home_page.shopping()
    assert home_page.get_cart() == "YOUR CART"
    assert home_page.get_first_item() == "Sauce Labs Backpack"
    assert home_page.get_second_item() == "Sauce Labs Bolt T-Shirt"
    home_page.checkout()
    assert home_page.get_checkout() == "CHECKOUT: YOUR INFORMATION"
    home_page.enter_information("Velida", "Cakmak", "71000")
    assert home_page.get_checkout_overview() == "CHECKOUT: OVERVIEW"
    assert home_page.get_first_overview_item() == "Sauce Labs Backpack" 
    assert home_page.get_second_overview_item() == "Sauce Labs Bolt T-Shirt"
    home_page.finish()
    assert home_page.get_checkout_complete() == "CHECKOUT: COMPLETE!"
    home_page.menu_logout()
    assert home_page.get_login() == "Password for all users:"
