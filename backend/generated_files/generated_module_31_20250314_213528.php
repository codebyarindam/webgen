**Module Details PHP Code**
=====================================

Below is a PHP code snippet that defines a `Module` class with details populated from the provided data.

```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $sortOrder;
    private $createdDate;

    /**
     * Constructor to initialize module details.
     *
     * @param int $id Unique identifier for the module.
     * @param string $name Name of the module.
     * @param string $description Description of the module.
     * @param int $sortOrder Order in which the module should be sorted.
     * @param DateTime $createdDate Date when the module was created.
     */
    public function __construct($id, $name, $description, $sortOrder, $createdDate) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sortOrder = $sortOrder;
        $this->createdDate = $createdDate;
    }

    /**
     * Get the module id.
     *
     * @return int
     */
    public function getId() {
        return $this->id;
    }

    /**
     * Get the module name.
     *
     * @return string
     */
    public function getName() {
        return $this->name;
    }

    /**
     * Get the module description.
     *
     * @return string
     */
    public function getDescription() {
        return $this->description;
    }

    /**
     * Get the module sort order.
     *
     * @return int
     */
    public function getSortOrder() {
        return $this->sortOrder;
    }

    /**
     * Get the module created date.
     *
     * @return DateTime
     */
    public function getCreatedDate() {
        return $this->createdDate;
    }
}

// Example usage
$moduleData = array(
    31,
    'Index Page',
    'Display a list of existing groups.' . "\r\n" . 'Provide options to:' . "\r\n" . 'Create a new group.' . "\r\n" . 'Select an existing group to view/edit contacts.',
    1,
    new DateTime('2025-02-05 09:17:38')
);

$module = new Module($moduleData[0], $moduleData[1], $moduleData[2], $moduleData[3], $moduleData[4]);

echo "Module ID: " . $module->getId() . "\n";
echo "Module Name: " . $module->getName() . "\n";
echo "Module Description: " . $module->getDescription() . "\n";
echo "Module Sort Order: " . $module->getSortOrder() . "\n";
echo "Module Created Date: " . $module->getCreatedDate()->format('Y-m-d H:i:s') . "\n";

?>
```

**Explanation**
---------------

*   We define a `Module` class with properties for `id`, `name`, `description`, `sortOrder`, and `createdDate`.
*   The constructor initializes these properties when an instance of the class is created.
*   Getter methods (`getId`, `getName`, `getDescription`, `getSortOrder`, `getCreatedDate`) allow access to the module's details.
*   The example usage demonstrates how to create a new `Module` instance and access its details.