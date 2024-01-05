1. Write a Java program to create a class called "Book" with attributes for title, author, and ISBN, and methods to add and remove books from a collection.

```java
package com.nayemtech;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
       Book English = new Book("English", "authorE", 2344);
       Book Bangla = new Book("Bangla", "authorB", 2345);
       Book Math = new Book("Math", "authorM", 2346);


       List<Book> bookList = new ArrayList<>();

       bookList.add(English);
       bookList.add(Bangla);
       bookList.add(Math);

       for (Book b : bookList) {
           System.out.println(b.getTitle() + " " + b.getAuthor() + " " + b.getISBN());
       }
    }
} 


package com.nayemtech;

public class Book {
    private String title;
    private String author;
    private long ISBN;

    public Book(String title, String author, long ISBN) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public long getISBN() {
        return ISBN;
    }

    public void setISBN(long ISBN) {
        this.ISBN = ISBN;
    }
}
```

* implementing above code with inheritance. this code is given below:

```java
package com.nayemtech;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
       Book english = new English();
       Book bangla = new Bangla();
       Book math = new Math();

       List<Book> bookList = new ArrayList<>();
       bookList.add(english);
       bookList.add(bangla);
       bookList.add(math);

       for (Book b : bookList) {
           b.read();
       }
    }
}

package com.nayemtech;

public abstract class Book {
    private String title;
    private String author;
    private long ISBN;

    public abstract void read();
}


package com.nayemtech;

public class English extends Book{
    @Override
    public void read() {
        System.out.println("Reading from English Book.");
    }
}


package com.nayemtech;

public class Bangla extends Book{
    @Override
    public void read() {
        System.out.println("Reading from Bangla Book.");
    }
}


package com.nayemtech;

public class Math extends Book{
    @Override
    public void read() {
        System.out.println("Reading from Math Book.");
    }
}
```

* Now, we can make the book class as an interface instead of the abstract class like above. but in this case, the interface's fields will be final, we need to initialize it. we can only override the method, but the attributes are final.

```java
package com.nayemtech;

public interface Book {
    String title = "Bangla";
    String author = "authorB";
    long ISBN = 2345;

    void read();
}
```

### chatGPT (provided above interface):

In the code you provided(above code), you've changed the `Book` class to an interface and included some constants (`title`, `author`, `ISBN`) within the interface. While this is syntactically correct, it introduces a couple of considerations:

1. **Constants in Interfaces:**
   
   - In Java, fields in interfaces are implicitly `public`, `static`, and `final`. Therefore, `title`, `author`, and `ISBN` are constants.
   - Constants in interfaces are usually intended to be public and shared across multiple classes that implement the interface.

2. **Lack of Flexibility:**
   
   - Constants in an interface cannot be modified or overridden by implementing classes. If you want each implementing class to have different values for these fields, using constants in the interface may not be the best approach.

3. **Design Considerations:**
   
   - Interfaces are typically used to define a contract for classes to implement, specifying method signatures without providing implementations.
   - Including fields in interfaces can be acceptable for constants shared by all implementing classes. However, for instance-specific values, it's usually better to use methods to provide flexibility.

Here's an alternative approach that maintains the interface but uses methods instead of constants for flexibility:

```java
package com.nayemtech;

public interface Book {
    String getTitle();
    String getAuthor();
    long getISBN();

    void read();
}
```

Now, any class implementing the `Book` interface must provide its own implementation for `getTitle()`, `getAuthor()`, and `getISBN()`, allowing different values for each class. For example:

```java
package com.nayemtech;

public class BanglaBook implements Book {
    private String title = "Bangla";
    private String author = "authorB";
    private long ISBN = 2345;

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }

    @Override
    public long getISBN() {
        return ISBN;
    }

    @Override
    public void read() {
        System.out.println("Reading from Bangla Book.");
    }
}
```

Using this approach, you retain the flexibility to have different values for each implementing class while still adhering to the interface contract.

# ***Single Respoinsibility Vs ... :***

Certainly, let's delve into the differences between having the collection inside the `Main` class (as in the first version) versus having it inside the `Book` class (as in the second version).

### First Version:

```java
public class Main {
    public static void main(String[] args) {
       Book english = new Book("English", "authorE", 2344);
       Book bangla = new Book("Bangla", "authorB", 2345);
       Book math = new Book("Math", "authorM", 2346);

       List<Book> bookList = new ArrayList<>();

       bookList.add(english);
       bookList.add(bangla);
       bookList.add(math);

       for (Book b : bookList) {
           System.out.println(b.getTitle() + " " + b.getAuthor() + " " + b.getISBN());
       }
    }
}
```

