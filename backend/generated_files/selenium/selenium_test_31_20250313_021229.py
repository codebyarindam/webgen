To create a Selenium test script for the given PHP code, we need to first create a web interface that interacts with the Module class. Since the provided PHP code doesn't create any web interface, let's assume that we have a simple HTML page where we can create, read, update, and delete (CRUD) modules.

Here's an example test script in Python using Selenium WebDriver:

```python
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up WebDriver
driver = webdriver.Chrome()  # Use Chrome as the browser

# Function to create a new module
def create_module(driver, id, name, description, order):
    driver.get("http://localhost/create_module.php")  # Navigate to the create module page
    id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "id")))
    name_input = driver.find_element(By.NAME, "name")
    description_input = driver.find_element(By.NAME, "description")
    order_input = driver.find_element(By.NAME, "order")
    submit_button = driver.find_element(By.NAME, "submit")

    id_input.send_keys(id)
    name_input.send_keys(name)
    description_input.send_keys(description)
    order_input.send_keys(order)
    submit_button.click()

# Function to read a module
def read_module(driver, id):
    driver.get(f"http://localhost/read_module.php?id={id}")  # Navigate to the read module page
    try:
        module_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@id='module-id']"))).text
        module_name = driver.find_element(By.XPATH, "//p[@id='module-name']").text
        module_description = driver.find_element(By.XPATH, "//p[@id='module-description']").text
        module_order = driver.find_element(By.XPATH, "//p[@id='module-order']").text
        return module_id, module_name, module_description, module_order
    except TimeoutException:
        return None

# Function to update a module
def update_module(driver, id, name, description, order):
    driver.get(f"http://localhost/update_module.php?id={id}")  # Navigate to the update module page
    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    description_input = driver.find_element(By.NAME, "description")
    order_input = driver.find_element(By.NAME, "order")
    submit_button = driver.find_element(By.NAME, "submit")

    name_input.clear()
    name_input.send_keys(name)
    description_input.clear()
    description_input.send_keys(description)
    order_input.clear()
    order_input.send_keys(order)
    submit_button.click()

# Function to delete a module
def delete_module(driver, id):
    driver.get(f"http://localhost/delete_module.php?id={id}")  # Navigate to the delete module page
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "submit")))
    submit_button.click()

# Test the CRUD operations
def test_module_crud(driver):
    # Create a new module
    create_module(driver, 31, "Index Page", "Display a list of existing groups.", 1)

    # Read the module
    module_id, module_name, module_description, module_order = read_module(driver, 31)
    assert module_id == "31"
    assert module_name == "Index Page"
    assert module_description == "Display a list of existing groups."
    assert module_order == "1"

    # Update the module
    update_module(driver, 31, "Updated Index Page", "Updated display a list of existing groups.", 2)

    # Read the updated module
    module_id, module_name, module_description, module_order = read_module(driver, 31)
    assert module_id == "31"
    assert module_name == "Updated Index Page"
    assert module_description == "Updated display a list of existing groups."
    assert module_order == "2"

    # Delete the module
    delete_module(driver, 31)

# Run the test
test_module_crud(driver)

# Close the browser
driver.quit()
```

Please note that this is a basic example and might need to be adapted to your specific use case. You will also need to create the corresponding PHP files (create_module.php, read_module.php, update_module.php, delete_module.php) to handle the CRUD operations.

Also, make sure to replace the URLs in the test script with the actual URLs of your application.

**PHP Code for CRUD Operations:**

Here is a basic example of how the PHP files for CRUD operations could look like:

**create_module.php:**
```php
<?php
// Create a new module
$id = $_POST["id"];
$name = $_POST["name"];
$description = $_POST["description"];
$order = $_POST["order"];

$module = new Module($id, $name, $description, $order);
// Save the module to the database
?>
```

**read_module.php:**
```php
<?php
// Read a module
$id = $_GET["id"];
$module = // Retrieve the module from the database
?>
<p id="module-id"><?= $module->getId() ?></p>
<p id="module-name"><?= $module->getName() ?></p>
<p id="module-description"><?= $module->getDescription() ?></p>
<p id="module-order"><?= $module->getOrder() ?></p>
```

**update_module.php:**
```php
<?php
// Update a module
$id = $_GET["id"];
$name = $_POST["name"];
$description = $_POST["description"];
$order = $_POST["order"];

$module = // Retrieve the module from the database
$module->setName($name);
$module->setDescription($description);
$module->setOrder($order);
// Save the updated module to the database
?>
```

**delete_module.php:**
```php
<?php
// Delete a module
$id = $_GET["id"];
// Remove the module from the database
?>
```

Remember to replace the comments with the actual database operations.