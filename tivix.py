import unittest
from selenium import webdriver
import time

class KarolinaTivixCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_career(self):
        global driver
        driver = self.driver
        driver.get("https://www.tivix.com/")
        driver.maximize_window()
        career1_btn = driver.find_element_by_css_selector('a[href="/careers"]')
        career1_btn.click()
        time.sleep(10)
        career2_btn = driver.find_element_by_css_selector('a[href="https://jobs.lever.co/tivix/"]')
        career2_btn.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
