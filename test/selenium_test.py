from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import inspect
import time

# java -jar selenium-server-standalone-3.141.59.jar
# CLI command to start the selenium server on port 4444


class TestWebsite(unittest.TestCase):
    """A class that holds tests to be run for game-aid

        Roy Ortega - A01078553
        ACIT 2911 - Set 2B
        May 2, 2020"""

    def setUp(self) -> None:
        """Initializes a test"""
        self.driver = webdriver.Chrome('/home/travis/virtualenv/python3.7.1/bin/')
        self.driver.get("http://game-aid.ca/wp/")
        self.driver.implicitly_wait(2) # Waits in seconds to find elements
        self.logPoint()

    def tearDown(self):
        """Log point for end of test"""
        self.driver.close()
        self.logPoint()

    def logPoint(self):
        """Creates log point function to be run after each set up and teardown"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_logo(self):
        """TP000-A Tests the logo portion of the header"""
        print('Testing Logo')
        logo = self.driver.find_element_by_xpath('//a')
        logo.click()
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://game-aid.ca/wp/', 'Should return http://game-aid.ca/wp/')

    def test_fps(self):
        """TP001-A Tests clicking an image in the front page"""
        print('Testing FPS Row - Landing Page')

        # Sets images to variables
        img_1 = self.driver.find_element_by_id('fps-i1')
        img_2 = self.driver.find_element_by_id('fps-i2')
        img_3 = self.driver.find_element_by_id('fps-i3')
        img_4 = self.driver.find_element_by_id('fps-i4')
        click_button = self.driver.find_element_by_id('fps-click')

        # Clicks images and clicks the redirection button
        img_1.click()
        img_2.click()
        img_3.click()
        img_4.click()
        click_button.click()

    def test_mmo(self):
        """TP001-B Tests clicking an image in the front page"""
        print('Testing MMO Row - Landing Page')

        # Sets variables
        img_1 = self.driver.find_element_by_id('mmo-i1')
        img_2 = self.driver.find_element_by_id('mmo-i2')
        img_3 = self.driver.find_element_by_id('mmo-i3')
        img_4 = self.driver.find_element_by_id('mmo-i4')
        click_button = self.driver.find_element_by_id('mmo-click')

        # Clicks all images and the redirection button
        img_1.click()
        img_2.click()
        img_3.click()
        img_4.click()
        click_button.click()

    def test_rts(self):
        """TP001-C Tests clicking an image in the front page"""
        print('Testing RTS Row - Landing Page')

        # Sets variables
        img_1 = self.driver.find_element_by_id('rts-i1')
        img_2 = self.driver.find_element_by_id('rts-i2')
        img_3 = self.driver.find_element_by_id('rts-i3')
        img_4 = self.driver.find_element_by_id('rts-i4')
        click_button = self.driver.find_element_by_id('rts-click')

        # Clicks all images and redirection button
        img_1.click()
        img_2.click()
        img_3.click()
        img_4.click()
        click_button.click()

    def test_login(self):
        """TP002-A Tests successful login"""
        print('Testing Successful Login')

        #
        self.driver.find_element_by_link_text('Login').click()


        login_area = self.driver.find_element_by_id('username-257')
        password_area = self.driver.find_element_by_id('user_password-257')
        login_button = self.driver.find_element_by_id('um-submit-btn')

        login_area.click()
        login_area.send_keys('test')

        password_area.click()
        password_area.send_keys('Testing1')

        login_button.click()

        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://game-aid.ca/wp/user/test/',
                         'Should return http://game-aid.ca/wp/user/test/')

    def test_login_false_username(self):
        """TP002-B Tests unsuccessful login with non-existent username"""
        print('Testing Unsuccessful Login with non-existent username')

        self.driver.find_element_by_link_text('Login').click()

        login_area = self.driver.find_element_by_id('username-257')
        password_area = self.driver.find_element_by_id('user_password-257')
        login_button = self.driver.find_element_by_id('um-submit-btn')

        login_area.click()
        login_area.send_keys('notarealuser')

        password_area.click()
        password_area.send_keys('notarealpassword')

        login_button.click()

        unknown_user_error = self.driver.find_element_by_class_name('um-error-code-invalid_username').text
        self.assertEqual(unknown_user_error, "Unknown username. Check again or try your email address.",
                         'Should return "Unknown username. Check again or try your email address."')

    def test_login_false_password(self):
        """TP002-C Tests unsuccessful login with non-existent username"""
        print('Testing Unsuccessful Login with wrong password.')

        # Navigates to login page
        self.driver.find_element_by_link_text('Login').click()

        # Sets login text fields to variables
        login_area = self.driver.find_element_by_id('username-257')
        password_area = self.driver.find_element_by_id('user_password-257')
        login_button = self.driver.find_element_by_id('um-submit-btn')

        # Enters login information
        login_area.click()
        login_area.send_keys('test')
        password_area.click()
        password_area.send_keys('notarealpassword')
        login_button.click()

        # Checks for proper error message
        unknown_pass_error = self.driver.find_element_by_class_name('um-field-error').text
        self.assertEqual(unknown_pass_error, "Password is incorrect. Please try again.",
                         'Should return "Password is incorrect. Please try again."')

    def test_loguot(self):
        """TP-003-A Tests successful logout"""
        print('Testing Successful Logout')

        # Navigates to login page
        self.driver.find_element_by_link_text('Login').click()

        # Sets text fields as variables
        login_area = self.driver.find_element_by_id('username-257')
        password_area = self.driver.find_element_by_id('user_password-257')
        login_button = self.driver.find_element_by_id('um-submit-btn')

        # Enters login information and enters
        login_area.click()
        login_area.send_keys('test')

        password_area.click()
        password_area.send_keys('Testing1')

        login_button.click()

        logout_link = self.driver.find_element_by_link_text('Login')  # Will need to fix this to say 'Logout'
        logout_link.click()
        print('this worked')

        logout_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Logout')]")

        logout_button.click()

        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://game-aid.ca/wp/login/',
                         'Should return http://game-aid.ca/wp/login/')

    def test_profile(self):
        """TP-004-A Tests profile page for a coach"""
        print('Testing profile information')

        # Navigates to page of interest
        self.driver.find_element_by_id('fps-click').click()
        self.driver.find_element_by_id('fps-coaches').click()
        self.driver.find_element_by_id('profile-1').click()

        # Assigns current url after a click and checks if it redirects properly
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://game-aid.ca/wp/fps-coach1/',
                         'Should return http://game-aid.ca/wp/fps-coach1/')

        # Assigns variables to web-page elements, found by ID
        coach_name = self.driver.find_element_by_id('coach-name')
        coach_stats = self.driver.find_element_by_id('coach-stats')
        coach_img = self.driver.find_element_by_id('coach-img')

        # Checks if element exists, is a string, as well as the value of the text
        self.assertTrue(coach_name)
        self.assertIsInstance(coach_name.text, str, 'Element should contain a string')
        self.assertEqual(coach_name.text, 'Jaguar "Hackermanz" Perlas',
                         'Should equal "Jaguar "Hackermanz" Perlas"')

        # Checks if element actually exists
        self.assertTrue(coach_stats.is_displayed())
        self.assertTrue(coach_img.is_displayed())

    def test_register_pass(self):
        """TP-005-A Tests a successful registration attempt

            Originally planned to implement this, however since it uses a live database and
            no access to it, we cannot mock it without making an actual account
        """
        pass

    def test_register_user_fail(self):
        """TP-005-B Tests an unsuccessful username registration attempt"""
        print('Testing Unsuccessful Registration [USERNAME]')

        # Navigates to registration form
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_class_name('um-alt').click()

        # Enters registration information
        self.driver.find_element_by_id('user_login-256').send_keys('')
        self.driver.find_element_by_id('first_name-256').send_keys('roger')
        self.driver.find_element_by_id('last_name-256').send_keys('rabbit')
        self.driver.find_element_by_id('user_email-256').send_keys('mangosentinel@hotmail.com')
        self.driver.find_element_by_id('user_password-256').send_keys('Thisismypassword1')
        self.driver.find_element_by_id('confirm_user_password-256').send_keys('Thisismypassword1')
        self.driver.find_element_by_id('um-submit-btn').click()

        # Asserts if the right error message is produced
        username_error = self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ),'
                                                           ' concat( " ", "um-field-error", " " ))]').text
        self.assertEqual(username_error, "Username is required",
                         'Should say "Username is required"')

    def test_register_email_fail(self):
        """TP-005-C Tests an unsuccessful email registration attempt"""
        print('Testing Unsuccessful Registration [EMAIL]')

        # Navigates to registration form
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_class_name('um-alt').click()

        # Enters registration information
        self.driver.find_element_by_id('user_login-256').send_keys('rogerrabbit')
        self.driver.find_element_by_id('first_name-256').send_keys('roger')
        self.driver.find_element_by_id('last_name-256').send_keys('rabbit')
        self.driver.find_element_by_id('user_email-256').send_keys('mangosentinel')
        self.driver.find_element_by_id('user_password-256').send_keys('Thisismypassword1')
        self.driver.find_element_by_id('confirm_user_password-256').send_keys('Thisismypassword1')
        self.driver.find_element_by_id('um-submit-btn').click()

        # Asserts if the right error message is produced
        email_error = self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), '
                                                        'concat( " ", "um-field-error", " " ))]').text
        self.assertEqual(email_error, "This is not a valid email",
                         'Should say "This is not a valid email"')

    def test_register_password_fail(self):
        """TP-005-B Tests an unsuccessful registration attempt"""
        print('Testing Unsuccessful Registration [PASSWORD]')

        # Navigates to register page
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_class_name('um-alt').click()

        # Enters user information and clicks
        self.driver.find_element_by_id('user_login-256').send_keys('rogerrabbit')
        self.driver.find_element_by_id('first_name-256').send_keys('roger')
        self.driver.find_element_by_id('last_name-256').send_keys('rabbit')
        self.driver.find_element_by_id('user_email-256').send_keys('mangosentinel@hotmail.com')
        self.driver.find_element_by_id('user_password-256').send_keys('thisismypassword')
        self.driver.find_element_by_id('confirm_user_password-256').send_keys('thisismypassword')
        self.driver.find_element_by_id('um-submit-btn').click()

        # Asserts if element equals the proper text
        password_error = self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), '
                                                           'concat( " ", "um-field-error", " " ))]').text
        self.assertEqual(password_error, "Your password must contain at least one lowercase letter, "
                                         "one capital letter and one number",
                         'Should say "Your password must contain at least one lowercase letter,'
                         ' one capital letter and one number"')

    def test_footer(self):
        """TP-006-A Tests the footer"""
        self.driver.find_element_by_id('fps-click').click()

        # Sets the variables to be tested
        footer_text = self.driver.find_element_by_id('footer-text')
        copyright_text = self.driver.find_element_by_id('copyright')
        social_media_buttons = self.driver.find_element_by_class_name('social-media')

        # Tests the elements through assertions or clicks to check if its a button
        self.assertEqual(footer_text.text, 'Game with confidence', 'Should be "Game with confidence"')
        self.driver.find_element_by_id('get-coached').click()
        self.assertEqual(copyright_text.text, '© All rights reserved', 'Should be "© All rights reserved"')
        social_media_buttons.click()


if __name__ == "__main__":
    unittest.main()
