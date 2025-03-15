```php
<?php

class Module {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleOrder;
    private $createdAt;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleOrder, $createdAt) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleOrder = $moduleOrder;
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

    public function getModuleOrder() {
        return $this->moduleOrder;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

// Example usage
$moduleId = 31;
$moduleName = 'Index Page';
$moduleDescription = 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.';
$moduleOrder = 1;
$createdAt = new DateTime('2025-02-05 09:17:38');

$module = new Module($moduleId, $moduleName, $moduleDescription, $moduleOrder, $createdAt);

print($module->getModuleId() . "\n");
print($module->getModuleName() . "\n");
print($module->getModuleDescription() . "\n");
print($module->getModuleOrder() . "\n");
print($module->getCreatedAt()->format('Y-m-d H:i:s') . "\n");

// Output:
// 31
// Index Page
// Display a list of existing groups.
// Provide options to:
// Create a new group.
// Select an existing group to view/edit contacts.
// 1
// 2025-02-05 09:17:38
```

In the provided PHP code:

*   A `Module` class is defined with private properties for module ID, name, description, order, and creation date.
*   A constructor (`__construct`) is used to initialize these properties when creating a new `Module` object.
*   Getter methods are provided to access the values of these properties.
*   An example usage is shown where a new `Module` object is created using the given data and its properties are printed to demonstrate the class functionality.