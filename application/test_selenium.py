from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setup_driver():
  options = Options()
  #options.add_argument("")
  driver = webdriver.Chrome()
  return driver
  
def get_site():
  driver = setup_driver()
  driver.get("https://www.duellinksmeta.com/")
  driver.set_window_size(1600, 1200)
  return driver.title

get_site()