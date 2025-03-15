To create a Selenium test script for the given PHP code, we first need to understand that Selenium is used for automating web browsers, and the PHP code provided does not involve a web browser or any graphical user interface. However, assuming that this PHP code is part of a larger web application and is used to display module information on a webpage, we can create a Selenium test script to validate that the module information is correctly displayed.

Here is a sample Selenium test script using Python and the Selenium WebDriver library:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestModulePage(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()

    def test_module_page(self):
        # Navigate to the webpage that displays the module information
        self.driver.get("http://example.com/module-page")

        # Wait for the module ID element to load
        module_id_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "module-id"))
        )

        # Verify that the module ID is correct
        self.assertEqual(module_id_element.text, "11")

        # Wait for the module name element to load
        module_name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "module-name"))
        )

        # Verify that the module name is correct
        self.assertEqual(module_name_element.text, "PATIENT_MANAGEMENT_MODULE")

        # Wait for the module description element to load
        module_description_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "module-description"))
        )

        # Verify that the module description is correct
        self.assertEqual(module_description_element.text, "A module to manage patient information and records.")

        # Wait for the module ID order element to load
        module_id_order_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "module-id-order"))
        )

        # Verify that the module ID order is correct
        self.assertEqual(module_id_order_element.text, "2")

        # Wait for the created at element to load
        created_at_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "created-at"))
        )

        # Verify that the created at date and time is correct
        self.assertEqual(created_at_element.text, "2022-01-11 12:00:00")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

This test script uses Selenium to navigate to a webpage that displays the module information, and then uses assertions to verify that the module ID, name, description, ID order, and created at date and time are correct.

However, to make this script actually work with the given PHP code, you would need to create a webpage that displays the module information. This could involve using a PHP framework such as Laravel or CodeIgniter to create a web application that displays the module information.

Here's a sample PHP code using CodeIgniter framework that displays the module information on a webpage:

```php
<?php

class Module extends CI_Controller {
    public function index() {
        $modules = array(
            array(11, 'PATIENT_MANAGEMENT_MODULE', 'A module to manage patient information and records.', 2, '2022-01-11 12:00:00')
        );

        foreach ($modules as $module) {
            if ($module[0] == 11) {
                $moduleObject = new ModuleModel($module[0], $module[1], $module[2], $module[3], $module[4]);
                $data['module_id'] = $moduleObject->getModuleId();
                $data['module_name'] = $moduleObject->getModuleName();
                $data['module_description'] = $moduleObject->getModuleDescription();
                $data['module_id_order'] = $moduleObject->getModuleIdOrder();
                $data['created_at'] = $moduleObject->getCreatedAt();
            }
        }

        $this->load->view('module_view', $data);
    }
}

class ModuleModel {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleIdOrder;
    private $createdAt;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleIdOrder, $createdAt) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleIdOrder = $moduleIdOrder;
        $this->createdAt = $createdAt;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getModuleName() {
        return $this->moduleName;
    }

    public function getModuleDescription() {
        return $this->moduleDescription;
    }

    public function getModuleIdOrder() {
        return $this->moduleIdOrder;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}
```

And the view (`module_view.php`) would be:

```php
<h1>Module Information</h1>
<p>Module ID: <?php echo $module_id; ?></p>
<p>Module Name: <?php echo $module_name; ?></p>
<p>Module Description: <?php echo $module_description; ?></p>
<p>Module ID Order: <?php echo $module_id_order; ?></p>
<p>Created At: <?php echo $created_at; ?></p>
```

This code creates a webpage that displays the module information. The Selenium test script can then be used to verify that the module information is correctly displayed on the webpage.