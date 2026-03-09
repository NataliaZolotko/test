import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from data import *

class TestCart:
    @allure.title("Добавление товара в корзину и наличие его в корзине")
    def test_add_to_cart(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.authorization()
        main_page.add_item_to_cart()
        main_page.go_to_cart()
        assert main_page.is_item_in_cart(), "Товар не появился в корзине"
        
      
    @allure.title("Увеличение счетчика корзины при добавлении товара")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.authorization()
        initial_counter = main_page.get_cart_counter()
        main_page.add_item_to_cart()
        new_counter = main_page.get_cart_counter()
        assert new_counter == TestData.expected_counter_value, \
               f"Счетчик корзины должен быть {TestData.expected_counter_value}, но он = {new_counter}"
        
       
    
   