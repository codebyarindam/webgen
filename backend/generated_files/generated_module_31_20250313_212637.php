```php
<?php

// Define a class to represent a module
class Module {
    private $id;
    private $name;
    private $description;
    private $order;
    private $moduleId;
    private $parentId;
    private $moduleIdRef;
    private $createdDate;

    // Constructor to initialize the module
    public function __construct($id, $name, $description, $order, $moduleId, $parentId, $moduleIdRef, $createdDate) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->moduleId = $moduleId;
        $this->parentId = $parentId;
        $this->moduleIdRef = $moduleIdRef;
        $this->createdDate = $createdDate;
    }

    // Getters to access module properties
    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getOrder() {
        return $this->order;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getModuleIdRef() {
        return $this->moduleIdRef;
    }

    public function getCreatedDate() {
        return $this->createdDate;
    }
}

// Create a module based on the provided data
$moduleData = array(
    'id' => 31,
    'name' => 'Index Page',
    'description' => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    'order' => 1,
    'moduleId' => null,
    'parentId' => null,
    'moduleIdRef' => null,
    'createdDate' => DateTime::createFromFormat('Y-m-d H:i:s', '2025-02-05 09:17:38')
);

$module = new Module(
    $moduleData['id'],
    $moduleData['name'],
    $moduleData['description'],
    $moduleData['order'],
    $moduleData['moduleId'],
    $moduleData['parentId'],
    $moduleData['moduleIdRef'],
    $moduleData['createdDate']
);

// Example usage
print($module->getId() . "\n");
print($module->getName() . "\n");
print($module->getDescription() . "\n");
print($module->getOrder() . "\n");
print($module->getCreatedDate()->format('Y-m-d H:i:s') . "\n");

?>
```