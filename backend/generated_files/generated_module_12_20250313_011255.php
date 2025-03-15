```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $level;
    private $parent_id;
    private $created_at;
    private $updated_at;
    private $deleted_at;
    private $module_id;

    public function __construct($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->level = $level;
        $this->parent_id = $parent_id;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
        $this->deleted_at = $deleted_at;
        $this->module_id = $module_id;
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

    public function get_level() {
        return $this->level;
    }

    public function get_parent_id() {
        return $this->parent_id;
    }

    public function get_created_at() {
        return $this->created_at;
    }

    public function get_updated_at() {
        return $this->updated_at;
    }

    public function get_deleted_at() {
        return $this->deleted_at;
    }

    public function get_module_id() {
        return $this->module_id;
    }
}

$data = array(
    array(12, 'DOCTOR_MANAGEMENT_MODULE', 'A module to manage doctor information and schedules.', 2, null, null, null, 12, new DateTime('2022-01-12 12:00:00'))
);

$modules = array();
foreach ($data as $module_data) {
    list($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id) = $module_data;
    $created_at = $created_at ? new DateTime($created_at) : null;
    $updated_at = $updated_at ? new DateTime($updated_at) : null;
    $deleted_at = $deleted_at ? new DateTime($deleted_at) : null;
    $modules[] = new Module($id, $name, $description, $level, $parent_id, $created_at, $updated_at, $deleted_at, $module_id);
}

foreach ($modules as $module) {
    echo "ID: " . $module->get_id() . "\n";
    echo "Name: " . $module->get_name() . "\n";
    echo "Description: " . $module->get_description() . "\n";
    echo "Level: " . $module->get_level() . "\n";
    echo "Parent ID: " . ($module->get_parent_id() !== null ? $module->get_parent_id() : 'None') . "\n";
    echo "Created At: " . ($module->get_created_at() !== null ? $module->get_created_at()->format('Y-m-d H:i:s') : 'None') . "\n";
    echo "Updated At: " . ($module->get_updated_at() !== null ? $module->get_updated_at()->format('Y-m-d H:i:s') : 'None') . "\n";
    echo "Deleted At: " . ($module->get_deleted_at() !== null ? $module->get_deleted_at()->format('Y-m-d H:i:s') : 'None') . "\n";
    echo "Module ID: " . $module->get_module_id() . "\n\n";
}
?>
```