Here's a PHP code based on the provided data. This code defines a `Module` class and creates an instance of it:

```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $sortOrder;
    private $createdAt;
    private $updatedAt;
    private $deletedAt;
    private $createdBy;
    private $updatedBy;

    public function __construct($id, $name, $description, $sortOrder, $createdAt, $updatedAt, $deletedAt, $createdBy, $updatedBy) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sortOrder = $sortOrder;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
        $this->deletedAt = $deletedAt;
        $this->createdBy = $createdBy;
        $this->updatedBy = $updatedBy;
    }

    public function __toString() {
        return "Module " . $this->id . ": " . $this->name . "\nDescription: " . $this->description . "\nSort Order: " . $this->sortOrder;
    }

    // Getters
    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getSortOrder() {
        return $this->sortOrder;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }

    public function getUpdatedAt() {
        return $this->updatedAt;
    }

    public function getDeletedAt() {
        return $this->deletedAt;
    }

    public function getCreatedBy() {
        return $this->createdBy;
    }

    public function getUpdatedBy() {
        return $this->updatedBy;
    }
}

$modules = [
    new Module(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, '2025-02-05 09:17:38', null, null, null, null)
];

foreach ($modules as $module) {
    echo $module . "\n";
}
```

Please note that `datetime` object is not required in this context because PHP can handle date string well. In case you want to specifically work with date, consider using PHP's DateTime class for more flexibility. Also, for simplicity, the deletedAt, createdBy, and updatedBy fields are set to null. You would replace these with your own values or implement a system to track this information. 

When run, this will display the details of each module. If you need further modifications, let me know!