
from selenium.webdriver.common.by import By


class MainPageLocators:
       
    LOGIN = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    ENTER_BUTTON = (By.XPATH, "//input[@id='login-button']")
    
    BASKET = (By.XPATH, "//a[@class='shopping_cart_link']")
    
    ADD_TO_CART = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    
    BACKET_COUNTER = (By.XPATH,"//span[@class='shopping_cart_badge']")
    
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    CART_ITEM_NAME = (By.XPATH, "//div[@class='inventory_item_name']")