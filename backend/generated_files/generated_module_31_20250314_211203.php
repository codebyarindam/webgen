**PHP Code Generation**
=======================

Based on the provided data, I will create a PHP class that represents a module with the specified details.

**Module Class**
---------------

```php
class Module {
    private $id;
    private $name;
    private $description;
    private $priority;
    private $createdAt;

    public function __construct($id, $name, $description, $priority, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->priority = $priority;
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

    public function getPriority() {
        return $this->priority;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}
```

**Module Instance**
------------------

```php
$module = new Module(
    31,
    'Index Page',
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    1,
    new DateTime('2025-02-05 09:17:38')
);
```

**Example Usage**
-----------------

```php
echo "Module ID: " . $module->getId() . "\n";
echo "Module Name: " . $module->getName() . "\n";
echo "Module Description: " . $module->getDescription() . "\n";
echo "Module Priority: " . $module->getPriority() . "\n";
echo "Module Created At: " . $module->getCreatedAt()->format('Y-m-d H:i:s') . "\n";
```

This code defines a `Module` class with properties for `id`, `name`, `description`, `priority`, and `createdAt`. The `Module` class has a constructor that initializes these properties, and getter methods to access their values. The example usage demonstrates how to create a new `Module` instance and access its properties.