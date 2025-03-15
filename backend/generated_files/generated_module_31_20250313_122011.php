Based on the provided data, here is a PHP code that represents the module details:

```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $position;
    private $parentId;
    private $createdAt;

    public function __construct($id, $name, $description, $position, $parentId = null, $createdAt = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->position = $position;
        $this->parentId = $parentId;
        $this->createdAt = $createdAt;
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

    public function getPosition() {
        return $this->position;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

$moduleDetails = new Module(
    31,
    'Index Page',
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    1,
    null,
    new DateTime('2025-02-05 09:17:38')
);

print_r($moduleDetails);

echo "Module ID: " . $moduleDetails->getId() . "\n";
echo "Module Name: " . $moduleDetails->getName() . "\n";
echo "Module Description: " . $moduleDetails->getDescription() . "\n";
echo "Module Position: " . $moduleDetails->getPosition() . "\n";
echo "Module Parent ID: " . $moduleDetails->getParentId() . "\n";
echo "Module Created At: " . $moduleDetails->getCreatedAt()->format('Y-m-d H:i:s') . "\n";

?>
```

This code defines a `Module` class with properties for `id`, `name`, `description`, `position`, `parentId`, and `createdAt`. It then creates a new instance of the `Module` class using the provided data and prints out the module details.

Note: The `DateTime` class is used to represent the `createdAt` date and time. The `format` method is used to format the date and time as a string.