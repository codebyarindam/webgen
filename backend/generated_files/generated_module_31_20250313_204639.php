```php
<?php

// Define the data
$data = array(
    array(
        "id" => 31,
        "name" => "Index Page",
        "description" => "Display a list of existing groups.\r\nProvide options to:\r\nCreate a new group.\r\nSelect an existing group to view/edit contacts.",
        "sequence" => 1,
        "created_at" => null,
        "updated_at" => null,
        "deleted_at" => null,
        "created_by" => null,
        "updated_by" => null,
        "deleted_by" => null,
        "created_date" => new DateTime("2025-02-05 09:17:38")
    )
);

// Define a class to hold the data
class Module {
    public $id;
    public $name;
    public $description;
    public $sequence;
    public $created_at;
    public $updated_at;
    public $deleted_at;
    public $created_by;
    public $updated_by;
    public $deleted_by;
    public $created_date;

    function __construct($id, $name, $description, $sequence, $created_at, $updated_at, $deleted_at, $created_by, $updated_by, $deleted_by, $created_date) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sequence = $sequence;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
        $this->deleted_at = $deleted_at;
        $this->created_by = $created_by;
        $this->updated_by = $updated_by;
        $this->deleted_by = $deleted_by;
        $this->created_date = $created_date;
    }
}

// Create an instance of the Module class
$module = new Module(
    $data[0]["id"],
    $data[0]["name"],
    $data[0]["description"],
    $data[0]["sequence"],
    $data[0]["created_at"],
    $data[0]["updated_at"],
    $data[0]["deleted_at"],
    $data[0]["created_by"],
    $data[0]["updated_by"],
    $data[0]["deleted_by"],
    $data[0]["created_date"]
);

// Print the module details
echo "Module ID: " . $module->id . "\n";
echo "Module Name: " . $module->name . "\n";
echo "Module Description: " . $module->description . "\n";
echo "Module Sequence: " . $module->sequence . "\n";
echo "Module Created At: " . ($module->created_at === null ? "None" : $module->created_at->format("Y-m-d H:i:s")) . "\n";
echo "Module Updated At: " . ($module->updated_at === null ? "None" : $module->updated_at->format("Y-m-d H:i:s")) . "\n";
echo "Module Deleted At: " . ($module->deleted_at === null ? "None" : $module->deleted_at->format("Y-m-d H:i:s")) . "\n";
echo "Module Created By: " . ($module->created_by === null ? "None" : $module->created_by) . "\n";
echo "Module Updated By: " . ($module->updated_by === null ? "None" : $module->updated_by) . "\n";
echo "Module Deleted By: " . ($module->deleted_by === null ? "None" : $module->deleted_by) . "\n";
echo "Module Created Date: " . $module->created_date->format("Y-m-d H:i:s") . "\n";

?>
```