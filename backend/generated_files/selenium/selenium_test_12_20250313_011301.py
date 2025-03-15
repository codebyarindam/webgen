To write a Selenium test script for the provided PHP project, we need to ensure that the project is set up as a web application that can be interacted with through a web browser. Since the provided PHP code is a simple script that prints out module information to the console, we'll need to create a simple web application that displays this information.

For the purpose of this example, let's assume that we've modified the PHP script to create a web page that displays the module information. We'll then use Selenium with Python to write a test script that validates the functionality of this web application.

### Modified PHP Script

```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $level;
    private $parent_id;
    private $created_at;
    private $updated_at;
    private $deleted_at;
    private $module_id;

    public function __construct($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->level = $level;
        $this->parent_id = $parent_id;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
        $this->deleted_at = $deleted_at;
        $this->module_id = $module_id;
    }

    public function get_id() {
        return $this->id;
    }

    public function get_name() {
        return $this->name;
    }

    public function get_description() {
        return $this->description;
    }

    public function get_level() {
        return $this->level;
    }

    public function get_parent_id() {
        return $this->parent_id;
    }

    public function get_created_at() {
        return $this->created_at;
    }

    public function get_updated_at() {
        return $this->updated_at;
    }

    public function get_deleted_at() {
        return $this->deleted_at;
    }

    public function get_module_id() {
        return $this->module_id;
    }
}

$data = array(
    array(12, 'DOCTOR_MANAGEMENT_MODULE', 'A module to manage doctor information and schedules.', 2, null, null, null, 12, new DateTime('2022-01-12 12:00:00'))
);

$modules = array();
foreach ($data as $module_data) {
    list($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id) = $module_data;
    $created_at = $created_at ? new DateTime($created_at) : null;
    $updated_at = $updated_at ? new DateTime($updated_at) : null;
    $deleted_at = $deleted_at ? new DateTime($deleted_at) : null;
    $modules[] = new Module($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id);
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Module Information</title>
</head>
<body>
    <h1>Module Information</h1>
    <ul>
    <?php foreach ($modules as $module) { ?>
        <li>
            <h2>Module <?php echo $module->get_id(); ?></h2>
            <p>Name: <?php echo $module->get_name(); ?></p>
            <p>Description: <?php echo $module->get_description(); ?></p>
            <p>Level: <?php echo $module->get_level(); ?></p>
            <p>Parent ID: <?php echo $module->get_parent_id() !== null ? $module->get_parent_id() : 'None'; ?></p>
            <p>Created At: <?php echo $module->get_created_at() !== null ? $module->get_created_at()->format('Y-m-d H:i:s') : 'None'; ?></p>
            <p>Updated At: <?php echo $module->get_updated_at() !== null ? $module->get_updated_at()->format('Y-m-d H:i:s') : 'None'; ?></p>
            <p>Deleted At: <?php echo $module->get_deleted_at() !== null ? $module->get_deleted_at()->format('Y-m-d H:i:s') : 'None'; ?></p>
            <p>Module ID: <?php echo $module->get_module_id(); ?></p>
        </li>
    <?php } ?>
    </ul>
</body>
</html>
```

### Selenium Test Script

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestModuleInformationPage(unittest.TestCase):

    def setUp(self):
        # Set up the webdriver
        self.driver = webdriver.Chrome()

    def test_module_information_page(self):
        # Navigate to the module information page
        self.driver.get("http://localhost:8080/module_info.php")

        # Wait for the module information to be loaded
        try:
            module_info = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ul"))
            )
        except TimeoutException:
            self.fail("Module information not loaded")

        # Verify the module information
        modules = self.driver.find_elements(By.XPATH, "//li")
        self.assertEqual(len(modules), 1)

        module = modules[0]
        self.assertEqual(module.find_element(By.TAG_NAME, "h2").text, "Module 12")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='name']").text, "Name: DOCTOR_MANAGEMENT_MODULE")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='description']").text, "Description: A module to manage doctor information and schedules.")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='level']").text, "Level: 2")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='parent_id']").text, "Parent ID: None")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='created_at']").text, "Created At: 2022-01-12 12:00:00")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='updated_at']").text, "Updated At: None")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='deleted_at']").text, "Deleted At: None")
        self.assertEqual(module.find_element(By.XPATH, ".//p[@class='module_id']").text, "Module ID: 12")

    def tearDown(self):
        # Close the webdriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

**Note**: This test script assumes that you're running the PHP script on a local server (e.g., `http://localhost:8080/module_info.php`). You may need to modify the URL in the test script to match your own setup.

**Also note**: The test script is written in Python and uses the Selenium WebDriver API to interact with the web page. You'll need to have Python and the Selenium WebDriver installed on your system to run this test script.

The test script verifies that the module information is displayed correctly on the web page, including the module ID, name, description, level, parent ID, created at, updated at, deleted at, and module ID. If any of these values are incorrect or missing, the test will fail.