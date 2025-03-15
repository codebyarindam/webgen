**Group Management System**
==========================

Below is a simple implementation of a group management system in Java. This system will have the following features:
- Display a list of existing groups
- Create a new group
- Select an existing group to view/edit contacts

### Group.java
```java
/**
 * Represents a group in the system.
 */
public class Group {
    private int id;
    private String name;

    public Group(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
```

### Contact.java
```java
/**
 * Represents a contact in the system.
 */
public class Contact {
    private int id;
    private String name;
    private String phoneNumber;

    public Contact(int id, String name, String phoneNumber) {
        this.id = id;
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }
}
```

### GroupManagementSystem.java
```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * The main class for the group management system.
 */
public class GroupManagementSystem {
    private List<Group> groups;
    private List<Contact> contacts;
    private Scanner scanner;

    public GroupManagementSystem() {
        this.groups = new ArrayList<>();
        this.contacts = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Displays the index page.
     */
    public void displayIndexPage() {
        System.out.println("Group Management System");
        System.out.println("1. Create a new group");
        System.out.println("2. Select an existing group to view/edit contacts");
        System.out.println("3. Display a list of existing groups");
        System.out.print("Enter your choice: ");
        int choice = Integer.parseInt(scanner.nextLine());
        switch (choice) {
            case 1:
                createNewGroup();
                break;
            case 2:
                selectExistingGroup();
                break;
            case 3:
                displayExistingGroups();
                break;
            default:
                System.out.println("Invalid choice. Please try again.");
        }
    }

    /**
     * Creates a new group.
     */
    private void createNewGroup() {
        System.out.print("Enter group name: ");
        String groupName = scanner.nextLine();
        Group newGroup = new Group(groups.size() + 1, groupName);
        groups.add(newGroup);
        System.out.println("Group created successfully.");
        displayIndexPage();
    }

    /**
     * Selects an existing group to view/edit contacts.
     */
    private void selectExistingGroup() {
        System.out.println("Select a group:");
        for (Group group : groups) {
            System.out.println(group.getId() + ". " + group.getName());
        }
        System.out.print("Enter group ID: ");
        int groupId = Integer.parseInt(scanner.nextLine());
        Group selectedGroup = groups.stream()
                .filter(group -> group.getId() == groupId)
                .findFirst()
                .orElse(null);
        if (selectedGroup != null) {
            viewEditContacts(selectedGroup);
        } else {
            System.out.println("Group not found.");
            displayIndexPage();
        }
    }

    /**
     * Views or edits contacts for the given group.
     * @param group the selected group
     */
    private void viewEditContacts(Group group) {
        System.out.println("Contacts for " + group.getName());
        System.out.println("1. View contacts");
        System.out.println("2. Edit contacts");
        System.out.print("Enter your choice: ");
        int choice = Integer.parseInt(scanner.nextLine());
        switch (choice) {
            case 1:
                viewContacts(group);
                break;
            case 2:
                editContacts(group);
                break;
            default:
                System.out.println("Invalid choice. Please try again.");
        }
    }

    /**
     * Views contacts for the given group.
     * @param group the selected group
     */
    private void viewContacts(Group group) {
        // Assuming contacts are stored in a separate list
        for (Contact contact : contacts) {
            System.out.println(contact.getName() + " - " + contact.getPhoneNumber());
        }
        displayIndexPage();
    }

    /**
     * Edits contacts for the given group.
     * @param group the selected group
     */
    private void editContacts(Group group) {
        // Assuming contacts are stored in a separate list
        System.out.print("Enter new contact name: ");
        String contactName = scanner.nextLine();
        System.out.print("Enter new contact phone number: ");
        String contactPhoneNumber = scanner.nextLine();
        Contact newContact = new Contact(contacts.size() + 1, contactName, contactPhoneNumber);
        contacts.add(newContact);
        System.out.println("Contact added successfully.");
        displayIndexPage();
    }

    /**
     * Displays a list of existing groups.
     */
    private void displayExistingGroups() {
        System.out.println("Existing groups:");
        for (Group group : groups) {
            System.out.println(group.getId() + ". " + group.getName());
        }
        displayIndexPage();
    }

    /**
     * Runs the group management system.
     */
    public void run() {
        displayIndexPage();
    }

    public static void main(String[] args) {
        GroupManagementSystem system = new GroupManagementSystem();
        system.run();
    }
}
```

### Usage

To run the group management system, simply compile and execute the `GroupManagementSystem` class. The system will display the index page, where you can choose to create a new group, select an existing group, or display a list of existing groups.

**Example Use Case**

1. Run the system and choose to create a new group.
2. Enter a group name, such as "Friends".
3. Choose to select an existing group and enter the ID of the group you just created.
4. View or edit contacts for the selected group.

Note: This is a basic implementation and you may want to add more features, such as storing contacts in a database, adding error handling, and implementing security measures.