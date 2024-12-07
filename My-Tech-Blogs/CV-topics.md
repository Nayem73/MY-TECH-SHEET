# Jira (Scrum Specific)

#### 1. **What is Jira?**

**Answer:**
Jira is a project management tool developed by Atlassian. It is widely used for bug tracking, issue tracking, and project management. Originally designed for software development teams, it has evolved to support all kinds of project management tasks, especially for Agile methodologies like Scrum.

#### 2. **How do you use Jira in your Scrum projects?**

**Answer:**
You can mention specific use cases such as:

- **Creating User Stories and Tasks:** Creating issues for user stories, tasks, and bugs.
- **Sprint Planning:** Using the backlog to plan sprints by dragging and dropping issues into the sprint backlog.
- **Sprint Tracking:** Using the Scrum board to track the progress of tasks during the sprint.
- **Daily Stand-ups:** Updating task statuses and adding comments to issues for team collaboration.
- **Sprint Reviews and Retrospectives:** Reviewing completed tasks and generating reports to improve future sprints.

#### 3. **What are Jira workflows?**

**Answer:**
A Jira workflow is a series of steps or statuses that an issue goes through during its lifecycle. It defines the transitions between these statuses. For example, a typical workflow might include statuses like To Do, In Progress, In Review, and Done.

#### 4. **Can you explain what an issue is in Jira?**

**Answer:**
In Jira, an issue can be a task, bug, user story, or any piece of work that needs to be tracked and managed. Issues can be assigned to team members, prioritized, and tracked through their lifecycle.

#### 5. **How do you prioritize issues in Jira?**

**Answer:**
Issues can be prioritized based on their importance and urgency. Jira allows you to set priorities such as Highest, High, Medium, Low, and Lowest. You can also use custom fields or labels to further categorize and prioritize issues.

#### 6. **What are Jira boards?**

**Answer:**
Jira boards (Kanban or Scrum) are visual representations of the work process. They help teams manage and visualize their tasks. 

- **Scrum Board:** Used for teams following the Scrum methodology, showing tasks in the context of a sprint.

#### 7. **How do you manage sprints in Jira?**

**Answer:**
For managing sprints, you can:

- **Create a Sprint:** Define the sprint duration and scope.
- **Plan Sprint:** Add issues to the sprint backlog.
- **Start Sprint:** Begin the sprint and track progress using the Scrum board.
- **Close Sprint:** Complete the sprint, review the progress, and handle any incomplete issues.

#### 8. **What types of reports does Jira provide?**

**Answer:**
Jira offers a variety of reports such as:

- **Burn-Down Chart:** Tracks the remaining work in a sprint.
- **Burn-Up Chart:** Shows the work completed against the total work.
- **Velocity Chart:** Measures the amount of work a team can handle in a sprint.
- **Sprint Report:** Summarizes the work completed and any issues.

#### 9. **How do you customize Jira to fit your project needs?**

**Answer:**
Customization in Jira can involve:

- **Custom Fields:** Adding new fields to capture specific information.
- **Workflows:** Creating or modifying workflows to fit your process.
- **Screens and Schemes:** Customizing issue screens and field configurations.
- **Add-Ons:** Integrating with other tools using Jira add-ons from the Atlassian Marketplace.

#### 10. **What is a Jira filter?**

**Answer:**
A Jira filter is a way to search and sort issues based on specific criteria using JQL (Jira Query Language). Filters can be saved and shared with team members to easily access specific sets of issues.

### Practical Example (Scrum Specific)

To demonstrate your knowledge, you might want to describe a practical scenario where you used Jira in a Scrum project:

**Example:**
"In my previous project, we used Jira to manage our software development process following the Scrum methodology. We created a product backlog with user stories and tasks, which we prioritized based on business value and complexity. During sprint planning, we moved the highest priority items into the sprint backlog and broke them down into smaller tasks.

