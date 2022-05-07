from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

# Create your tests here.

class TestLogin(LiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver(executable_path='/usr/local/bin/chromedriver')

  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super().tearDownClass()

  def test_login(self):
    # open up a login page
    self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

    # login
    username_input = self.selenium.find_element_by_name('login')
    username_input.send_keys('genta.shibasaki.78@gmail.com')
    password_input = self.selenium.find_element_by_name('password')
    password_input.send_keys('komu4839')
    self.selenium.find_element_by_class_name('btn').click()

    # confirm page title 
    self.assertEquals('日記一覧 | Private Diary', self.selenium.title)