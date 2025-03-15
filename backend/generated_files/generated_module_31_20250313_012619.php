Here's a PHP code based on the provided data:

```php
<?php

// Define a class to represent a module
class Module {
    private $id;
    private $name;
    private $description;
    private $position;
    private $parentId;
    private $controller;
    private $action;
    private $createdAt;

    // Constructor to initialize the module
    public function __construct($id, $name, $description, $position, $parentId, $controller, $action, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->position = $position;
        $this->parentId = $parentId;
        $this->controller = $controller;
        $this->action = $action;
        $this->createdAt = $createdAt;
    }

    // Getter methods to access module properties
    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getPosition() {
        return $this->position;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getController() {
        return $this->controller;
    }

    public function getAction() {
        return $this->action;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

// Create a module based on the provided data
$moduleData = array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, '2025-02-05 09:17:38');

// Convert the date string to a DateTime object
$createdAt = DateTime::createFromFormat('Y-m-d H:i:s', $moduleData[7]);

// Create a new module
$module = new Module($moduleData[0], $moduleData[1], $moduleData[2], $moduleData[3], $moduleData[4], $moduleData[5], $moduleData[6], $createdAt);

// Display the module details
echo "Id: " . $module->getId() . "\n";
echo "Name: " . $module->getName() . "\n";
echo "Description: " . $module->getDescription() . "\n";
echo "Position: " . $module->getPosition() . "\n";
echo "Parent Id: " . ($module->getParentId() !== null ? $module->getParentId() : 'None') . "\n";
echo "Controller: " . ($module->getController() !== null ? $module->getController() : 'None') . "\n";
echo "Action: " . ($module->getAction() !== null ? $module->getAction() : 'None') . "\n";
echo "Created At: " . $module->getCreatedAt()->format('Y-m-d H:i:s') . "\n";

?>
```

In this code:

*   We define a `Module` class with properties like `id`, `name`, `description`, `position`, `parentId`, `controller`, `action`, and `createdAt`.
*   We create a constructor to initialize these properties.
*   We provide getter methods to access these properties.
*   We create a new `Module` object based on the provided data and display its details.

This code provides a basic structure for representing and displaying module details using a `Module` class. You can modify it according to your specific requirements.