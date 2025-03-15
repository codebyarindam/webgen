Here's an example of PHP code based on the provided data. This code defines a class named `ModuleDetails` and uses an associative array to store and display the module details.

```php
<?php

// Define the ModuleDetails class
class ModuleDetails {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleIdOrder;
    private $createdBy;
    private $updatedBy;
    private $deletedBy;
    private $createdAt;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleIdOrder, $createdBy, $updatedBy, $deletedBy, $createdAt) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleIdOrder = $moduleIdOrder;
        $this->createdBy = $createdBy;
        $this->updatedBy = $updatedBy;
        $this->deletedBy = $deletedBy;
        $this->createdAt = $createdAt;
    }

    public function __toString() {
        return "Module ID: $this->moduleId\nModule Name: $this->moduleName\nModule Description: $this->moduleDescription\nModule ID Order: $this->moduleIdOrder\nCreated By: $this->createdBy\nUpdated By: $this->updatedBy\nDeleted By: $this->deletedBy\nCreated At: $this->createdAt";
    }
}

// Create a new ModuleDetails object
$moduleId = 31;
$moduleName = 'Index Page';
$moduleDescription = 'Display a list of existing groups.' . "\r\n" . 'Provide options to:' . "\r\n" . 'Create a new group.' . "\r\n" . 'Select an existing group to view/edit contacts.';
$moduleIdOrder = 1;
$createdBy = null;
$updatedBy = null;
$deletedBy = null;
$createdAt = '2025-02-05 09:17:38';

// You can use DateTime object if you want
//$createdAt = date('Y-m-d H:i:s', strtotime('2025-02-05 09:17:38'));

$moduleDetails = new ModuleDetails($moduleId, $moduleName, $moduleDescription, $moduleIdOrder, $createdBy, $updatedBy, $deletedBy, $createdAt);

// Display the module details
echo $moduleDetails . "\n";

?>
```

If you're planning to store this data in a database and then create the ModuleDetails object, you would replace the variables in the ModuleDetails constructor with your database query results.

Here's how you would do it using MySQL and PDO:

```php
<?php
class ModuleDetails {
    // existing code...
}

try {
    $host = 'localhost';
    $dbname = 'your_database_name';
    $username = 'your_database_username';
    $password = 'your_database_password';

    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sql = "SELECT module_id, module_name, module_description, module_id_order, created_by, updated_by, deleted_by, created_at FROM modules";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();

    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $moduleDetails = new ModuleDetails(
            $row['module_id'],
            $row['module_name'],
            $row['module_description'],
            $row['module_id_order'],
            $row['created_by'],
            $row['updated_by'],
            $row['deleted_by'],
            $row['created_at']
        );

        echo $moduleDetails . "\n";
    }

    $stmt = null;
    $pdo = null;
} catch (PDOException $e) {
    echo $e->getMessage();
}
?>
```

You would replace `'localhost'`, `'your_database_name'`, `'your_database_username'`, and `'your_database_password'` with your actual MySQL host, database name, username, and password.

You would also need a `modules` table with the corresponding columns (`module_id`, `module_name`, `module_description`, `module_id_order`, `created_by`, `updated_by`, `deleted_by`, `created_at`). 

Remember that storing sensitive data such as database credentials directly in your script is not recommended for security reasons. Instead, consider using environment variables or a secure secrets manager.