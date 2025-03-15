```php
<?php

// Define a class for the module details
class ModuleDetails {
    public $id;
    public $name;
    public $description;
    public $status;
    public $created_at;
    public $updated_at;
    public $deleted_at;
    public $created_by;
    public $updated_by;

    function __construct($id, $name, $description, $status, $created_at, $updated_at, $deleted_at, $created_by, $updated_by) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->status = $status;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
        $this->deleted_at = $deleted_at;
        $this->created_by = $created_by;
        $this->updated_by = $updated_by;
    }
}

// Given data
$data = array(
    array(
        32,
        'Group Page',
        'Display the name of the selected group.
Allow users to:
Add a new contact.
Edit existing contacts.
Delete existing contacts.
Search for contacts within the group.',
        1,
        null,
        null,
        null,
        null,
        new DateTime('2025-02-05 09:18:22')
    )
);

// Create an array to store module details
$modules = array();

// Populate the modules array
foreach ($data as $module_data) {
    $module = new ModuleDetails(
        $module_data[0],
        $module_data[1],
        $module_data[2],
        $module_data[3],
        $module_data[4],
        $module_data[5],
        $module_data[6],
        $module_data[7],
        $module_data[8]
    );
    array_push($modules, $module);
}

// Print the modules
foreach ($modules as $module) {
    print("ID: $module->id\n");
    print("Name: $module->name\n");
    print("Description: $module->description\n");
    print("Status: $module->status\n");
    print("Created At: " . $module->created_at->format('Y-m-d H:i:s') . "\n");
    print("Updated At: $module->updated_at\n");
    print("Deleted At: $module->deleted_at\n");
    print("Created By: $module->created_by\n");
    print("Updated By: $module->updated_by\n\n");
}

?>
```

This code defines a `ModuleDetails` class with properties for the given data. It then creates an array to store instances of this class and populates it with the given data. Finally, it prints out the details of each module.

**Note:** The `DateTime` class is used to represent the date and time in PHP. The `format` method is used to format the date and time as a string. 

In this code, I assume that `null` values are allowed for `created_at`, `updated_at`, `deleted_at`, `created_by`, and `updated_by`. If these values are not allowed to be `null`, you may need to adjust the code accordingly. 

Please ensure that you have the correct timezone set in your PHP environment to avoid any unexpected date and time issues.