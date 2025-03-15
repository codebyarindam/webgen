```php
<?php

class Module {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleOrder;
    private $moduleCreatedAt;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleOrder, $moduleCreatedAt) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleOrder = $moduleOrder;
        $this->moduleCreatedAt = $moduleCreatedAt;
    }

    public function __toString() {
        return "Module ID: $this->moduleId\nModule Name: $this->moduleName\nModule Description: $this->moduleDescription\nModule Order: $this->moduleOrder\nModule Created At: $this->moduleCreatedAt";
    }
}

$moduleId = 31;
$moduleName = 'Index Page';
$moduleDescription = 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.';
$moduleOrder = 1;
$moduleCreatedAt = new DateTime('2025-02-05 09:17:38');

$module = new Module($moduleId, $moduleName, $moduleDescription, $moduleOrder, $moduleCreatedAt);
print($module);

?>
```