### Second Version:

```java
// Book.java
import java.util.ArrayList;

public class Book {
  private String title;
  private String author;
  private String ISBN;
  private static ArrayList<Book> bookCollection = new ArrayList<Book>();

  // ... constructor, getter, setter methods ...

  public static void add_Book(Book book) {
    bookCollection.add(book);
  }

  public static void remove_Book(Book book) {
    bookCollection.remove(book);
  }

  public static ArrayList<Book> get_BookCollection() {
    return bookCollection;
  }
}
```

### Comparison:

1. **Responsibility and Separation of Concerns:**
   
   - In the first version, the responsibility of managing the list of books is placed in the `Main` class. This adheres to the principle of separating concerns. The `Book` class is responsible for representing a book, while the `Main` class is responsible for managing the collection of books.
   - In the second version, the `Book` class itself manages a static list of all books. This can lead to a violation of the single responsibility principle, as a class ideally should have one reason to change.

2. **Encapsulation:**
   
   - In the first version, the `List<Book>` is encapsulated within the `Main` class, making it private to that class. This is a good practice as it hides the internal implementation details of how the list of books is managed.
   - In the second version, the `ArrayList<Book>` is static and directly accessible from outside the `Book` class. This can lead to a lack of encapsulation, as external classes can modify the list without going through proper methods.

3. **Flexibility and Reusability:**
   
   - The first version allows for flexibility in choosing the data structure for the list of books. You can easily switch to a different collection type or even a database without affecting the `Book` class.
   - The second version ties the `Book` class directly to an `ArrayList`. If you decide to change the underlying data structure or move to a database, you would need to modify the `Book` class, violating the Open/Closed Principle.

### Recommendations:

1. **First Version (Main Managing Collection):**
   
   - Use when you want to keep the responsibility of managing collections outside the class representing the entities (in this case, books).
   - Encourages better separation of concerns and follows the single responsibility principle.

2. **Second Version (Book Class Manages Collection):**
   
   - Use with caution, especially in cases where the class is primarily a data holder (like the `Book` class). Having a static collection inside such a class might lead to less maintainable and more tightly coupled code.
   - Consider this approach if you have a specific reason for having a global collection shared among all instances of the class.

In general, it's a good practice to encapsulate the collection management responsibilities in a dedicated class or the class responsible for managing the overall application state. This promotes better organization, maintainability, and adherence to object-oriented principles.

----------

### Q.7: Write a Java program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.

# Below code maintains the Single Responsibility principle but violates the Open/Closed principle:

* The deposit method and the withdraw method may need changes in the future on how they should be carried out so by adding them directly in the Account class will need modifications in the future, although the deposit and withdraw methods are direclty related to the Account class, so it maintains the single responsibility principle, it violates the Open/Closed principle.

```java
import java.util.ArrayList;
import java.util.List;

class Account {
    private String accountNumber;
    private String customerName;
    private double balance;

    public Account(String accountNumber, String customerName, double balance) {
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.balance = balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getCustomerName() {
        return customerName;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposit of $" + amount + " successful. New balance: $" + balance);
        } else {
            System.out.println("Invalid deposit amount. Please enter a positive value.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawal of $" + amount + " successful. New balance: $" + balance);
        } else {
            System.out.println("Invalid withdrawal amount or insufficient funds.");
        }
    }
}

public class Bank {
    private List<Account> accounts;

    public Bank() {
        this.accounts = new ArrayList<>();
    }

    public void addAccount(Account account) {
        accounts.add(account);
        System.out.println("Account added successfully. Account Number: " + account.getAccountNumber());
    }

    public void removeAccount(Account account) {
        if (accounts.remove(account)) {
            System.out.println("Account removed successfully. Account Number: " + account.getAccountNumber());
        } else {
            System.out.println("Account not found. Removal failed.");
        }
    }

    public void displayAccounts() {
        System.out.println("Accounts in the bank:");
        for (Account account : accounts) {
            System.out.println("Account Number: " + account.getAccountNumber() +
                    ", Customer Name: " + account.getCustomerName() +
                    ", Balance: $" + account.getBalance());
        }
    }

    public static void main(String[] args) {
        // Example usage:
        Bank bank = new Bank();

        Account account1 = new Account("1001", "John Doe", 1000.0);
        Account account2 = new Account("1002", "Jane Doe", 500.0);

        bank.addAccount(account1);
        bank.addAccount(account2);

        bank.displayAccounts();

        account1.deposit(500.0);
        account2.withdraw(200.0);

        bank.displayAccounts();
    }
}
```

