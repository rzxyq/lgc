from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # change to explicit wait when app gets complicted

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # open the homepage
        self.browser.get(self.live_server_url)


# class NewVisitorTest(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3) # change to explicit wait when app gets complicted

#     def tearDown(self):
#         self.browser.quit()

#     def test_can_start_a_list_and_retrieve_it_later(self):
#         # open the homepage
#         self.browser.get(self.live_server_url)

#         # notices the page title and header mentions to-do list
#         self.assertIn('To-Do', self.browser.title)
#         header_text = self.browser.find_element_by_tag_name('h1').text
#         self.assertIn('To-Do', header_text)

#         # invited to enter a to-do list right-away
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

#         # entered an item. is taken to a new URL when hit enter. 
#         inputbox.send_keys('Buy peacock feathers')
#         inputbox.send_keys(Keys.ENTER)
#         edith_list_url = self.browser.current_url
#         self.assertRegex(edith_list_url, '/lists/.+')
#         # make sure it's actually in the table!
#         self.check_for_row_in_list_table('1: Buy peacock feathers')

#         # enter a second item
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Use peacock feathers to make a fly')
#         inputbox.send_keys(Keys.ENTER)
#         # page updates again, now show both items on her list
#         self.check_for_row_in_list_table('1: Buy peacock feathers')
#         self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')




#         # Now a new user, Francis, comes to the site
#         # We use a new browser session to make sure that no info of EEdith is coming through from cookies
#         self.browser.quit()
#         self.browser = webdriver.Firefox()

#         # Fracis visits the home page, no sign of Edith's list
#         self.browser.get(self.live_server_url)
#         page_text = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_text)
#         self.assertNotIn('Use peacock feathers to make a fly', page_text)

#         # Francis starts a new list
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy milk')
#         inputbox.send_keys(Keys.ENTER)

#         # Francis gets his own new URL
#         francis_list_url = self.browser.current_url
#         self.assertRegex(edith_list_url, '/lists/.+')
#         self.assertNotEqual(francis_list_url, edith_list_url)
#         # the new URL doesn't have edith's trace
#         page_text = self.browser.find_elements_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_text)
#         self.check_for_row_in_list_table('1: Buy milk')


#         self.fail('Finish the test!')


#     def check_for_row_in_list_table(self, row_text):
#         table = self.browser.find_element_by_id('id_list_table')
#         rows = table.find_elements_by_tag_name('tr')
#         # self.assertTrue(
#         #   any(row.text == '1: Buy peacock feathers' for row in rows), 
#         #   "New to do item did not appear in table -- its text was:\n%s" % (table.text,)
#         # )
#         self.assertIn(row_text, [row.text for row in rows])
