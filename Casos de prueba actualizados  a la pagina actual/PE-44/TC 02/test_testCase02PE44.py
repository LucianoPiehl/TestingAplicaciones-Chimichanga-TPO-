# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestCase02PE44():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCase02PE44(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(968, 1038)
    self.driver.find_element(By.ID, "logo").click()
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(3) td:nth-child(1) #itemImage").click()
    self.driver.find_element(By.LINK_TEXT, "Add to Cart").click()
  
