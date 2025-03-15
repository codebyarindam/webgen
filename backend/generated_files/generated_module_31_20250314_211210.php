```php
<?php

class Module {
    private $id;
    private $name;
    private $description;
    private $displayOrder;
    private $createdBy;
    private $updatedBy;
    private $createdAt;
    private $updatedAt;

    public function __construct($id, $name, $description, $displayOrder, $createdBy, $updatedBy, $createdAt, $updatedAt) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->displayOrder = $displayOrder;
        $this->createdBy = $createdBy;
        $this->updatedBy = $updatedBy;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
    }

    public function __toString() {
        return "Module " . $this->id . ": " . $this->name . "\nDescription: " . $this->description . "\nDisplay Order: " . $this->displayOrder . "\nCreated By: " . $this->createdBy . "\nUpdated By: " . $this->updatedBy . "\nCreated At: " . $this->createdAt . "\nUpdated At: " . $this->updatedAt;
    }
}

$data = array("id" => 31, "name" => 'Index Page', "description" => 'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', "displayOrder" => 1, "createdBy" => null, "updatedBy" => null, "createdAt" => '2025-02-05 09:17:38', "updatedAt" => null);

$module = new Module($data["id"], $data["name"], $data["description"], $data["displayOrder"], $data["createdBy"], $data["updatedBy"], $data["createdAt"], $data["updatedAt"]);

print($module . "\n");

?>
```

To run this code, save it to a file named `module.php` and run it with PHP: `php module.php`.

When you run this code, it creates a new `Module` object and prints its details to the console.

### Explanation

This PHP code defines a `Module` class to represent the provided data. The class has properties for `id`, `name`, `description`, `displayOrder`, `createdBy`, `updatedBy`, `createdAt`, and `updatedAt`. The `__construct` method initializes these properties when an object is created. The `__toString` method returns a string representation of the object.

The code then creates a new `Module` object using the provided data and prints its details to the console.

### Output

The output of this code will be:

```
Module 31: Index Page
Description: Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.
Display Order: 1
Created By: 
Updated By: 
Created At: 2025-02-05 09:17:38
Updated At: 
```