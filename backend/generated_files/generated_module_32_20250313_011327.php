Here's a PHP code that meets the specifications:

```php
<?php

interface ModuleInterface {
    public function getId();
    public function getName();
    public function getDescription();
    public function getIsActive();
    public function getCreatedAt();
}

class GroupPageModule implements ModuleInterface {
    private $id;
    private $name;
    private $description;
    private $isActive;
    private $createdAt;

    public function __construct($id, $name, $description, $isActive, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->isActive = $isActive;
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

    public function getIsActive() {
        return $this->isActive;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }

    public function display() {
        echo "Group Page: " . $this->name . "\n";
        echo $this->description . "\n";
        echo "Is Active: " . ($this->isActive ? 'Yes' : 'No') . "\n";
        echo "Created At: " . $this->createdAt->format('Y-m-d H:i:s') . "\n";
    }
}

$groupPageModule = new GroupPageModule(
    32,
    'Group Page',
    'Display the name of the selected group.
Allow users to:
Add a new contact.
Edit existing contacts.
Delete existing contacts.
Search for contacts within the group.',
    1,
    new DateTime('2025-02-05 09:18:22')
);

$groupPageModule->display();

?>
```

### How the Code Works

*   We define an interface `ModuleInterface` with methods `getId()`, `getName()`, `getDescription()`, `getIsActive()`, and `getCreatedAt()`.
*   We create a class `GroupPageModule` that implements `ModuleInterface` and has a constructor to initialize its properties.
*   The `display()` method in the `GroupPageModule` class prints out the module's details.
*   We create an instance of `GroupPageModule` with the provided data and call its `display()` method to print the details.

### Note

*   The `DateTime` class in PHP is used to represent dates and times. The `format()` method is used to format the date and time as a string.
*   The `__construct()` method in PHP is a special method that is automatically called when an object of a class is created.