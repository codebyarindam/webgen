### Selenium Test Script for Contact Details Page

The provided Selenium test script in the `tests.py` file is a good start, but it can be improved for better functionality and error handling. Here's an updated version of the script with additional test cases:

```python
from django.test import TestCase
from selenium import webdriver
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ContactDetailsTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            full_name='John Doe',
            phone_numbers='1234567890',
            email='john@example.com',
            address='123 Main St',
            notes='This is a note'
        )
        self.driver = webdriver.Chrome()
        self.url = reverse('contact_details', args=[self.contact.pk])

    def test_contact_details_page(self):
        self.driver.get(self.url)
        self.assertEqual(self.driver.title, 'Contact Details')

    def test_edit_contact_details(self):
        self.driver.get(self.url)
        full_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'full_name'))
        )
        full_name_input.clear()
        full_name_input.send_keys('Jane Doe')

        form = self.driver.find_element(By.TAG_NAME, 'form')
        form.submit()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.url)
            )
            self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, 'Contact Details')
            self.assertEqual(self.driver.find_element(By.NAME, 'full_name').get_attribute('value'), 'Jane Doe')
        except TimeoutException:
            self.fail("Failed to edit contact details")

    def test_contact_information(self):
        self.driver.get(self.url)
        full_name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Full Name:')]"))
        )
        self.assertEqual(full_name_element.text, 'Full Name: John Doe')

        phone_numbers_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Phone Numbers:')]"))
        )
        self.assertEqual(phone_numbers_element.text, 'Phone Numbers: 1234567890')

        email_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Email:')]"))
        )
        self.assertEqual(email_element.text, 'Email: john@example.com')

        address_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Address:')]"))
        )
        self.assertEqual(address_element.text, 'Address: 123 Main St')

        notes_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Notes:')]"))
        )
        self.assertEqual(notes_element.text, 'Notes: This is a note')

    def tearDown(self):
        self.driver.quit()
```

### Changes Made

1. **setUp method**: Moved the creation of the driver to the `setUp` method to ensure that a new driver instance is created for each test method.
2. **Added wait**: Added a wait mechanism using `WebDriverWait` to ensure that the elements are present on the page before attempting to interact with them.
3. **Assertions**: Added more assertions to verify the correctness of the page elements.
4. **Test cases**: Added separate test cases for editing contact details and verifying contact information.
5. **tearDown method**: Added a `tearDown` method to quit the driver instance after each test method.

### Notes

1. Make sure to replace the `contact_details` url in the `tests.py` file with the actual url name from your `urls.py` file.
2. Run the tests using the `python manage.py test` command.
3. Ensure that the Chrome driver is installed and the path to the driver is added to the system's PATH environment variable.