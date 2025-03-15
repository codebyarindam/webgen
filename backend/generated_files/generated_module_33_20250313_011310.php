Here's a PHP code based on the provided data. The code will include class properties and methods to create, read, update, and delete contact details.

```php
<?php

class Contact {
    private $id;
    private $fullName;
    private $phoneNumbers;
    private $email;
    private $address;
    private $notes;

    public function __construct($id, $fullName, $phoneNumbers, $email, $address, $notes) {
        $this->id = $id;
        $this->fullName = $fullName;
        $this->phoneNumbers = $phoneNumbers;
        $this->email = $email;
        $this->address = $address;
        $this->notes = $notes;
    }

    // Getters
    public function getId() {
        return $this->id;
    }

    public function getFullName() {
        return $this->fullName;
    }

    public function getPhoneNumbers() {
        return $this->phoneNumbers;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getAddress() {
        return $this->address;
    }

    public function getNotes() {
        return $this->notes;
    }

    // Setters
    public function setFullName($fullName) {
        $this->fullName = $fullName;
    }

    public function setPhoneNumbers($phoneNumbers) {
        $this->phoneNumbers = $phoneNumbers;
    }

    public function setEmail($email) {
        $this->email = $email;
    }

    public function setAddress($address) {
        $this->address = $address;
    }

    public function setNotes($notes) {
        $this->notes = $notes;
    }
}

class ContactDetailsPage {
    private $contacts;

    public function __construct() {
        $this->contacts = [];
    }

    // Create a new contact
    public function createContact($id, $fullName, $phoneNumbers, $email, $address, $notes) {
        $contact = new Contact($id, $fullName, $phoneNumbers, $email, $address, $notes);
        $this->contacts[$id] = $contact;
        return $contact;
    }

    // Read contact details
    public function getContactDetails($id) {
        if (isset($this->contacts[$id])) {
            $contact = $this->contacts[$id];
            return [
                'id' => $contact->getId(),
                'fullName' => $contact->getFullName(),
                'phoneNumbers' => $contact->getPhoneNumbers(),
                'email' => $contact->getEmail(),
                'address' => $contact->getAddress(),
                'notes' => $contact->getNotes(),
            ];
        } else {
            return null;
        }
    }

    // Update contact details
    public function updateContact($id, $fullName = null, $phoneNumbers = null, $email = null, $address = null, $notes = null) {
        if (isset($this->contacts[$id])) {
            $contact = $this->contacts[$id];
            if ($fullName !== null) {
                $contact->setFullName($fullName);
            }
            if ($phoneNumbers !== null) {
                $contact->setPhoneNumbers($phoneNumbers);
            }
            if ($email !== null) {
                $contact->setEmail($email);
            }
            if ($address !== null) {
                $contact->setAddress($address);
            }
            if ($notes !== null) {
                $contact->setNotes($notes);
            }
            return true;
        } else {
            return false;
        }
    }

    // Delete contact
    public function deleteContact($id) {
        if (isset($this->contacts[$id])) {
            unset($this->contacts[$id]);
            return true;
        } else {
            return false;
        }
    }
}

// Example usage:
$page = new ContactDetailsPage();
$contactId = 33;
$contact = $page->createContact($contactId, 'John Doe', ['123-456-7890'], 'john@example.com', '123 Main St', 'This is a note');
print_r($page->getContactDetails($contactId));
$page->updateContact($contactId, 'Jane Doe', ['987-654-3210'], 'jane@example.com', '456 Elm St', 'This is another note');
print_r($page->getContactDetails($contactId));
$page->deleteContact($contactId);
var_dump($page->getContactDetails($contactId));

```

As for creating a Selenium script to test the creation of a contact, here is an example in PHP:

```php
use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;

require_once "vendor/autoload.php";

$host = 'http://localhost:4444/wd/hub';
$capabilities = DesiredCapabilities::chrome();
$driver = RemoteWebDriver::create($host, $capabilities, 5000);

$driver->get("http://example.com/addressbook/contact");
$driver->setwIndowSize(1024, 768);
$fullNameInput = $driver->findElement(WebDriverBy::name("fullName"));
$fullNameInput->sendKeys("John Doe");
$phoneNumbersInput = $driver->findElement(WebDriverBy::name("phoneNumbers"));
$phoneNumbersInput->sendKeys("123-456-7890");
$emailInput = $driver->findElement(WebDriverBy::name("email"));
$emailInput->sendKeys("john@example.com");
$addressInput = $driver->findElement(WebDriverBy::name("address"));
$addressInput->sendKeys("123 Main St");
$notesInput = $driver->findElement(WebDriverBy::name("notes"));
$notesInput->sendKeys("This is a note");
$submitBtn = $driver->findElement(WebDriverBy::name("submit"));
$submitBtn->click();

$driver->quit();

```

Note: To use the above Selenium script, you need to install Selenium WebDriver and the Facebook WebDriver library. You can do this using Composer with the command `composer require facebook/webdriver`. Make sure you have the ChromeDriver executable in your system's PATH.

Make sure to adjust the URLs and element names according to your application. Also, ensure you're running your tests in an environment that has a compatible version of Chrome and the ChromeDriver executable in the system's PATH.