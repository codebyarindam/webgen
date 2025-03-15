**PHP Code Generation**

Based on the provided data, I will generate a PHP code that creates a module detail page. This page will display a list of existing groups, provide options to create a new group, and select an existing group to view or edit contacts.

```php
// Module.php

class Module {
    private $id;
    private $name;
    private $description;
    private $groupId;
    private $creationDate;

    public function __construct($id, $name, $description, $groupId, $creationDate) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->groupId = $groupId;
        $this->creationDate = $creationDate;
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

    public function getGroupId() {
        return $this->groupId;
    }

    public function getCreationDate() {
        return $this->creationDate;
    }
}

// ModuleDetails.php

class ModuleDetails {
    private $modules;

    public function __construct() {
        $this->modules = array();
    }

    public function addModule($module) {
        array_push($this->modules, $module);
    }

    public function displayModules() {
        foreach ($this->modules as $module) {
            echo "Module ID: " . $module->getId() . "\n";
            echo "Module Name: " . $module->getName() . "\n";
            echo "Module Description: " . $module->getDescription() . "\n";
            echo "Group ID: " . $module->getGroupId() . "\n";
            echo "Creation Date: " . $module->getCreationDate() . "\n\n";
        }
    }
}

// Usage

$moduleDetails = new ModuleDetails();

$module = new Module(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, new DateTime('2025-02-05 09:17:38'));
$moduleDetails->addModule($module);

$moduleDetails->displayModules();
```

**Selenium Script using Python**

To automate the interaction with the module detail page, we can use Selenium with Python. Here's an example script:

```python
# module_details.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

class ModuleDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://example.com/module-details"

    def navigate(self):
        self.driver.get(self.url)

    def get_module_details(self):
        try:
            module_id_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='module-id']"))
            )
            module_name_element = self.driver.find_element(By.XPATH, "//div[@id='module-name']")
            module_description_element = self.driver.find_element(By.XPATH, "//div[@id='module-description']")
            group_id_element = self.driver.find_element(By.XPATH, "//div[@id='group-id']")
            creation_date_element = self.driver.find_element(By.XPATH, "//div[@id='creation-date']")

            module_id = module_id_element.text
            module_name = module_name_element.text
            module_description = module_description_element.text
            group_id = group_id_element.text
            creation_date = creation_date_element.text

            return {
                "id": module_id,
                "name": module_name,
                "description": module_description,
                "group_id": group_id,
                "creation_date": creation_date
            }
        except TimeoutException:
            print("Timed out waiting for module details to load")
            return None

    def create_new_group(self):
        # Implement logic to create a new group
        pass

    def select_existing_group(self):
        # Implement logic to select an existing group
        pass

# Usage

driver = webdriver.Chrome()
module_details_page = ModuleDetailsPage(driver)
module_details_page.navigate()

module_details = module_details_page.get_module_details()
if module_details:
    print("Module ID:", module_details["id"])
    print("Module Name:", module_details["name"])
    print("Module Description:", module_details["description"])
    print("Group ID:", module_details["group_id"])
    print("Creation Date:", module_details["creation_date"])

driver.quit()
```

Note: Replace the XPATH values in the Selenium script with the actual XPATH values of the elements on your webpage. Also, implement the logic to create a new group and select an existing group in the `create_new_group` and `select_existing_group` methods respectively.