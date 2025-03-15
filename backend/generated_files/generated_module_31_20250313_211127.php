Here's a PHP code based on the provided data:

```php
<?php

// Define a class for the module
class Module {
    private $id;
    private $name;
    private $description;
    private $position;
    private $parentId;
    private $createTime;
    private $updateTime;
    private $deleteTime;

    // Constructor to initialize the object
    public function __construct($id, $name, $description, $position, $parentId, $createTime, $updateTime, $deleteTime) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->position = $position;
        $this->parentId = $parentId;
        $this->createTime = $createTime;
        $this->updateTime = $updateTime;
        $this->deleteTime = $deleteTime;
    }

    // Getters to retrieve module details
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

    public function getCreateTime() {
        return $this->createTime;
    }

    public function getUpdateTime() {
        return $this->updateTime;
    }

    public function getDeleteTime() {
        return $this->deleteTime;
    }
}

// Create a module object
$module = new Module(
    31, 
    'Index Page', 
    'Display a list of existing groups.
    Provide options to:
    Create a new group.
    Select an existing group to view/edit contacts.', 
    1, 
    null, 
    null, 
    new DateTime('2025-02-05 09:17:38'), 
    null
);

// Print module details
echo "Module ID: " . $module->getId() . "\n";
echo "Module Name: " . $module->getName() . "\n";
echo "Module Description: " . $module->getDescription() . "\n";
echo "Module Position: " . $module->getPosition() . "\n";
echo "Module Parent ID: " . $module->getParentId() . "\n";
echo "Module Create Time: " . $module->getCreateTime()->format('Y-m-d H:i:s') . "\n";
echo "Module Update Time: " . $module->getUpdateTime() . "\n";
echo "Module Delete Time: " . $module->getDeleteTime() . "\n";

?>
```

This PHP code defines a `Module` class to represent the module details. It includes a constructor to initialize the object and getter methods to retrieve the module details. Then, it creates a `Module` object based on the provided data and prints the module details.

**Example Output:**

```
Module ID: 31
Module Name: Index Page
Module Description: Display a list of existing groups.
    Provide options to:
    Create a new group.
    Select an existing group to view/edit contacts.
Module Position: 1
Module Parent ID: 
Module Create Time: 2025-02-05 09:17:38
Module Update Time: 
Module Delete Time:
```

Please note that this code uses the `DateTime` class to handle dates and times. The `DateTime` class is part of the PHP Standard Library and provides a convenient way to work with dates and times in PHP.