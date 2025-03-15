```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $order;
    private $created_at;

    public function __construct($id, $name, $description, $order, $created_at) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->order = $order;
        $this->created_at = $created_at;
    }

    public function __toString() {
        return "Module " . $this->id . ": " . $this->name . "\nDescription: " . $this->description . "\nOrder: " . $this->order . "\nCreated at: " . $this->created_at;
    }
}

$module_data = array(
    array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, DateTime::createFromFormat('Y-m-d H:i:s', '2025-02-05 09:17:38'))
);

$modules = array();

foreach ($module_data as $data) {
    $module = new Module($data[0], $data[1], $data[2], $data[3], $data[4]);
    $modules[] = $module;
}

foreach ($modules as $module) {
    echo $module . "\n";
}

?>
```