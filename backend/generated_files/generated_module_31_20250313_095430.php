```php
<?php

// Define a class to represent the module details
class Module {
    public $id;
    public $name;
    public $description;
    public $order;
    public $created_at;

    public function __construct($id, $name, $description, $order, $created_at) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->created_at = $created_at;
    }
}

// Define the data
$data = array(
    'id' => 31,
    'name' => 'Index Page',
    'description' => 'Display a list of existing groups.' . "\r\n" . 'Provide options to:' . "\r\n" . 'Create a new group.' . "\r\n" . 'Select an existing group to view/edit contacts.',
    'order' => 1,
    'created_at' => '2025-02-05 09:17:38'
);

// Create an instance of the Module class
$module = new Module($data['id'], $data['name'], $data['description'], $data['order'], $data['created_at']);

// Print the module details
echo "Module ID: " . $module->id . "\n";
echo "Module Name: " . $module->name . "\n";
echo "Module Description: " . $module->description . "\n";
echo "Module Order: " . $module->order . "\n";
echo "Module Created At: " . $module->created_at . "\n";

?>
```