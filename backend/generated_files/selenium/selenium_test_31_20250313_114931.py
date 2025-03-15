Below is a Selenium test script to validate the functionality of the generated project: Group Management System.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class GroupManagementSystemTest {

    WebDriver driver;

    @BeforeTest
    public void setup() {
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
        driver.get("http://localhost:8080/group-management-system");
    }

    @AfterTest
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void testCreateNewGroup() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement createNewGroupButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#create-new-group")));
        createNewGroupButton.click();

        WebElement groupNameInput = driver.findElement(By.cssSelector("#group-name"));
        groupNameInput.sendKeys("Friends");

        WebElement saveButton = driver.findElement(By.cssSelector("#save"));
        saveButton.click();

        WebElement groupList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list")));
        assert groupList.getText().contains("Friends");
    }

    @Test
    public void testSelectExistingGroup() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement groupList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list")));
        groupList.click();

        WebElement selectGroupButton = driver.findElement(By.cssSelector("#select-group"));
        selectGroupButton.click();

        WebElement groupNameInput = driver.findElement(By.cssSelector("#group-name"));
        groupNameInput.sendKeys("1");

        WebElement saveButton = driver.findElement(By.cssSelector("#save"));
        saveButton.click();

        WebElement contactList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#contact-list")));
        assert contactList != null;
    }

    @Test
    public void testViewEditContacts() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement groupList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list")));
        groupList.click();

        WebElement selectGroupButton = driver.findElement(By.cssSelector("#select-group"));
        selectGroupButton.click();

        WebElement groupNameInput = driver.findElement(By.cssSelector("#group-name"));
        groupNameInput.sendKeys("1");

        WebElement saveButton = driver.findElement(By.cssSelector("#save"));
        saveButton.click();

        WebElement viewContactsButton = driver.findElement(By.cssSelector("#view-contacts"));
        viewContactsButton.click();

        WebElement contactList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#contact-list")));
        assert contactList != null;

        WebElement editContactsButton = driver.findElement(By.cssSelector("#edit-contacts"));
        editContactsButton.click();

        WebElement newNameInput = driver.findElement(By.cssSelector("#new-name"));
        newNameInput.sendKeys("John Doe");

        WebElement newNumberInput = driver.findElement(By.cssSelector("#new-number"));
        newNumberInput.sendKeys("123-456-7890");

        WebElement saveButton2 = driver.findElement(By.cssSelector("#save"));
        saveButton2.click();

        WebElement contactList2 = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#contact-list")));
        assert contactList2.getText().contains("John Doe");
    }

    @Test
    public void testDisplayExistingGroups() {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement groupListButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list-button")));
        groupListButton.click();

        WebElement groupList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list")));
        assert groupList != null;
    }
}
```
However, there are several points to consider:
1. We'll need to convert the `GroupManagementSystem` to a web application for Selenium to work properly, because Selenium works by interacting with a GUI, not a console application.
2. The above test class assumes a web application and HTML structure that might not match the actual implementation of the `GroupManagementSystem` class.
3. These tests can be used as a starting point but will likely need to be modified and expanded to fully cover the functionality of the `GroupManagementSystem` class.

To convert the `GroupManagementSystem` to a web application, we could use a Java web framework like Spring Boot, which would involve creating a new Spring Boot project, mapping the console interactions to HTTP requests and responses, and updating the tests to use the new web application. Here is an example of how this could be done:
### GroupController.java
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GroupController {

    private final GroupService groupService;

    @Autowired
    public GroupController(GroupService groupService) {
        this.groupService = groupService;
    }

    @GetMapping("/groups")
    public List<Group> getGroups() {
        return groupService.getGroups();
    }

    @PostMapping("/groups")
    public Group createGroup(@RequestBody Group group) {
        return groupService.createGroup(group);
    }

    @GetMapping("/groups/{id}")
    public Group getGroup(@PathVariable int id) {
        return groupService.getGroup(id);
    }

    @PostMapping("/groups/{id}/contacts")
    public Contact createContact(@PathVariable int id, @RequestBody Contact contact) {
        return groupService.createContact(id, contact);
    }

    @GetMapping("/groups/{id}/contacts")
    public List<Contact> getContacts(@PathVariable int id) {
        return groupService.getContacts(id);
    }
}
```
### GroupService.java
```java
import java.util.List;

public interface GroupService {

    List<Group> getGroups();

    Group createGroup(Group group);

    Group getGroup(int id);

    Contact createContact(int id, Contact contact);

    List<Contact> getContacts(int id);
}
```
### GroupServiceImpl.java
```java
import java.util.List;

@Service
public class GroupServiceImpl implements GroupService {

    private final GroupRepository groupRepository;
    private final ContactRepository contactRepository;

    @Autowired
    public GroupServiceImpl(GroupRepository groupRepository, ContactRepository contactRepository) {
        this.groupRepository = groupRepository;
        this.contactRepository = contactRepository;
    }

    @Override
    public List<Group> getGroups() {
        return groupRepository.findAll();
    }

    @Override
    public Group createGroup(Group group) {
        return groupRepository.save(group);
    }

    @Override
    public Group getGroup(int id) {
        return groupRepository.findById(id).orElse(null);
    }

    @Override
    public Contact createContact(int id, Contact contact) {
        Group group = getGroup(id);
        if (group != null) {
            contact.setGroup(group);
            return contactRepository.save(contact);
        } else {
            return null;
        }
    }

    @Override
    public List<Contact> getContacts(int id) {
        Group group = getGroup(id);
        if (group != null) {
            return contactRepository.findByGroup(group);
        } else {
            return null;
        }
    }
}
```
Then we would need to update the Selenium tests to use the REST API, like so:
```java
@Test
public void testCreateNewGroup() {
    WebDriverWait wait = new WebDriverWait(driver, 10);
    driver.get("http://localhost:8080/groups");

    WebElement groupNameInput = driver.findElement(By.cssSelector("#group-name"));
    groupNameInput.sendKeys("Friends");

    WebElement saveButton = driver.findElement(By.cssSelector("#save"));
    saveButton.click();

    driver.get("http://localhost:8080/groups");

    WebElement groupList = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#group-list")));
    assert groupList.getText().contains("Friends");
}
```