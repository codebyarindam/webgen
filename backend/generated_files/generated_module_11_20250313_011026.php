```php
<?php

class Module {
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

$modules = array(
    array(11, 'PATIENT_MANAGEMENT_MODULE', 'A module to manage patient information and records.', 2, '2022-01-11 12:00:00')
);

foreach ($modules as $module) {
    if ($module[0] == 11) {
        $moduleObject = new Module($module[0], $module[1], $module[2], $module[3], $module[4]);
        echo "Module ID: " . $moduleObject->getModuleId() . "\n";
        echo "Module Name: " . $moduleObject->getModuleName() . "\n";
        echo "Module Description: " . $moduleObject->getModuleDescription() . "\n";
        echo "Module ID Order: " . $moduleObject->getModuleIdOrder() . "\n";
        echo "Created At: " . $moduleObject->getCreatedAt() . "\n";
    }
}
?>
```

In this code:

- A `Module` class is created to encapsulate the properties of a module.
- An array of modules is defined, where each module is an array containing its properties.
- The code then loops through the array of modules and creates a `Module` object for the module with ID 11.
- Finally, the properties of the module with ID 11 are printed to the console.

Note: The `datetime` object is not available in PHP, so we use a string to represent the date and time instead. If you need to work with dates and times in PHP, consider using the `DateTime` class.