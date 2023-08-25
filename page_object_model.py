from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Header:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.experitone.com"

    def get_url(self):
        self.driver.get(self.base_url)

    def contact_button_click(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/div[1]/div[2]/div/nav/div/a").click()

    def login_button_click(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/div[2]/div[2]/div[1]/span/a/svg").click()

    def cart_button_click(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, "/html/body/header/div[2]/div/div[2]/div[2]/div[2]/div/span/span/span[1]/button/svg")))
        cart_button.click()
        # self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/div[2]/div[2]/div/span/span/span["
        #                                    "1]/button/svg").click()

    def cart_button(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/div[2]/div[2]/div/span/span/span["
                                           "1]/button/svg")

    def experitone_logo(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/div[1]/div[1]/div/a/img")


class LandingPage(Header):

    def mix_master_coaching_page_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div/div/div/div[1]/div/div[2]/div["
                                           "1]/h4/a").click()

    def co_mixing_reaper_page_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div["
                                           "1]/h4/a").click()

    def learn_python_programming_page_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div["
                                           "1]/h4/a").click()


class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.experitone.com/contact"

    def get_url(self):
        self.driver.get(self.base_url)

    def first_name_field(self, first_name):
        self.driver.find_element(By.NAME, "firstName"). \
            send_keys(first_name)

    def last_name_field(self, last_name):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/div[2]/div/div/div[3]/div/form/div[1]/div[2]/input").send_keys(
            last_name)

    def email_adress_field(self, adress):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/div[2]/div/div/div[3]/div/form/div[2]/input").send_keys(adress)

    def message_box(self, message):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/div[2]/div/div/div[3]/div/form/div[3]/textarea").send_keys(
            message)

    def send_button_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[3]/div/form/div[6]/button").click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def remove_button_click(self):
        remove_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]")))
        remove_button.click()
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]").click()

    def checkout_button_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div[2]/button/span").click()

    def cart_page_close(self):
        cart_page_close_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, "/html/body/div[4]/div/div[1]/button/svg/path")))
        cart_page_close_button.click()
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/button/svg/path").click()


class ProductPage(LandingPage):

    def pay_what_you_want_field(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[2]/div/div/div[3]/div["
                                           "2]/div/input")

    def add_to_cart_button_click(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[2]/div/div/button[1]")))
        add_to_cart_button.click()
        # self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[2]/div/div/button[1]").click()

    def buy_now_button_click(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[2]/div/div/button[2]").click()


class LoginPage:
    pass
