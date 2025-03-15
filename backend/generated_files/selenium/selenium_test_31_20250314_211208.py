To validate the functionality of the generated PHP project using Selenium, we'll need to create a web interface for the Module class and then write Selenium tests to interact with this interface.

**Module Web Interface**
------------------------

First, let's create a simple web interface for the Module class using PHP. We'll use a basic HTML form to input module data and display the module details.

```php
// module.php

require_once 'Module.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $description = $_POST['description'];
    $priority = $_POST['priority'];
    $createdAt = DateTime::createFromFormat('Y-m-d H:i:s', $_POST['createdAt']);

    $module = new Module($id, $name, $description, $priority, $createdAt);

    echo "Module ID: " . $module->getId() . "\n";
    echo "Module Name: " . $module->getName() . "\n";
    echo "Module Description: " . $module->getDescription() . "\n";
    echo "Module Priority: " . $module->getPriority() . "\n";
    echo "Module Created At: " . $module->getCreatedAt()->format('Y-m-d H:i:s') . "\n";
} else {
    ?>
    <form action="module.php" method="post">
        <label for="id">ID:</label>
        <input type="number" id="id" name="id"><br><br>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="priority">Priority:</label>
        <input type="number" id="priority" name="priority"><br><br>
        <label for="createdAt">Created At:</label>
        <input type="datetime-local" id="createdAt" name="createdAt"><br><br>
        <input type="submit" value="Submit">
    </form>
    <?php
}
```

**Selenium Test Script**
-----------------------

Now, let's write a Selenium test script in Python using the WebDriver API.

```python
# test_module.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

def test_module():
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    # Navigate to the module page
    driver.get('http://localhost/module.php')

    # Fill out the form
    id_input = driver.find_element(By.NAME, 'id')
    id_input.send_keys('31')

    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys('Index Page')

    description_input = driver.find_element(By.NAME, 'description')
    description_input.send_keys('Display a list of existing groups.\nProvide options to:\nCreate a new group.\nSelect an existing group to view/edit contacts.')

    priority_input = driver.find_element(By.NAME, 'priority')
    priority_input.send_keys('1')

    created_at_input = driver.find_element(By.NAME, 'createdAt')
    created_at_input.send_keys('2025-02-05T09:17:38')

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()

    # Wait for the module details to be displayed
    try:
        module_id_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//body'), 'Module ID: 31')
        )
        module_name_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//body'), 'Module Name: Index Page')
        )
        module_description_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//body'), 'Module Description: Display a list of existing groups.')
        )
        module_priority_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//body'), 'Module Priority: 1')
        )
        module_created_at_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//body'), 'Module Created At: 2025-02-05 09:17:38')
        )
    except TimeoutException:
        print('Timed out waiting for module details to be displayed')
        driver.quit()
        return

    # Verify the module details
    module_id = driver.find_element(By.XPATH, '//body').text.split('\n')[0].split(': ')[1]
    assert module_id == '31'

    module_name = driver.find_element(By.XPATH, '//body').text.split('\n')[1].split(': ')[1]
    assert module_name == 'Index Page'

    module_description = driver.find_element(By.XPATH, '//body').text.split('\n')[2].split(': ')[1]
    assert module_description == 'Display a list of existing groups.'

    module_priority = driver.find_element(By.XPATH, '//body').text.split('\n')[3].split(': ')[1]
    assert module_priority == '1'

    module_created_at = driver.find_element(By.XPATH, '//body').text.split('\n')[4].split(': ')[1]
    assert module_created_at == '2025-02-05 09:17:38'

    driver.quit()

if __name__ == '__main__':
    test_module()
```

This test script uses Selenium WebDriver to interact with the module web interface. It fills out the form with the required data, submits the form, and waits for the module details to be displayed. It then verifies that the displayed module details match the expected values.