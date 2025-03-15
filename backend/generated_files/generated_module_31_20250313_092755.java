Here's a Java class that represents the given module details:

```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Module {
    private int id;
    private String name;
    private String description;
    private int moduleId;
    private Integer parentId;
    private Integer groupId;
    private Integer userId;
    private LocalDateTime createdAt;

    public Module(int id, String name, String description, int moduleId, Integer parentId, Integer groupId, Integer userId, LocalDateTime createdAt) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.moduleId = moduleId;
        this.parentId = parentId;
        this.groupId = groupId;
        this.userId = userId;
        this.createdAt = createdAt;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getModuleId() {
        return moduleId;
    }

    public void setModuleId(int moduleId) {
        this.moduleId = moduleId;
    }

    public Integer getParentId() {
        return parentId;
    }

    public void setParentId(Integer parentId) {
        this.parentId = parentId;
    }

    public Integer getGroupId() {
        return groupId;
    }

    public void setGroupId(Integer groupId) {
        this.groupId = groupId;
    }

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return "Module{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", moduleId=" + moduleId +
                ", parentId=" + parentId +
                ", groupId=" + groupId +
                ", userId=" + userId +
                ", createdAt=" + createdAt.format(formatter) +
                '}';
    }

    public static void main(String[] args) {
        Module module = new Module(
                31,
                "Index Page",
                "Display a list of existing groups.\r\nProvide options to:\r\nCreate a new group.\r\nSelect an existing group to view/edit contacts.",
                1,
                null,
                null,
                null,
                LocalDateTime.of(2025, 2, 5, 9, 17, 38)
        );
        System.out.println(module.toString());
    }
}
```

This Java class `Module` represents the given data with its respective properties and methods for getting and setting the properties. The `toString` method is overridden to provide a human-readable representation of the object. In the `main` method, an instance of `Module` is created with the given data and printed to the console.