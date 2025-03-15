```php
<?php

// Define the module details class
class ModuleDetails {
    public $id;
    public $name;
    public $description;
    public $level;
    public $parent_id;
    public $created_at;

    // Constructor to initialize the object
    function __construct($id, $name, $description, $level, $parent_id = null, $created_at = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->level = $level;
        $this->parent_id = $parent_id;
        $this->created_at = $created_at;
    }
}

// Create a new module details object
$module_details = new ModuleDetails(
    31, 
    'Index Page', 
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 
    1, 
    null, 
    new DateTime('2025-02-05 09:17:38')
);

// Print the module details
echo "ID: $module_details->id\n";
echo "Name: $module_details->name\n";
echo "Description: $module_details->description\n";
echo "Level: $module_details->level\n";
echo "Parent ID: $module_details->parent_id\n";
echo "Created At: $module_details->created_at->format('Y-m-d H:i:s')\n";

?>
```