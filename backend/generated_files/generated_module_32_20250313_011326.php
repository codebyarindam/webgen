```php
<?php

class Module {
    private $moduleId;
    private $moduleName;
    private $moduleDescription;
    private $moduleIdParent;
    private $moduleOrder;

    public function __construct($moduleId, $moduleName, $moduleDescription, $moduleIdParent = null, $moduleOrder = null) {
        $this->moduleId = $moduleId;
        $this->moduleName = $moduleName;
        $this->moduleDescription = $moduleDescription;
        $this->moduleIdParent = $moduleIdParent;
        $this->moduleOrder = $moduleOrder;
    }

    public function __toString() {
        return "Module ID: $this->moduleId\nModule Name: $this->moduleName\nModule Description: $this->moduleDescription\nModule ID Parent: $this->moduleIdParent\nModule Order: $this->moduleOrder";
    }
}

$data = [
    [
        'moduleId' => 32,
        'moduleName' => 'Group Page',
        'moduleDescription' => 'Display the name of the selected group.
Allow users to:
Add a new contact.
Edit existing contacts.
Delete existing contacts.
Search for contacts within the group.',
        'moduleIdParent' => 1,
        'moduleOrder' => null,
        'createdDate' => new DateTime('2025-02-05 09:18:22')
    ]
];

$modules = [];
foreach ($data as $moduleData) {
    $module = new Module(
        $moduleData['moduleId'],
        $moduleData['moduleName'],
        $moduleData['moduleDescription'],
        $moduleData['moduleIdParent'],
        $moduleData['moduleOrder']
    );
    $modules[] = $module;
}

foreach ($modules as $module) {
    echo $module . "\n";
}
```

In this PHP code:

- We define a `Module` class to represent each module.
- We create an instance of the `Module` class for each module in the provided data.
- We store each `Module` instance in an array called `$modules`.
- Finally, we print out the details of each module.

This code will output:

```
Module ID: 32
Module Name: Group Page
Module Description: Display the name of the selected group.
Allow users to:
Add a new contact.
Edit existing contacts.
Delete existing contacts.
Search for contacts within the group.
Module ID Parent: 1
Module Order:
```