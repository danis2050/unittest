import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ProductionGold(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get("http://zoloto585.ru")
        driver.find_element_by_css_selector("#app>header>div.section.header-middle>div>div.header-middle__login>div.header-middle__login-block>div>a:nth-child(1)").click()

        #self.assertIn("Python", driver.title)
        #elem = driver.find_element_by_name("q")
        #elem.send_keys("pycon")
        #assert "No results found." not in driver.page_source
        #elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()