```php
<?php

class ModuleDetails {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleIdParent;
    private $moduleDisplayOrder;
    private $moduleCreatedDate;
    private $moduleModifiedDate;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleIdParent = null, $moduleDisplayOrder = null, $moduleCreatedDate = null, $moduleModifiedDate = null) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleIdParent = $moduleIdParent;
        $this->moduleDisplayOrder = $moduleDisplayOrder;
        $this->moduleCreatedDate = $moduleCreatedDate;
        $this->moduleModifiedDate = $moduleModifiedDate;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getModuleName() {
        return $this->moduleName;
    }

    public function getModuleDescription() {
        return $this->moduleDescription;
    }

    public function getModuleIdParent() {
        return $this->moduleIdParent;
    }

    public function getModuleDisplayOrder() {
        return $this->moduleDisplayOrder;
    }

    public function getModuleCreatedDate() {
        return $this->moduleCreatedDate;
    }

    public function getModuleModifiedDate() {
        return $this->moduleModifiedDate;
    }
}

$moduleDetails = new ModuleDetails(
    31,
    'Index Page',
    'Display a list of existing groups.' . "\r\n" . 'Provide options to:' . "\r\n" . 'Create a new group.' . "\r\n" . 'Select an existing group to view/edit contacts.',
    null,
    1,
    null,
    new DateTime('2025-02-05 09:17:38')
);

print_r($moduleDetails);

?>
```