```php
<?php

// Define the module details class
class ModuleDetails {
    private $id;
    private $name;
    private $description;
    private $sequence;
    private $parentId;
    private $moduleId;
    private $moduleIdRef;
    private $createdAt;

    public function __construct($id, $name, $description, $sequence, $parentId, $moduleId, $moduleIdRef, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sequence = $sequence;
        $this->parentId = $parentId;
        $this->moduleId = $moduleId;
        $this->moduleIdRef = $moduleIdRef;
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

    public function getSequence() {
        return $this->sequence;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getModuleIdRef() {
        return $this->moduleIdRef;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

// Create a new module details instance
$moduleDetails = new ModuleDetails(
    31,
    'Index Page',
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    1,
    null,
    null,
    null,
    new DateTime('2025-02-05 09:17:38')
);

// Print the module details
print_r($moduleDetails);

// Access the module details properties
echo $moduleDetails->getId() . "\n";
echo $moduleDetails->getName() . "\n";
echo $moduleDetails->getDescription() . "\n";
echo $moduleDetails->getSequence() . "\n";
echo $moduleDetails->getParentId() . "\n";
echo $moduleDetails->getModuleId() . "\n";
echo $moduleDetails->getModuleIdRef() . "\n";
echo $moduleDetails->getCreatedAt()->format('Y-m-d H:i:s') . "\n";

?>
```