* Below is the way on how we can maintain both single responsibility principle and open/closed principle:

```java
public interface AccountOperation {
    void execute(Account account);
}

class DepositOperation implements AccountOperation {
    private double amount;

    public DepositOperation(double amount) {
        this.amount = amount;
    }

    @Override
    public void execute(Account account) {
        account.deposit(amount);
    }
}

class WithdrawOperation implements AccountOperation {
    private double amount;

    public WithdrawOperation(double amount) {
        this.amount = amount;
    }

    @Override
    public void execute(Account account) {
        account.withdraw(amount);
    }
}

public class Bank {
    private List<Account> accounts;

    public Bank() {
        this.accounts = new ArrayList<>();
    }

    public void addAccount(Account account) {
        accounts.add(account);
        System.out.println("Account added successfully. Account Number: " + account.getAccountNumber());
    }

    public void removeAccount(Account account) {
        if (accounts.remove(account)) {
            System.out.println("Account removed successfully. Account Number: " + account.getAccountNumber());
        } else {
            System.out.println("Account not found. Removal failed.");
        }
    }

    public void displayAccounts() {
        System.out.println("Accounts in the bank:");
        for (Account account : accounts) {
            System.out.println("Account Number: " + account.getAccountNumber() +
                    ", Customer Name: " + account.getCustomerName() +
                    ", Balance: $" + account.getBalance());
        }
    }

    public void executeOperation(Account account, AccountOperation operation) {
        operation.execute(account);
    }

    public static void main(String[] args) {
        // Example usage:
        Bank bank = new Bank();

        Account account1 = new Account("1001", "John Doe", 1000.0);
        Account account2 = new Account("1002", "Jane Doe", 500.0);

        bank.addAccount(account1);
        bank.addAccount(account2);

        bank.displayAccounts();

        bank.executeOperation(account1, new DepositOperation(500.0));
        bank.executeOperation(account2, new WithdrawOperation(200.0));

        bank.displayAccounts();
    }
}
```

* The modified code maintains adherence to both the Single Responsibility Principle (SRP) and the Open/Closed Principle (OCP).

### Single Responsibility Principle (SRP):

- **`Account` Class:**
  
  - **Responsibility:** Represents an account with details and methods for deposit and withdrawal.
  - **Justification:** The `Account` class is responsible for managing the details of a single account, and its methods (`deposit` and `withdraw`) are directly related to the behavior of an account.

- **`AccountOperation` Interface and Implementing Classes (`DepositOperation`, `WithdrawOperation`):**
  
  - **Responsibility:** Represents operations on an account, such as deposit and withdrawal.
  - **Justification:** Each class adheres to the SRP by encapsulating the logic for a specific operation on an account.

- **`Bank` Class:**
  
  - **Responsibility:** Manages a collection of accounts and provides methods for adding, removing, displaying accounts, and executing operations on accounts.
  - **Justification:** The `Bank` class encapsulates the logic related to managing a bank's accounts, and it collaborates with the `AccountOperation` interface for executing different operations on accounts.

### Open/Closed Principle (OCP):

- **`Bank` Class:**
  
  - **Extension:** The `Bank` class is open for extension. You can introduce new `AccountOperation` implementations without modifying the existing `Bank` class.
  - **Closure:** The `Bank` class is closed for modification. Adding new operations does not require changing the `Bank` class.

- **`AccountOperation` Interface and Implementing Classes (`DepositOperation`, `WithdrawOperation`):**
  
  - **Extension:** New operations can be added by creating new classes implementing the `AccountOperation` interface without modifying existing code.
  - **Closure:** The existing classes (e.g., `Bank` and `Account`) don't need modification to support new operations.

# Now by me Alhamdulillah

