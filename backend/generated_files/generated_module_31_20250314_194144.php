Here's an example PHP code based on the given data:

```php
<?php

// Define a class for the module
class Module {
    private $id;
    private $name;
    private $description;
    private $order;
    private $groupId;
    private $moduleId;
    private $parentId;
    private $created;

    // Constructor to initialize module details
    public function __construct($id, $name, $description, $order, $groupId, $moduleId, $parentId, $created) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->groupId = $groupId;
        $this->moduleId = $moduleId;
        $this->parentId = $parentId;
        $this->created = $created;
    }

    // Getters for module details
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

    public function getGroupId() {
        return $this->groupId;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getCreated() {
        return $this->created;
    }
}

// Define the module details
$moduleDetails = [
    [
        'id' => 31,
        'name' => 'Index Page',
        'description' => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
        'order' => 1,
        'groupId' => null,
        'moduleId' => null,
        'parentId' => null,
        'created' => '2025-02-05 09:17:38'
    ]
];

// Create a module object
$module = new Module($moduleDetails[0]['id'], $moduleDetails[0]['name'], $moduleDetails[0]['description'], 
                      $moduleDetails[0]['order'], $moduleDetails[0]['groupId'], $moduleDetails[0]['moduleId'], 
                      $moduleDetails[0]['parentId'], $moduleDetails[0]['created']);

// Display module details
echo "ID: " . $module->getId() . "\n";
echo "Name: " . $module->getName() . "\n";
echo "Description: " . $module->getDescription() . "\n";
echo "Order: " . $module->getOrder() . "\n";
echo "Group ID: " . ($module->getGroupId() !== null ? $module->getGroupId() : 'None') . "\n";
echo "Module ID: " . ($module->getModuleId() !== null ? $module->getModuleId() : 'None') . "\n";
echo "Parent ID: " . ($module->getParentId() !== null ? $module->getParentId() : 'None') . "\n";
echo "Created: " . $module->getCreated() . "\n";

?>
```

**How it works:**

1. We define a `Module` class to represent the module details.
2. The class has private properties for `id`, `name`, `description`, `order`, `groupId`, `moduleId`, `parentId`, and `created`.
3. The constructor initializes these properties when creating a new `Module` object.
4. We define getter methods to access these properties.
5. We define an array `$moduleDetails` containing the module details.
6. We create a new `Module` object using the details from the array.
7. We display the module details using the getter methods.

Note that in the `created` property, I used a string in the format `'YYYY-MM-DD HH:MM:SS'` instead of a `datetime` object, as PHP does not have a direct equivalent of Python's `datetime` object. If you need to work with dates and times, consider using PHP's `DateTime` class.