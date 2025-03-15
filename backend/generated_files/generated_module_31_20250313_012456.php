```php
<?php

// Class ModuleDetails
class ModuleDetails {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $isActive;
    private $createdAt;
    private $updatedAt;

    // Constructor
    function __construct($moduleId, $moduleName, $moduleDescription, $isActive, $createdAt = null, $updatedAt = null) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->isActive = $isActive;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
    }

    // Getters and Setters
    function getModuleId() {
        return $this->moduleId;
    }

    function setModuleId($moduleId) {
        $this->moduleId = $moduleId;
    }

    function getModuleName() {
        return $this->moduleName;
    }

    function setModuleName($moduleName) {
        $this->moduleName = $moduleName;
    }

    function getModuleDescription() {
        return $this->moduleDescription;
    }

    function setModuleDescription($moduleDescription) {
        $this->moduleDescription = $moduleDescription;
    }

    function getIsActive() {
        return $this->isActive;
    }

    function setIsActive($isActive) {
        $this->isActive = $isActive;
    }

    function getCreatedAt() {
        return $this->createdAt;
    }

    function setCreatedAt($createdAt) {
        $this->createdAt = $createdAt;
    }

    function getUpdatedAt() {
        return $this->updatedAt;
    }

    function setUpdatedAt($updatedAt) {
        $this->updatedAt = $updatedAt;
    }
}

// Create ModuleDetails object
$moduleId = 31;
$moduleName = 'Index Page';
$moduleDescription = 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.';
$isActive = 1;
$createdAt = '2025-02-05 09:17:38';
$updatedAt = null;

$moduleDetails = new ModuleDetails($moduleId, $moduleName, $moduleDescription, $isActive, $createdAt, $updatedAt);

// Display ModuleDetails
echo "Module ID: " . $moduleDetails->getModuleId() . "\n";
echo "Module Name: " . $moduleDetails->getModuleName() . "\n";
echo "Module Description: " . $moduleDetails->getModuleDescription() . "\n";
echo "Is Active: " . $moduleDetails->getIsActive() . "\n";
echo "Created At: " . $moduleDetails->getCreatedAt() . "\n";
echo "Updated At: " . ($moduleDetails->getUpdatedAt() ?? 'None') . "\n";

?>
```