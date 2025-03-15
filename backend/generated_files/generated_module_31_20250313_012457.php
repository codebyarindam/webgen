```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $orderId;
    private $parentId;
    private $moduleId;
    private $controllerId;
    private $createdAt;

    public function __construct($id, $name, $description, $orderId, $parentId, $moduleId, $controllerId, $createdAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->orderId = $orderId;
        $this->parentId = $parentId;
        $this->moduleId = $moduleId;
        $this->controllerId = $controllerId;
        $this->createdAt = $createdAt;
    }

    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getOrderId() {
        return $this->orderId;
    }

    public function getParentId() {
        return $this->parentId;
    }

    public function getModuleId() {
        return $this->moduleId;
    }

    public function getControllerId() {
        return $this->controllerId;
    }

    public function getCreatedAt() {
        return $this->createdAt;
    }
}

$data = array(31, 'Index Page', 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 1, null, null, null, new DateTime('2025-02-05 09:17:38'));

$module = new Module($data[0], $data[1], $data[2], $data[3], $data[4], $data[5], $data[6], $data[7]);

print_r($module);

?>
```