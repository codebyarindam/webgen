To create a Selenium test script for this PHP code, we'll need to create a simple web page that displays the details of the `Module` object. Then we'll write a Selenium test to verify that the web page displays the correct information.

First, let's modify the PHP code to create a simple web page:

```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $displayOrder;
    private $createdBy;
    private $updatedBy;
    private $createdAt;
    private $updatedAt;

    public function __construct($id, $name, $description, $displayOrder, $createdBy, $updatedBy, $createdAt, $updatedAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->displayOrder = $displayOrder;
        $this->createdBy = $createdBy;
        $this->updatedBy = $updatedBy;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
    }

    public function __toString() {
        return "Module " . $this->id . ": " . $this->name . "\nDescription: " . $this->description . "\nDisplay Order: " . $this->displayOrder . "\nCreated By: " . $this->createdBy . "\nUpdated By: " . $this->updatedBy . "\nCreated At: " . $this->createdAt . "\nUpdated At: " . $this->updatedAt;
    }

    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getDisplayOrder() {
        return $this->displayOrder;
    }

    public function getCreatedBy() {
        return $this->createdBy;
    }

    public function getUpdatedBy() {
        return $this->updatedBy;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }

    public function getUpdatedAt() {
        return $this->updatedAt;
    }
}

$data = array("id" => 31, "name" => 'Index Page', "description" => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', "displayOrder" => 1, "createdBy" => null, "updatedBy" => null, "createdAt" => '2025-02-05 09:17:38', "updatedAt" => null);

$module = new Module($data["id"], $data["name"], $data["description"], $data["displayOrder"], $data["createdBy"], $data["updatedBy"], $data["createdAt"], $data["updatedAt"]);

?>

<html>
    <body>
        <h1>Module Details</h1>
        <p>Module ID: <?php echo $module->getId(); ?></p>
        <p>Module Name: <?php echo $module->getName(); ?></p>
        <p>Module Description: <?php echo $module->getDescription(); ?></p>
        <p>Display Order: <?php echo $module->getDisplayOrder(); ?></p>
        <p>Created By: <?php echo $module->getCreatedBy(); ?></p>
        <p>Updated By: <?php echo $module->getUpdatedBy(); ?></p>
        <p>Created At: <?php echo $module->getCreatedAt(); ?></p>
        <p>Updated At: <?php echo $module->getUpdatedAt(); ?></p>
    </body>
</html>
```

Save this code in a file named `index.php`.

Now, let's create a Selenium test script in Python:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_module_details():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the web page
    driver.get("http://localhost/index.php")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Verify the module details
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Module ID')]").text == "Module ID: 31"
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Module Name')]").text == "Module Name: Index Page"
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Module Description')]").text == "Module Description: Display a list of existing groups.\nProvide options to:\nCreate a new group.\nSelect an existing group to view/edit contacts."
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Display Order')]").text == "Display Order: 1"
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Created By')]").text == "Created By: "
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Updated By')]").text == "Updated By: "
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Created At')]").text == "Created At: 2025-02-05 09:17:38"
    assert driver.find_element(By.XPATH, "//p[contains(text(), 'Updated At')]").text == "Updated At: "

    # Close the browser window
    driver.quit()

# Run the test
test_module_details()
```

This test script uses Selenium to navigate to the `index.php` page, wait for the page to load, and then verify the module details displayed on the page.

Please note that you'll need to have the Selenium WebDriver for Chrome installed on your system and the `chromedriver.exe` file should be in your system's PATH. You'll also need to have the `selenium` library installed in your Python environment. You can install it using pip:

```bash
pip install selenium
```