```php
<?php

class Module {
    public $id;
    public $name;
    public $description;
    public $sort_order;
    public $created_at;
    public $updated_at;

    function __construct($id, $name, $description, $sort_order, $created_at = null, $updated_at = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sort_order = $sort_order;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
    }

    function __toString() {
        return "Module $this->id: $this->name";
    }
}

$module_data = array(
    array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, new DateTime('2025-02-05 09:17:38'))
);

$modules = array();

foreach ($module_data as $data) {
    $module = new Module(
        $data[0],
        $data[1],
        $data[2],
        $data[3],
        $data[4]
    );

    $modules[] = $module;
}

foreach ($modules as $module) {
    echo $module->id . "\n";
    echo $module->name . "\n";
    echo $module->description . "\n";
    echo $module->sort_order . "\n";
    echo $module->created_at->format('Y-m-d H:i:s') . "\n";
    echo $module->updated_at . "\n";
}

?>
```