Throughout the sprint, we used the Scrum board to track the progress of each task, moving them from To Do to In Progress, In Review, and Done. Daily stand-up meetings were supported by the Jira board, allowing us to quickly identify any blockers and update the status of our tasks.

At the end of each sprint, we used Jira's reporting features to generate burn-down charts and velocity charts, which helped us assess our progress and plan for the next sprint. During sprint reviews, we demonstrated completed features and gathered feedback, while retrospectives focused on analyzing the reports to identify areas for improvement."

By preparing these explanations and examples, you will be able to demonstrate your practical knowledge and experience with Jira during your interview.

# Maven

### Common Questions and Explanations (Maven)

#### 1. **What is Maven?**

**Answer:**
Apache Maven is a build automation tool used primarily for Java projects. It simplifies the build process by providing a uniform build system, project management, and comprehension via plugins, a project object model (POM), and dependency management.

#### 2. **What is a POM file in Maven?**

**Answer:**
POM (Project Object Model) is an XML file that contains information about the project and configuration details used by Maven to build the project. It includes details such as project dependencies, plugins, goals, and other project configurations.

#### 3. **How do you add a dependency in Maven?**

**Answer:**
To add a dependency, you include it in the `dependencies` section of the POM file. For example:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.5.2</version>
</dependency>
```

#### 4. **What are Maven goals and phases?**

**Answer:**

- **Goals:** A specific task that contributes to the building and managing of a project, like `compile`, `test`, `package`.
- **Phases:** A sequence of goals bound to a lifecycle, like `clean`, `validate`, `compile`, `test`, `package`, `verify`, `install`, and `deploy`.

#### 5. **What is a Maven repository?**

**Answer:**
A Maven repository is a directory where all the project jars, library jars, plugins, and other project-specific artifacts are stored and shared. Types of repositories include:

- **Local Repository:** Located on the developer’s machine.
- **Central Repository:** Managed by Maven community, accessible via internet.
- **Remote Repository:** Third-party repository or a repository within an organization.

#### 6. **How do you create a Maven project?**

**Answer:**
You can create a Maven project using the command line:

```sh
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

This command generates a simple project structure.

#### 7. **What is the purpose of the `mvn clean` command?**

**Answer:**
The `mvn clean` command removes the `target` directory, which contains the compiled files and build artifacts. This ensures a clean build environment.

#### 8. **What is the `mvn install` command used for?**

**Answer:**
The `mvn install` command builds the project and installs the resulting artifact (jar, war, etc.) into the local Maven repository, making it available for other projects on the same machine.

#### 9. **Explain the `dependency:tree` goal.**

**Answer:**
The `dependency:tree` goal is used to display the dependency tree for the project, showing how dependencies are resolved. It helps to identify conflicts or issues with dependency versions.

```sh
mvn dependency:tree
```

#### 10. **How do you configure a plugin in Maven?**

**Answer:**
Plugins are configured in the `build` section of the POM file. For example, configuring the `maven-compiler-plugin` to use a specific Java version:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### Practical Example

To demonstrate your knowledge, you might want to describe a practical scenario where you used Maven:

**Example:**
"In my previous project, I used Maven to manage our Java project's build lifecycle. We defined all project dependencies in the POM file, ensuring that all team members had a consistent development environment. During the build process, we used `mvn clean` to clear previous builds, `mvn compile` to compile the code, and `mvn package` to bundle the application into a JAR file.

We also utilized plugins like `maven-surefire-plugin` for running tests and `maven-compiler-plugin` to specify the Java version. When adding new libraries, we updated the POM file with the necessary dependencies and used `mvn dependency:tree` to check for any version conflicts. This streamlined our build process and ensured that all dependencies were correctly managed and updated."

By preparing these explanations and examples, you will be able to demonstrate your practical knowledge and experience with Maven during your interview.

# JUnit

### JUnit in Spring Boot

#### 1. **What is JUnit?**

**Answer:**
JUnit is a popular testing framework for Java applications. It allows developers to write and run repeatable tests. JUnit is widely used for unit testing of code.

