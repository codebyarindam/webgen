**PHP Module Details Generation**
=====================================

Below is a PHP code that represents the given module details:

```php
<?php

class ModuleDetails {
    private $id;
    private $moduleName;
    private $moduleDescription;
    private $moduleId;
    private $created_at;

    public function __construct($id, $moduleName, $moduleDescription, $moduleId, $created_at) {
        $this->id = $id;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleId = $moduleId;
        $this->created_at = $created_at;
    }

    public function getModuleDetails() {
        return [
            'id' => $this->id,
            'module_name' => $this->moduleName,
            'module_description' => $this->moduleDescription,
            'module_id' => $this->moduleId,
            'created_at' => $this->created_at,
        ];
    }
}

$moduleData = [
    'id' => 31,
    'module_name' => 'Index Page',
    'module_description' => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    'module_id' => 1,
    'created_at' => '2025-02-05 09:17:38',
];

$moduleDetails = new ModuleDetails(
    $moduleData['id'],
    $moduleData['module_name'],
    $moduleData['module_description'],
    $moduleData['module_id'],
    $moduleData['created_at']
);

print_r($moduleDetails->getModuleDetails());

?>
```

**Explanation:**

*   We define a `ModuleDetails` class with private properties for `id`, `moduleName`, `moduleDescription`, `moduleId`, and `created_at`.
*   The class has a constructor method that initializes these properties.
*   The `getModuleDetails` method returns an array containing the module details.
*   We create an instance of the `ModuleDetails` class with the provided data and print the module details using the `getModuleDetails` method.

**Example Output:**

```php
Array
(
    [id] => 31
    [module_name] => Index Page
    [module_description] => Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.
    [module_id] => 1
    [created_at] => 2025-02-05 09:17:38
)
```