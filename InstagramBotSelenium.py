from time import sleep
from selenium import webdriver

# username: carbot_88
# password: instagrambot56
# email: rayle88@outlook.com

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        # self.browser.find_element_by_xpath("//a[text()='Log In']").click()
        sleep(2)
        return LoginPage(self.browser)
 

browser = webdriver.Firefox()
# If can't find login_link, wait 5 more seconds before refreshing
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("carbot_88", "instagrambot56")

browser.close()
