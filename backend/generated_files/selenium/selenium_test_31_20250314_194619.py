Here's a basic Selenium test script to validate the functionality of the provided Django project.

### Test Group Creation

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGroupCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/groups/")

    def test_create_group(self):
        # Click on the "Create New Group" link
        create_group_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create New Group"))
        )
        create_group_link.click()

        # Fill in the group form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Group")

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys("This is a test group")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Check if the group is created successfully
        group_list_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Test Group"))
        )
        self.assertIsNotNone(group_list_link)

    def tearDown(self):
        self.driver.quit()
```

### Test Group Detail View

```python
class TestGroupDetailView(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/groups/")

    def test_group_detail_view(self):
        # Click on the "Create New Group" link
        create_group_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create New Group"))
        )
        create_group_link.click()

        # Fill in the group form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Group")

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys("This is a test group")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Click on the group detail link
        group_detail_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Test Group"))
        )
        group_detail_link.click()

        # Check if the group detail page is displayed
        group_name = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(group_name.text, "Test Group")

    def tearDown(self):
        self.driver.quit()
```

### Test Contact Creation

```python
class TestContactCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/groups/")

    def test_create_contact(self):
        # Click on the "Create New Group" link
        create_group_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create New Group"))
        )
        create_group_link.click()

        # Fill in the group form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Group")

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys("This is a test group")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Click on the group detail link
        group_detail_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Test Group"))
        )
        group_detail_link.click()

        # Click on the "Create New Contact" link
        create_contact_link = self.driver.find_element(By.LINK_TEXT, "Create New Contact")
        create_contact_link.click()

        # Fill in the contact form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Contact")

        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("test@example.com")

        phone_input = self.driver.find_element(By.NAME, "phone")
        phone_input.send_keys("1234567890")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Check if the contact is created successfully
        contact_list = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(contact_list), 0)

    def tearDown(self):
        self.driver.quit()
```

### Test Contact Update

```python
class TestContactUpdate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/groups/")

    def test_update_contact(self):
        # Click on the "Create New Group" link
        create_group_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create New Group"))
        )
        create_group_link.click()

        # Fill in the group form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Group")

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys("This is a test group")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Click on the group detail link
        group_detail_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Test Group"))
        )
        group_detail_link.click()

        # Click on the "Create New Contact" link
        create_contact_link = self.driver.find_element(By.LINK_TEXT, "Create New Contact")
        create_contact_link.click()

        # Fill in the contact form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("Test Contact")

        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("test@example.com")

        phone_input = self.driver.find_element(By.NAME, "phone")
        phone_input.send_keys("1234567890")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Click on the "Edit" link
        edit_link = self.driver.find_element(By.LINK_TEXT, "Edit")
        edit_link.click()

        # Update the contact form
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys("Updated Test Contact")

        # Click the submit button
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Check if the contact is updated successfully
        contact_list = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(contact_list), 0)
        self.assertEqual(contact_list[0].text, "Updated Test Contact")

    def tearDown(self):
        self.driver.quit()
```

Run the tests using the following command:
```bash
python manage.py test
```
Note that these are just basic tests and you may need to add more tests to cover all the functionality of your application. Also, make sure to replace the URLs and locators with the actual values from your application.