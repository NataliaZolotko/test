from pages.base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import main_site, Auth
import allure


class MainPage(BasePage):
    @allure.step('Открываем страницу "Главная"')
    def open_main_page(self):
        self.open(main_site)
    
    @allure.step("Авторизация")
    def authorization(self):
        login_input = self.find_element(MainPageLocators.LOGIN)
        login_input.clear()
        login_input.send_keys(Auth.login)
        
        password_input = self.find_element(MainPageLocators.PASSWORD)
        password_input.clear()
        password_input.send_keys(Auth.password)
        
        self.click(MainPageLocators.ENTER_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BASKET))
        return True  
           
                
    @allure.step("Добавить товар в корзину")
    def add_item_to_cart(self):
        self.click(MainPageLocators.ADD_TO_CART)
    
    @allure.step("Получить счетчик корзины")
    def get_cart_counter(self):
        try:
            counter_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.BACKET_COUNTER))
            return int(counter_element.text)
        except:
            return 0
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.click(MainPageLocators.BASKET)
    
    @allure.step("Проверить наличие товара в корзине")
    def is_item_in_cart(self):
        try:
            cart_items = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(MainPageLocators.CART_ITEM))
            return len(cart_items) > 0
        except:
            return False