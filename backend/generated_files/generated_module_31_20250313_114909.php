```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $parentId;
    private $createdAt;
    private $updatedAt;

    public function __construct($id, $name, $description, $parentId, $createdAt = null, $updatedAt = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->parentId = $parentId;
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

    public function getParentId() {
        return $this->parentId;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }

    public function getUpdatedAt() {
        return $this->updatedAt;
    }
}

$moduleData = array(
    31,
    'Index Page',
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    1,
    null,
    null,
    new DateTime('2025-02-05 09:17:38')
);

$module = new Module(
    $moduleData[0],
    $moduleData[1],
    $moduleData[2],
    $moduleData[3],
    $moduleData[5],
    $moduleData[6]
);

print_r($module);

?>
```