**PHP Code**
```php
<?php

class Module {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleOrder;
    private $moduleParentId;
    private $moduleCreationDate;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleOrder, $moduleParentId, $moduleCreationDate) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleOrder = $moduleOrder;
        $this->moduleParentId = $moduleParentId;
        $this->moduleCreationDate = $moduleCreationDate;
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

    public function getModuleOrder() {
        return $this->moduleOrder;
    }

    public function getModuleParentId() {
        return $this->moduleParentId;
    }

    public function getModuleCreationDate() {
        return $this->moduleCreationDate;
    }
}

$moduleData = array(
    array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, null, '2025-02-05 09:17:38')
);

$modules = array();

foreach ($moduleData as $data) {
    $module = new Module(
        $data[0],
        $data[1],
        $data[2],
        $data[3],
        $data[4],
        $data[7]
    );
    array_push($modules, $module);
}

foreach ($modules as $module) {
    echo "Module ID: " . $module->getModuleId() . "\n";
    echo "Module Name: " . $module->getModuleName() . "\n";
    echo "Module Description: " . $module->getModuleDescription() . "\n";
    echo "Module Order: " . $module->getModuleOrder() . "\n";
    echo "Module Parent ID: " . $module->getModuleParentId() . "\n";
    echo "Module Creation Date: " . $module->getModuleCreationDate() . "\n\n";
}
```

**Selenium Script using Python**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import unittest

class TestIndexPage(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_index_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/index")

        # Wait for the page to load
        time.sleep(2)

        # Verify the title of the page
        self.assertEqual(driver.title, "Index Page")

        # Verify the groups list is displayed
        groups_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='groups-list']"))
        )
        self.assertTrue(groups_list.is_displayed())

        # Verify the create new group option is displayed
        create_new_group = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='create-new-group']"))
        )
        self.assertTrue(create_new_group.is_displayed())

        # Verify the select existing group option is displayed
        select_existing_group = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='select-existing-group']"))
        )
        self.assertTrue(select_existing_group.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

**Example Usage**

To run the Selenium script, save it as `test_index_page.py` and run it using the command `python test_index_page.py`. This will execute the test case and verify that the index page is displayed correctly.

To use the PHP code, save it as `module.php` and run it using the command `php module.php`. This will create an instance of the `Module` class and print out the module details.