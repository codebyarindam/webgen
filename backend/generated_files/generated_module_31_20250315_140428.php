```php
<?php

// Define a class to hold the module details
class Module {
    public $id;
    public $name;
    public $description;
    public $order;
    public $parentId;
    public $moduleId;
    public $moduleId2;
    public $moduleId3;
    public $createdDate;

    // Constructor to initialize the module details
    function __construct($id, $name, $description, $order, $parentId, $moduleId, $moduleId2, $moduleId3, $createdDate) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->parentId = $parentId;
        $this->moduleId = $moduleId;
        $this->moduleId2 = $moduleId2;
        $this->moduleId3 = $moduleId3;
        $this->createdDate = $createdDate;
    }
}

// Function to generate PHP code based on the provided data
function generate_php_code($data) {
    // Initialize an empty array to store the module objects
    $modules = array();

    // Loop through the provided data and create module objects
    foreach ($data as $item) {
        $module = new Module(
            $item[0],
            $item[1],
            $item[2],
            $item[3],
            $item[4],
            $item[5],
            $item[6],
            $item[7],
            $item[8]
        );
        array_push($modules, $module);
    }

    // Print the generated PHP code
    foreach ($modules as $module) {
        echo "Module ID: $module->id\n";
        echo "Name: $module->name\n";
        echo "Description: $module->description\n";
        echo "Order: $module->order\n";
        echo "Parent ID: $module->parentId\n";
        echo "Module ID: $module->moduleId\n";
        echo "Module ID 2: $module->moduleId2\n";
        echo "Module ID 3: $module->moduleId3\n";
        echo "Created Date: $module->createdDate\n\n";
    }
}

// Example usage
$data = array(
    array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, NULL, NULL, NULL, NULL, '2025-02-05 09:17:38')
);

generate_php_code($data);

?>
```

**Output:**
```
Module ID: 31
Name: Index Page
Description: Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.
Order: 1
Parent ID: 
Module ID: 
Module ID 2: 
Module ID 3: 
Created Date: 2025-02-05 09:17:38
```

In this code:

1.  We define a `Module` class to hold the module details.
2.  The `generate_php_code` function takes the provided data, creates `Module` objects, and prints the generated PHP code.
3.  We demonstrate the usage of the `generate_php_code` function with an example array of module data.
4.  The output displays the module details in a formatted manner.