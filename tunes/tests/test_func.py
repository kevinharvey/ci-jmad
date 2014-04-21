from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from authtools.models import User

class TunesFunctionalTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(self):
        self.user = User.objects.create(email="jill@example.com")
        self.user.set_password("password")
        self.user.save()
        
        self.selenium = WebDriver()
        super(TunesFunctionalTestCase, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        self.selenium.quit()
        super(TunesFunctionalTestCase, self).tearDownClass()
    
    def test_login_and_add_tune_info(self):
        """
        Log in to the site, find a tune by name, and add some
        info about it.
        """

        # Jill goes to the home page of the site and logs in
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_css_selector("a#tuw-login").click()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('jill@example.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_css_selector('form#tuw-login button#tuw-submit-login').click()

        # she clicks the "Add new info" button
        self.selenium.find_element_by_css_selector('a#tuw-add-new-info').click()

        # and then selects "Tune"
        self.selenium.find_element_by_css_selector('a#tuw-tune-edit').click()

        # she searches for the word "Night"
        search_form = self.selenium.find_element_by_name("search")
        search_form.send_keys("Night")
        self.selenium.find_element_by_css_selector('form#tuw-login input#tuw-submit-search') 

        # and sees a few options
        #   "The Night Has a Thousand Eyes"
        #   "Night in Tunisia"
        #   "Night Train"
        
        # She selects "Night Train, and since we already have some info
        # about this tune in the database, she sees and partially
        # filled form

        # She adds what data she can about "Night Train" and 
        # saves the form

        # She wants to add another tune to the database, so she clicks
        # "Edit Another Tune"

        # She searches for the word "Mood"

        # and sees a few options
        #   "Mood Indigo"
        #   "In a Sentimental Mood"

        # She selects "In a Sentimental Mood", and since there's no 
        # info in the database about this tune yet, she see's a 
        # completely empty form

        # She enters all the information she knows about this tune in
        # in the form and clicks save.

        # When shes's done, she goes to the home page to the home page
        # and sees the newly added tunes

        self.fail("FINISH THE TEST")
