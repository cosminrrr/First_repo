
from time import sleep
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o singura data
    Signup_Login_BTN = (By.XPATH, '//a[@href="/login"]/i[@class="fa fa-lock"]')
    Register_BTN = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    Name_Signup = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    Email_Signup = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    Register_pass = (By.ID, 'password')
    Register_gender = (By.ID, 'id_gender1')
    Register_day = (By.ID, 'days')
    Register_month = (By.ID, 'months')
    Register_year = (By.ID, 'years')
    Register_first_name = (By.ID, 'first_name')
    Register_last_name = (By.ID, 'last_name')
    Register_adress = (By.ID, 'address1')
    Register_country = (By.ID, 'country')
    Register_state = (By.ID, 'state')
    Register_city = (By.ID, 'city')
    Register_zip_code = (By.ID, 'zipcode')
    Register_mobile_number = By.ID, 'mobile_number'
    Create_account_btn = (By.XPATH, '//button[@data-qa="create-account"]')
    Submit_success_message = (By.XPATH, '//p[@style="font-size: 20px; font-family: garamond;"]')
    Subscription_box = (By.ID, 'susbscribe_email')
    Subscription_btn = (By.ID, 'subscribe')
    Subscription_congrats = (By.ID, 'success-subscribe')
    Login_box_email = (By.XPATH, '//input[@type="email" and @data-qa="login-email"]')
    Login_box_pass = (By.XPATH, '//input[@data-qa="login-password"]')
    Login_acc_btn = (By.XPATH, '//button[@type="submit" and @data-qa="login-button"]')
    Logout_btn = (By.XPATH, '//a[@href="/logout"]')
    Delete_acc = (By.XPATH, '//a[@href="/delete_account"]')
    Fake_Login = (By.XPATH, "//p[@style='color: red;']")
    Products_Btn = (By.LINK_TEXT, "https://automationexercise.com/products")

    #2 se rulaza inainte de fiecare test si are rolul de a face set-up-ul de chrome inainte de fiecare test
    #Am implemetat metoda def setUp care se va rula inaintea fiecarui test. Are rolul de a face setUp-ul browser-ului
    #de chrome inainte de fiecare test cat si accesarea link-ului ste-ului testat.


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://automationexercise.com/')

    #3 Apoi am implementat metoda teardown- care se va
    # executa la finalizare fiecarui test.
    # Mai exact acici inchidem browser-ul chrome
    def tearDown(self):
        self.chrome.quit()

    # TEST 1 # Primul test este pt a verifica url-ul site-ului



    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://automationexercise.com/'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')




    # TEST 2 pentru a verifica titul paginii

    def test_page_title(self):
        actual = self.chrome.title  # se extrage automat titlul paginii incarcate prin intermediul metodei title
        print(f"Titlul extras al paginii este {actual}")
        expected = 'Automation Exercise'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # TEST 3 , aici am verificat corectitudinea afisarii titlului paginii de inregistrare/login
    def test_sign_up_page(self):
        self.chrome.find_element(*self.Signup_Login_BTN).click()
        actual = self.chrome.title
        expected = 'Automation Exercise - Signup / Login'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # TEST 4
    def test_new_user_form(self):
        self.chrome.find_element(*self.Signup_Login_BTN).click()
        elem = self.chrome.find_element(*self.Register_BTN)
        self.assertTrue(elem.is_displayed(), 'New user form nu e vizibil')

    # TEST 5 Aici testam creare unui user nou

    def test_register_new_user(self):
        self.chrome.find_element(*self.Signup_Login_BTN).click()
        self.chrome.find_element(*self.Name_Signup).send_keys('Rusu Constantin')
        self.chrome.find_element(*self.Email_Signup).send_keys('conturi4@gmail.com')
        self.chrome.find_element(*self.Register_BTN).click()
        self.chrome.find_element(*self.Register_pass).send_keys('12345')
        self.chrome.find_element(*self.Register_gender).click()
        subject_heading_option1 = Select(self.chrome.find_element(*self.Register_day))
        subject_heading_option1.select_by_visible_text("23")
        subject_heading_option2 = Select(self.chrome.find_element(*self.Register_month))
        subject_heading_option2.select_by_visible_text("February")
        subject_heading_option3 = Select(self.chrome.find_element(*self.Register_year))
        subject_heading_option3.select_by_visible_text("1993")
        self.chrome.find_element(*self.Register_first_name).send_keys('Rusu')
        self.chrome.find_element(*self.Register_last_name).send_keys('Constantin')
        self.chrome.find_element(*self.Register_adress).send_keys("Str. Plaurului nr 17")
        subject_heading_country = Select(self.chrome.find_element(*self.Register_country))
        subject_heading_country.select_by_visible_text("United States")
        self.chrome.find_element(*self.Register_state).send_keys("NYC")
        self.chrome.find_element(*self.Register_city).send_keys("NYC")
        self.chrome.find_element(*self.Register_zip_code).send_keys("12345")
        self.chrome.find_element(*self.Register_mobile_number).send_keys("0730784055")
        sleep(6)
        self.chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(5)
        self.chrome.find_element(*self.Create_account_btn).click()
        actual = self.chrome.current_url
        expected = 'https://automationexercise.com/account_created'
        # expected value, actual value, mesaj in caz de fail test
        self.assertEqual(expected, actual, 'URL is incorrect')
        self.chrome.find_element(*self.Continue_btn).click()

        # TEST 6 Testam abonarea cu o adresa de email

    def test_sub_by_email(self):
        self.chrome.find_element(*self.Subscription_box).send_keys('conturi4@gmail.com')
        self.chrome.find_element(*self.Subscription_btn).click()
        expected = "You have been successfully subscribed!"
        actual = self.chrome.find_element(*self.Subscription_congrats).text
        self.assertEqual(expected, actual, "Submit did not work")

        # TEST 7 testam logarea in site

    def test_login_account(self):
        self.chrome.find_element(*self.Signup_Login_BTN).click()
        self.chrome.find_element(*self.Login_box_email).send_keys('conturi4@gmail.com')
        self.chrome.find_element(*self.Login_box_pass).send_keys('12345')
        self.chrome.find_element(*self.Login_acc_btn).click()
        expected = "https://automationexercise.com/"
        actual = self.chrome.current_url
        assert actual == expected, f'INVALID URL: expected {expected} but found {actual}'

        print('TEST PASSED')


    # TEST 8 verificam logarea cu un user care nu este inregistrat
    def test_fake_log(self):
        self.chrome.find_element(*self.Signup_Login_BTN).click()
        self.chrome.find_element(*self.Login_box_email).send_keys('fake@gmail.com')
        self.chrome.find_element(*self.Login_box_pass).send_keys('12345')
        self.chrome.find_element(*self.Login_acc_btn).click()
        expected = "https://automationexercise.com/login"
        actual= self.chrome.current_url
        assert actual == expected, f'INVALID URL: expected {expected} but found {actual}'

        print('TEST PASSED')













