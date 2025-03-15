```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $displayOrder;
    private $moduleId;
    private $iconClass;
    private $link;
    private $createdAt;

    public function __construct($id, $name, $description, $displayOrder, $moduleId, $iconClass, $link, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->displayOrder = $displayOrder;
        $this->moduleId = $moduleId;
        $this->iconClass = $iconClass;
        $this->link = $link;
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

    public function getDisplayOrder() {
        return $this->displayOrder;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getIconClass() {
        return $this->iconClass;
    }

    public function getLink() {
        return $this->link;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

$moduleData = array(
    array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, '2025-02-05 09:17:38')
);

$modules = array();

foreach ($moduleData as $module) {
    $moduleId = $module[0];
    $name = $module[1];
    $description = $module[2];
    $displayOrder = $module[3];
    $moduleIdValue = $module[4];
    $iconClass = $module[5];
    $link = $module[6];
    $createdAt = DateTime::createFromFormat('Y-m-d H:i:s', $module[7]);

    $newModule = new Module($moduleId, $name, $description, $displayOrder, $moduleIdValue, $iconClass, $link, $createdAt);
    $modules[] = $newModule;
}

foreach ($modules as $module) {
    echo "ID: " . $module->getId() . "\n";
    echo "Name: " . $module->getName() . "\n";
    echo "Description: " . $module->getDescription() . "\n";
    echo "Display Order: " . $module->getDisplayOrder() . "\n";
    echo "Module ID: " . $module->getModuleId() . "\n";
    echo "Icon Class: " . $module->getIconClass() . "\n";
    echo "Link: " . $module->getLink() . "\n";
    echo "Created At: " . $module->getCreatedAt()->format('Y-m-d H:i:s') . "\n";
}
```

### Explanation

This PHP code defines a `Module` class with properties for `id`, `name`, `description`, `displayOrder`, `moduleId`, `iconClass`, `link`, and `createdAt`. The class includes getter methods for each property.

The code then creates an array of module data, where each element represents a module with its corresponding properties.

It then iterates over the module data array, creates a new `Module` object for each element, and adds it to the `$modules` array.

Finally, it iterates over the `$modules` array and prints out the properties of each module using the getter methods.

### Example Use Case

This code can be used to manage and display modules in a web application. For example, you can use the `Module` class to create modules with different properties, such as name, description, and display order, and then display them in a list or grid layout.

To add a new module, you can simply create a new `Module` object and add it to the `$modules` array. To remove a module, you can remove the corresponding element from the `$modules` array.

You can also use the getter methods to access the properties of a module and display them in a template or view.

### Step-by-Step Solution

1. Define the `Module` class with its properties and getter methods.
2. Create an array of module data, where each element represents a module with its corresponding properties.
3. Iterate over the module data array and create a new `Module` object for each element.
4. Add each `Module` object to the `$modules` array.
5. Iterate over the `$modules` array and print out the properties of each module using the getter methods.

### Advice

* Use a consistent naming convention for your variables and properties.
* Use getter and setter methods to encapsulate access to your properties.
* Use arrays or collections to store and manage multiple objects of the same type.
* Use iteration and loops to process and display data in a flexible and efficient way.