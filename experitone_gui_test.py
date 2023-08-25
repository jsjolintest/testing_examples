import requests
import xdist
from selenium.webdriver.common.by import By
from page_object_model import ContactPage, LandingPage, Header, ProductPage, CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys
import pytest
from selenium import webdriver


sys.path.append('/app')

test_data = [
    ('test', 'test'),
    (1, 1),
    ('e', 'e'),
    (3, 9),
    (4, 16),
]


# TODO testa speciella bokstäver och symboler i input fält, funktion som jämför input data mot den data som skrivs i
#  fältet


# @pytest.mark.parametrize("input, expected_output", test_data)
# def test_square(input, expected_output):
#     result = compare_input_to_output(input)
#     assert result == expected_output


@pytest.fixture(params=[(1920, 1080), (1280, 720), (1024, 768), (2560, 1440)])
def resolution(request):
    return request.param


@pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "MicrosoftEdge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"])
def headless_browser(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    elif request.param == "MicrosoftEdge":
        options = webdriver.EdgeOptions()
        options.headless = True
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_binary_path
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()


@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def edge_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def get_all_links(firefox_driver):
    # Get all the link elements on the page
    links = firefox_driver.find_elements(By.TAG_NAME, 'a')
    return [link.get_attribute('href') for link in links]


@pytest.mark.functional
class TestFunctional:

    @pytest.mark.smoke
    def test_check_links_validity(self, firefox_driver):

        header_page_object = Header(firefox_driver)
        header_page_object.get_url()

        # contact_page_object = ContactPage(firefox_driver)
        # contact_page_object.get_url()
        #
        # combined_list = [header_page_object.get_url(), contact_page_object.get_url()]

        WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

        all_links = get_all_links(firefox_driver)

        for link in all_links:
            print(link)
            try:
                response = requests.head(link)
                assert response.status_code == 200, f"Link {link} is not valid (Status code: {response.status_code})"
            except requests.ConnectionError:
                assert False, f"Link {link} is not reachable"


@pytest.mark.functional
class TestNavigation:

    def test_contact_button(self, firefox_driver):
        landing_page = LandingPage(firefox_driver)
        landing_page.get_url()


class TestLinks:

    def test_contact_page_class(self):
        contact = ContactPage(firefox_driver)
        contact.last_name_field("test")

    def test_e2e(self):
        landing_page = LandingPage(firefox_driver)
        landing_page.mix_master_coaching_page_click()

    def test_logo(self):
        header_page = Header(firefox_driver)
        header_page.experitone_logo().click()


@pytest.mark.scenario
class TestUserScenario:

    def test_add_and_remove_product_from_cart(self, firefox_driver):
        landing_page = LandingPage(firefox_driver)
        landing_page.get_url()
        landing_page.mix_master_coaching_page_click()
        product_page = ProductPage(firefox_driver)
        product_page.add_to_cart_button_click()
        cart_page = CartPage(firefox_driver)
        cart_page.remove_button_click()
        # cart_page.cart_page_close()

        #TODO hur chckar jag att cart är tom?
        # cart_text = firefox_driver.find_element(By.XPATH, "/html/body/div[4]/div").text
        # if "No items added to cart yet" in cart_text:
        #     print("No items in cart")
        # print(cart_text)
        # assert "No items added to cart yet" == cart_text




# skapa en readme fil där jag kan skiva om mitt tillvägagångssätt.

# if __name__ == '__main__':
#     pytest -m smoke
