import time
from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# unittest class to test the CV page
class cvTest(unittest.TestCase):

    # Initialize the web
    def setUp(self):
        print('Begin Test')
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.webWait = WebDriverWait(self.browser, 20)

    # test the function
    def test_function(self):
        self.title_string = 'Test the Title'
        self.body_string = 'Test the content'

        print('Run the test function')

        # TODO: implement following test tasks
        # Static Function
        # One:Bisite the login page to login the website
        self.browser.get('http://127.0.0.1:8000/login/')
        print('Visit the Login Page')
        time.sleep(1)
        username = self.webWait.until(EC.presence_of_element_located(
            (By.NAME, 'username')))
        password = self.webWait.until(EC.presence_of_element_located(
            (By.NAME, 'password')))
        username.send_keys('huangshukai')
        password.send_keys('huangshukai')
        button = self.webWait.until(EC.element_to_be_clickable((By.XPATH, '//button')))
        button.click()
        time.sleep(1)

        # Two:Visit the Home page and test the loaded information.
        # 1. Test the title
        title = self.browser.title
        print('The title is' + title)
        self.assertEqual('Blog', title)
        # 2. Test the navigation
        cv_text = self.webWait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@id="header-navbar"]/ul[contains(@class,"nav navbar-left")]//li[last()]/a'))).text
        print('The text of the navigation is ' + cv_text)
        self.assertEqual('Personal CV', cv_text)
        # 3. Test the link of the navigation
        cv_url = self.webWait.until(EC.presence_of_element_located((By.XPATH,
                                                                    '//div[@id="header-navbar"]/ul[contains(@class,"nav navbar-left")]//li[last()]/a'))).get_attribute(
            'href')
        print('The link of the navagation is' + cv_url)
        self.assertEqual('http://127.0.0.1:8000/cv/1', cv_url)
        print('Visit the Cv page')
        time.sleep(1)

        # Three:Visit the CV page and test the loaded information
        self.browser.get(cv_url)
        time.sleep(1)
        # 1. Test the title
        title = self.browser.title
        print('The title is' + title)
        self.assertEqual('Personal CV', title)
        # 2. Test the content
        cv_title = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//h1'))).text
        print('The title of the cv is' + cv_title)
        # 3. Test the content
        content = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="article_center"]/h5'))).text
        print('The cv is ' + content)
        time.sleep(1)

        # Dynamic Test
        # Four:Visit the Edit page and Edit the CV content
        button = self.webWait.until(
            EC.element_to_be_clickable((By.XPATH, '//button')))
        button.click()
        print('Visit the Edit page')
        time.sleep(1)
        input_title = self.webWait.until(EC.presence_of_element_located(
            (By.NAME, 'title')))
        input_title.clear()
        input_title.send_keys(self.title_string)
        self.browser.switch_to.frame(0)
        input_content = self.browser.find_element_by_tag_name('body')
        input_content.clear()
        input_content.send_keys(self.body_string)
        self.browser.switch_to.default_content()
        button = self.webWait.until(EC.element_to_be_clickable((By.NAME, '_save')))
        button.click()
        time.sleep(1)

        # Three:Visit the CV page again and test the loaded information
        self.browser.get(cv_url)
        print('Visit the CV page again')
        time.sleep(1)
        # 1. Test the title
        title = self.browser.title
        print('The title is ' + title)
        self.assertEqual('Personal CV', title)
        # 2. Test the CV title
        cv_title = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//h1'))).text
        print('The title is' + cv_title)
        # 3. Test the content
        content = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="article_center"]/h5'))).text
        print('The second time to visit the cv content ' + content)
        time.sleep(1)

        # Six:Test the newest comment blog page
        # 1. Test the title of the newest comment blog
        blogUrl = self.webWait.until(
            EC.element_to_be_clickable((By.XPATH, '//ul[@class="u"]//a')))
        blogTitle = blogUrl.get_attribute('title')
        print('Newest comment blog is' + blogTitle)
        self.browser.get(blogUrl.get_attribute('href'))
        print('Testing the newest comment blog page')
        time.sleep(1)
        title = self.webWait.until(EC.presence_of_element_located((By.XPATH, '//h1/a'))).text
        print('The title is' + title)
        self.assertEqual(title, blogTitle)
        # 2. Test the content
        content = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="article_center"]/h5'))).text
        print('The content is' + content)
        # 3. Test the comment content
        comment = self.webWait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="comment-main"]/p[2]'))).text
        print('The respon of the blog is' + comment)
        time.sleep(3)

    # Quit the test
    def tearDown(self):
        self.browser.quit()
        print('End of the Test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