```java
package com.nayemtech;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Bank sonaliBank = new Bank(); // ei bank er under e nicher account gulo thakbe tai ei line sobar first e likhlam

        Account nayemAccount = new Account(123, "Nayem", new BigDecimal("12000"));
        Account jimAccount = new Account(129, "Jim", new BigDecimal("30000"));
        Account karimAccount = new Account(391, "Karim", new BigDecimal("0"));

//        nayemAccount.deposit(333); This is how it should have been. so follow this and implement open/closed principle

        sonaliBank.executeOperation(new Deposit(nayemAccount, new BigDecimal("1000.99"))); // executeOperation method ta Bank class e die, ei line er moto korleo hoy
                                                                    // abar direct main class e Bank er instance create kore korleo hoy.

        System.out.println(nayemAccount.getBalance());

    }
} 


package com.nayemtech;

import java.util.ArrayList;
import java.util.List;

public class Bank {
    private List<Account> accountList;

    public Bank() {
        List<Account> accountList = new ArrayList<>();
    }

    public void executeOperation(AccountOperation accountOperation) {
//        deposit.execute() //this is how it should have been before.
        accountOperation.execute();
    }
} 

package com.nayemtech;

import java.math.BigDecimal;

public class Account {
    private int accountNumber;
    private String customerName;
    private BigDecimal balance;

    public Account(int accountNumber, String customerName, BigDecimal balance) {
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.balance = balance;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }
}
package com.nayemtech;

import java.math.BigDecimal;

public interface package com.nayemtech;

import java.math.BigDecimal;

public class Deposit implements AccountOperation{
    private Account account;
    private BigDecimal amount;

    public Deposit(Account account, BigDecimal amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void execute() {
        account.setBalance(account.getBalance().add(amount));
    }
}
AccountOperation {
    void execute();
}



```

The primary difference between the `AccountOperation` interface and the `Deposit` class in the code you provided and the `AccountOperation` interface and the `DepositOperation` class in the modified code I presented earlier lies in the level of abstraction and generality.

Let's break down the differences:

### Your Code:

```java
package com.nayemtech;

import java.math.BigDecimal;

public interface AccountOperation {
    void execute();
}

package com.nayemtech;

import java.math.BigDecimal;

public class Deposit implements AccountOperation{
    private Account account;
    private BigDecimal amount;

    public Deposit(Account account, BigDecimal amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void execute() {
        account.setBalance(account.getBalance().add(amount));
    }
}
```

### Modified Code:

```java
public interface AccountOperation {
    void execute(Account account);
}

class DepositOperation implements AccountOperation {
    private BigDecimal amount;

    public DepositOperation(BigDecimal amount) {
        this.amount = amount;
    }

    @Override
    public void execute(Account account) {
        account.deposit(amount);
    }
}
```

### Key Differences:

1. **Scope of Operation:**
   
   - **Your Code (`Deposit`):** The `Deposit` class is specifically designed for deposit operations. It directly manipulates the balance of the associated `Account` instance.
   - **Modified Code (`DepositOperation`):** The `DepositOperation` class is more generic and abstract. It represents a deposit operation but does not directly manipulate the `Account` details. Instead, it delegates the actual operation to the `Account` class through the `deposit` method.

2. **Dependency Injection:**
   
   - **Your Code (`Deposit`):** The `Deposit` class takes an `Account` instance and an amount as constructor parameters. It assumes that the `Account` is already created.
   - **Modified Code (`DepositOperation`):** The `DepositOperation` class takes only the amount as a parameter and expects an `Account` to be provided when the operation is executed. This allows for more flexibility in managing dependencies.

3. **Encapsulation:**
   
   - **Your Code (`Deposit`):** Directly accesses and modifies the `Account`'s balance property.
   - **Modified Code (`DepositOperation`):** Uses the `deposit` method of the `Account` class, encapsulating the logic within the `Account` class itself.

### When to Use Which Approach:

- **Your Code (`Deposit`):**
  
  - Use when you have a specific operation with complex logic tied directly to the operation itself.
  - Useful if the operation requires access to multiple properties or methods of the associated objects.

- **Modified Code (`DepositOperation`):**
  
  - Use when you want a more generic and abstract representation of an operation.
  - Helpful when you have multiple operations that can be executed on different types of objects (not limited to `Account` instances).

Both approaches are valid, and the choice depends on the specific requirements and design goals of your application. If you anticipate having various operations that involve different objects, the modified code's approach might offer more flexibility and scalability. If your operations are more tightly coupled to specific objects, the approach in your code may be appropriate.

------

# Q.9: Write a Java program to create a class called "Employee" with a name, salary, and hire date attributes, and a method to calculate years of service.

```java
package com.nayemtech;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        LocalDateTime hireDate = LocalDateTime.of(2017, 12, 30, 2, 30);
        Employee Karim = new Employee("Karim", 50000, hireDate);
        System.out.println(Karim.calculateYearsOfService());
    }
} 

package com.nayemtech;

import java.time.Duration;
import java.time.LocalDateTime;

public class Employee {
    private String name;
    private double salary;
    private LocalDateTime hireDate;

    public Employee(String name, double salary, LocalDateTime hireDate) {
        this.name = name;
        this.salary = salary;
        this.hireDate = hireDate;
    }
    public long calculateYearsOfService() {
        LocalDateTime curTime = LocalDateTime.now();
        Duration duration = Duration.between(hireDate, curTime);
        return duration.toDays()/365;
    }
}

```

--------
