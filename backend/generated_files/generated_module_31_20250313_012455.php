```php
<?php

// Define the Module class
class Module {
    private $id;
    private $name;
    private $description;
    private $orderId;
    private $parentId;
    private $moduleId;
    private $moduleName;
    private $createdAt;

    // Constructor to initialize the properties
    public function __construct($id, $name, $description, $orderId, $parentId = null, $moduleId = null, $moduleName = null, $createdAt = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->orderId = $orderId;
        $this->parentId = $parentId;
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->createdAt = $createdAt;
    }

    // Method to display the module details
    public function displayModuleDetails() {
        echo "Module ID: $this->id\n";
        echo "Module Name: $this->name\n";
        echo "Module Description: $this->description\n";
        echo "Order ID: $this->orderId\n";
        echo "Parent ID: $this->parentId\n";
        echo "Module ID: $this->moduleId\n";
        echo "Module Name: $this->moduleName\n";
        echo "Created At: $this->createdAt\n";
    }
}

// Create a new module
$module = new Module(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, '2025-02-05 09:17:38');

// Display the module details
$module->displayModuleDetails();

?>
```