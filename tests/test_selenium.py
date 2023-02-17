from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestCI():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless")
    self.driver = webdriver.Chrome()
    self.verificationErrors = []
    self.accept_next_alert = True
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cI(self):
    self.driver.get("https://www.duellinksmeta.com/")
    self.driver.set_window_size(1600, 1200)
    return self.driver.title
    
  def test_wiki(self):
    self.driver.get("https://wikiroulette.co/")
    return self.driver.title
  
