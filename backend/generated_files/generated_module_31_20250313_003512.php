Based on the provided data, I will generate a PHP code to create the index page with the specified functionality and a Python script using Selenium for browser automation.

### PHP Code

```php
<?php
// index.php

// Initialize the database connection
$conn = new mysqli("localhost", "username", "password", "database");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to display existing groups
function display_groups() {
    global $conn;
    $sql = "SELECT * FROM groups";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<a href='view_group.php?group_id=" . $row["id"] . "'>" . $row["name"] . "</a><br>";
        }
    } else {
        echo "No groups found.";
    }
}

// Function to create a new group
function create_group() {
    global $conn;
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $group_name = $_POST["group_name"];
        $sql = "INSERT INTO groups (name) VALUES ('$group_name')";
        if ($conn->query($sql) === TRUE) {
            echo "Group created successfully.";
        } else {
            echo "Error creating group: " . $conn->error;
        }
    }
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
</head>
<body>
    <h1>Index Page</h1>
    <h2>Existing Groups:</h2>
    <?php display_groups(); ?>
    
    <h2>Create a new group:</h2>
    <form method="post">
        <label for="group_name">Group Name:</label><br>
        <input type="text" id="group_name" name="group_name" required><br>
        <input type="submit" value="Create Group">
    </form>
</body>
</html>
```

### Python Script using Selenium

```python
# selenium_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the webdriver
driver = webdriver.Chrome()  # Replace with your preferred browser

# Function to create a new group
def create_group(group_name):
    driver.get("http://localhost/index.php")  # Replace with your website URL
    try:
        # Wait for the create group form to load
        create_group_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )
        
        # Fill in the group name
        group_name_input = create_group_form.find_element(By.NAME, "group_name")
        group_name_input.send_keys(group_name)
        
        # Submit the form
        create_group_form.find_element(By.TAG_NAME, "input").click()
    except TimeoutException:
        print("Error creating group: Timed out waiting for page to load")

# Function to view an existing group
def view_group(group_id):
    driver.get(f"http://localhost/view_group.php?group_id={group_id}")  # Replace with your website URL

# Create a new group
create_group("My New Group")

# View an existing group
view_group(1)

# Close the browser
driver.quit()
```

Note: Replace the database connection details and website URL in the PHP code with your own. Additionally, replace the `webdriver.Chrome()` line in the Python script with your preferred browser. Ensure that the Selenium webdriver is installed and configured correctly for your chosen browser.

These scripts are basic examples and may need to be adapted to fit your specific use case. You should also consider implementing security measures such as input validation and error handling to prevent potential issues.