from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
    
    def login(self, username, password):
        
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        time.sleep(5)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(5)
    
    def get_products(self):
        products_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return products_element.text
    
    def shopping(self):
        first_item = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
        first_item.click()
        second_item = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        second_item.click()
        time.sleep(5)
        icon = self.driver.find_element(By.ID, "shopping_cart_container")
        icon.click()
        time.sleep(5)

    def get_cart(self):
        cart_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return cart_element.text

    def get_first_item(self):
        first_cart_item = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_4_title_link']/div")))
        return first_cart_item.text 

    def get_second_item(self):
        second_cart_item = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_1_title_link']/div")))
        return second_cart_item.text

    def checkout(self):
        checkout = self.driver.find_element(By.ID, "checkout")
        checkout.click()
        time.sleep(5)

    def get_checkout(self):
        checkout_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return checkout_element.text

    def enter_information(self, first, last, zip):
        first_name= self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name.clear()
        first_name.click()
        first_name.send_keys(first)
        last_name = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_name.clear()
        last_name.click()
        last_name.send_keys(last)
        zip_code= self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        zip_code.clear()
        zip_code.click()
        zip_code.send_keys(zip)
        time.sleep(5)
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def get_checkout_overview(self):
        checkout_overview_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return checkout_overview_element.text

    def get_first_overview_item(self):
        first_overview_item = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_4_title_link']/div")))
        return first_overview_item.text 

    def get_second_overview_item(self):
        second_overview_item = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_1_title_link']/div")))
        return second_overview_item.text

    def finish(self):
        finish = self.driver.find_element(By.ID, "finish")
        finish.click()
        time.sleep(5)

    def get_checkout_complete(self):
        checkout_complete_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return checkout_complete_element.text

    def menu_logout(self):
        menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu.click()
        time.sleep(5)
        logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout.click()
        time.sleep(5)

    def get_login(self):
        login_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='login_password']/h4")))
        return login_element.text

    