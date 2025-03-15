```php
<?php

// Define a Module class
class Module {
    private $id;
    private $name;
    private $description;
    private $status;
    private $created_at;

    public function __construct($id, $name, $description, $status, $created_at) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->status = $status;
        $this->created_at = $created_at;
    }

    public function get_id() {
        return $this->id;
    }

    public function get_name() {
        return $this->name;
    }

    public function get_description() {
        return $this->description;
    }

    public function get_status() {
        return $this->status;
    }

    public function get_created_at() {
        return $this->created_at;
    }
}

// Create a Module object from the given data
$module_data = array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, null, '2025-02-05 09:17:38');
$module = new Module($module_data[0], $module_data[1], $module_data[2], $module_data[3], DateTime::createFromFormat('Y-m-d H:i:s', $module_data[8]));

// Print the module details
echo "Module ID: " . $module->get_id() . "\n";
echo "Module Name: " . $module->get_name() . "\n";
echo "Module Description: " . $module->get_description() . "\n";
echo "Module Status: " . $module->get_status() . "\n";
echo "Module Created At: " . $module->get_created_at()->format('Y-m-d H:i:s') . "\n";

?>
```