```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $order;
    private $createdAt;
    private $updatedAt;

    public function __construct($id, $name, $description, $order, $createdAt = null, $updatedAt = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
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

    public function getOrder() {
        return $this->order;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }

    public function getUpdatedAt() {
        return $this->updatedAt;
    }
}

$data = [
    [31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, '2025-02-05 09:17:38']
];

$modules = [];

foreach ($data as $moduleData) {
    $moduleId = $moduleData[0];
    $moduleName = $moduleData[1];
    $moduleDescription = $moduleData[2];
    $moduleOrder = $moduleData[3];
    $moduleCreatedAt = DateTime::createFromFormat('Y-m-d H:i:s', $moduleData[7]);

    $module = new Module($moduleId, $moduleName, $moduleDescription, $moduleOrder, $moduleCreatedAt);
    $modules[] = $module;
}

foreach ($modules as $module) {
    echo "Module ID: " . $module->getId() . "\n";
    echo "Module Name: " . $module->getName() . "\n";
    echo "Module Description: " . $module->getDescription() . "\n";
    echo "Module Order: " . $module->getOrder() . "\n";
    echo "Module Created At: " . $module->getCreatedAt()->format('Y-m-d H:i:s') . "\n";
}
?>
```