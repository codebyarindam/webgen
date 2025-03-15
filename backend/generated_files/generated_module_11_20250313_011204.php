```php
<?php

// Define the class Module
class Module {
    public $id;
    public $name;
    public $description;
    public $sequence;
    public $parent_id;
    public $created_at;
    public $updated_at;

    // Constructor to initialize the module
    function __construct($id, $name, $description, $sequence, $parent_id, $created_at, $updated_at) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sequence = $sequence;
        $this->parent_id = $parent_id;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
    }

    // Method to display the module details
    function display_details() {
        echo "Module ID: $this->id\n";
        echo "Module Name: $this->name\n";
        echo "Module Description: $this->description\n";
        echo "Module Sequence: $this->sequence\n";
        echo "Parent ID: $this->parent_id\n";
        echo "Created At: $this->created_at\n";
        echo "Updated At: $this->updated_at\n";
    }
}

// Create an instance of the Module class
$module = new Module(11, 'PATIENT_MANAGEMENT_MODULE', 'A module to manage patient information and records.', 2, null, '2022-01-11 12:00:00', null);

// Display the module details
$module->display_details();

?>
```