```php
class Module {
    public $id;
    public $name;
    public $description;
    public $sort_order;
    public $created_at;
    public $updated_at;

    function __construct($id, $name, $description, $sort_order, $created_at = null, $updated_at = null) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->sort_order = $sort_order;
        $this->created_at = $created_at;
        $this->updated_at = $updated_at;
    }
}

// Example usage:
$module = new Module(
    31, 
    'Index Page', 
    'Display a list of existing groups.
Provide options to:
Create a new group.
Select an existing group to view/edit contacts.', 
    1, 
    new DateTime('2025-02-05 09:17:38')
);

print_r($module);
```

Here's an explanation of the provided PHP code:
1. We create a `Module` class that represents a module with properties `id`, `name`, `description`, `sort_order`, `created_at`, and `updated_at`.
2. The `__construct` method initializes a new instance of the `Module` class. The `created_at` and `updated_at` parameters are optional and default to `null` if not provided.
3. We create a new instance of the `Module` class using the provided data. Note that PHP's `DateTime` class is used to represent dates and times.
4. Finally, we print the properties of the `$module` object using `print_r`.