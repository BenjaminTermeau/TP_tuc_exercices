from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cI(self):
    self.driver.get("https://www.duellinksmeta.com/")
    self.driver.set_window_size(1600, 1200)
    return self.driver.title
    
  def test_wiki(self):
    self.driver.get("https://wikiroulette.co/")
    return self.driver.title
  
