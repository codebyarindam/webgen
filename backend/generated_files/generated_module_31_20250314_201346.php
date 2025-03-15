```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $parentId;
    private $moduleId;
    private $otherId;
    private $otherParam;
    private $createdAt;

    public function __construct($id, $name, $description, $parentId, $moduleId, $otherId, $otherParam, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->parentId = $parentId;
        $this->moduleId = $moduleId;
        $this->otherId = $otherId;
        $this->otherParam = $otherParam;
        $this->createdAt = $createdAt;
    }

    public function getDetails() {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'description' => $this->description,
            'parent_id' => $this->parentId,
            'module_id' => $this->moduleId,
            'other_id' => $this->otherId,
            'other_param' => $this->otherParam,
            'created_at' => $this->createdAt
        ];
    }
}

$moduleData = [
    'id' => 31,
    'name' => 'Index Page',
    'description' => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.',
    'parent_id' => 1,
    'module_id' => null,
    'other_id' => null,
    'other_param' => null,
    'created_at' => new DateTime('2025-02-05 09:17:38')
];

$module = new Module(
    $moduleData['id'],
    $moduleData['name'],
    $moduleData['description'],
    $moduleData['parent_id'],
    $moduleData['module_id'],
    $moduleData['other_id'],
    $moduleData['other_param'],
    $moduleData['created_at']
);

print_r($module->getDetails());

?>
```