#### 2. **Why is JUnit important for Spring Boot applications?**

**Answer:**
JUnit is essential for Spring Boot applications as it helps ensure that the code works as expected. By writing tests, you can catch bugs early, verify that changes do not break existing functionality, and maintain a high level of code quality.

#### 3. **How do you set up JUnit in a Spring Boot project?**

**Answer:**

- **Step 1:** Add the necessary dependencies to your `pom.xml` (for Maven) or `build.gradle` (for Gradle). For Maven:
  
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-test</artifactId>
          <scope>test</scope>
      </dependency>
  </dependencies>
  ```

- **Step 2:** Create a test class in the `src/test/java` directory of your project. Annotate this class with `@SpringBootTest`.

#### 4. **What is a simple example of a JUnit test in a Spring Boot application?**

**Answer:**
Let's say you have a simple service that adds two numbers. Here’s how you can write a test for it.

- **Service Class:**
  
  ```java
  @Service
  public class CalculatorService {
      public int add(int a, int b) {
          return a + b;
      }
  }
  ```

- **Test Class:**
  
  ```java
  @SpringBootTest
  public class CalculatorServiceTest {
  
      @Autowired
      private CalculatorService calculatorService;
  
      @Test
      public void testAdd() {
          int result = calculatorService.add(10, 20);
          assertEquals(30, result);
      }
  }
  ```

#### 5. **What annotations are commonly used in JUnit tests for Spring Boot?**

**Answer:**

- **@SpringBootTest:** Used to create an application context for integration tests.
- **@Test:** Marks a method as a test method.
- **@BeforeEach:** Executed before each test method.
- **@AfterEach:** Executed after each test method.
- **@MockBean:** Used to add mock objects to the Spring application context.
- **@Autowired:** Used to inject beans into the test class.

#### 6. **How do you mock dependencies in JUnit tests with Spring Boot?**

**Answer:**
You can use `@MockBean` to mock dependencies in your test class. Here’s an example:

- **Service Class:**
  
  ```java
  @Service
  public class UserService {
      @Autowired
      private UserRepository userRepository;
  
      public User getUserById(Long id) {
          return userRepository.findById(id).orElse(null);
      }
  }
  ```

- **Test Class:**
  
  ```java
  @SpringBootTest
  public class UserServiceTest {
  
      @Autowired
      private UserService userService;
  
      @MockBean
      private UserRepository userRepository;
  
      @Test
      public void testGetUserById() {
          User user = new User();
          user.setId(1L);
          when(userRepository.findById(1L)).thenReturn(Optional.of(user));
  
          User result = userService.getUserById(1L);
          assertEquals(1L, result.getId().longValue());
      }
  }
  ```

#### 7. **How do you run JUnit tests in a Spring Boot project?**

**Answer:**
JUnit tests can be run using your IDE, Maven, or Gradle.

- **IDE:** Right-click on the test class or method and select "Run".
- **Maven:** Run `mvn test` in the terminal.
- **Gradle:** Run `gradle test` in the terminal.

#### 8. **What are some best practices for writing JUnit tests in Spring Boot?**

**Answer:**

- **Write clear and concise tests:** Each test should focus on a single functionality.
- **Use meaningful test method names:** Describe what the test is checking.
- **Avoid hard-coded values:** Use constants or parameterized tests.
- **Mock external dependencies:** To isolate the unit of work being tested.
- **Check edge cases:** Ensure that your code handles unexpected inputs gracefully.

By preparing these explanations and examples, you will be able to demonstrate your practical knowledge and experience with JUnit and Spring Boot during your interview.

# JWT

#### **How JWT Works**

- **Authentication:** When the user logs in using their credentials, the server generates a JWT and sends it back to the client.
- **Storage:** The client stores the JWT, usually in local storage or cookies.
- **Authorization:** On subsequent requests, the client sends the JWT in the HTTP header. The server verifies the token and grants access to protected resources.
