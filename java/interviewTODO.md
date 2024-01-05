1. ask chatGPT to give you interview oop questions also to give you something to implement with oop that would cover most oop interview questions basics and help to become fluent with oop

2. what is std:: in C++?

3. I know stuff like static keyword, when to use and not to use, but I better learn some characteristics (for example, you can call that static method from any other class without creating any instance) - review such characteristics for other java and oop stuffs

4. LinkedList

5. SDLC

6. bitwise operators

7. Heap

8. file read/write

9. why software engineer?

10. what is backwards compatibility api or code? (amigoscode: interface with default keyword and then override the method of default keyword in the implemented classes if necessary)

11. singly/ single directional linked list reverse order e print korte hobe konorokom data structure chara.

12. LinkedList **************

13. include namespace std; and :: operator

14. pass by reference and pass by value in both java and C++

15. OOP
    
    * Difference Between Interface and class?
    
    * jekono ekta class er modhe field declare korbo and then interface use korbo. Then why do I need interface? I can just use the class
    
    * so what is the difference between interface and abstract class? when should we use what?
    
    * amake polymorphism ta bujhayte parba?
    
    * polymorphism er ekta practical example deo.

16. Backend developer er ekta API call er whole lifecycle ta jana uchit. serokom ekta frontend/js developer er bolte hobe, js browser e kivabe run hoy? process ta ki?

17. probability

18. world e jokhon kono technology ashe, kono kisu solve korar jonnoi. so what problem react solved after it arrived?

19. why java then why spring boot?

20. why backend web development? why not mobile app or frontend or database etc.

21. company somporke search, company'r product somporke jana and linkedin e employee background check and kaoke jigges kora and reference if possible... company'r culture and company'r future nie idea.

22. sdlc ta rakute e kivabe manage korba? --- rakuten e waterfall follow kore.

23. put and patch er difference ki! put/patch etc er request status code, 

24. implement that list from this video https://youtu.be/Af3s3KsxStY?list=PL_c9BZzLwBRLW7Kw8bqc_PJqAnjCJI63P

```java
ArrayList<User> users = new ArrayList<User>();
List<User> users = new ArrayList<User>(); // does ArrayList implements list?
                                    //so that we can use it like this line?
                                  //I'm talking about List being the Super class
                                //and ArrayList extends List
```

23. Git and Github
24. default method and static method. what are they again? they are declared in interfaces.
25. class within a class in java
26. lambda expression .. stream loop .. for each type er loop
27. comparable<Integer>
28. List<Integer> or List<int> ? which is correct and why
29. java essentials course from amigos (teaches about generics and methods, return types,  of java and stuff)
30. java streams course from amigos (functional programming in java, streams etc.)
31. Number is an abstract class in java. Search for why Number is an abstract class in java to know better about abstract classes.
32. streams is part of functional programming
33. diff between jar and war
34. What is a java class file?
* A Java class file is a file (with the .class filename extension) containing Java bytecode that can be executed on the Java Virtual Machine (JVM). A Java class file is usually produced by a Java compiler from Java programming language source files (.java files) containing Java classes (alternatively, other JVM languages can also be used to create class files).
35. <u>*class inside a class:*</u>

```java
public class Main {

    // Outer class (Main class) members and methods

    // Inner class
    class InnerClass {
        // Inner class members and methods

        void display() {
            System.out.println("Inside InnerClass");
        }
    }

    public static void main(String[] args) {
        // Creating an instance of the outer class
        Main outerObj = new Main();

        // Creating an instance of the inner class
        InnerClass innerObj = outerObj.new InnerClass();

        // Calling a method of the inner class
        innerObj.display();
    }
}
```

* Another example is given below. Here, even though the attribute name and price of Vehicle class is  private, I can directly access these fields from the Main class because Vehicle is a nested class of Main class.

```java
package com.nayemtech;

public class Main {
    public static void main(String[] args) {
        Person Rahim = new Person("Rahim", 23);
        Person Karim = new Person("Karim", 33);

        System.out.println(Rahim.getName() + " " + Rahim.getAge());
        System.out.println(Karim.getName() + " " + Karim.getAge());

        Main main = new Main();
        Vehicle car = main.new Vehicle("Audi", 34000);
        System.out.println(car.name);
    }

    public class Vehicle {
        private String name;
        private int price;

        public Vehicle(String name, int price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }
        public int getPrice() {
            return price;
        }
    }
}
```

* Even deeper Nested class:

```java
package com.nayemtech;

public class Main {

    // Outer class (Main class) members and methods

    // Inner class
    class InnerClass {
        // Inner class members and methods

        void display() {
            System.out.println("Inside InnerClass");

            // Creating an instance of the nested class
            NestedClass nestedObj = new NestedClass();
            nestedObj.show();
        }

        // Nested class inside InnerClass
        class NestedClass {
            // Nested class members and methods

            void show() {
                System.out.println("Inside NestedClass");
            }
        }
    }

    public static void main(String[] args) {
        // Creating an instance of the outer class
        Main outerObj = new Main();

        // Creating an instance of the inner class
        InnerClass innerObj = outerObj.new InnerClass();

        // Calling a method of the inner class, which in turn calls a method of the nested class
        innerObj.display();
    }
}
```

* Inner class accessing outer class's attributes and methods:

```java
public class Main {

    private int outerVariable = 10;

    // Outer class method
    public void outerMethod() {
        System.out.println("Outer method: " + outerVariable);
    }

    // Inner class
    class InnerClass {
        private int innerVariable = 20;

        // Inner class method accessing outer class members
        public void innerMethod() {
            System.out.println("Inner method: " + outerVariable); // Accessing outer class variable
            outerMethod(); // Accessing outer class method
            System.out.println("Inner variable: " + innerVariable);
        }
    }

    public static void main(String[] args) {
        // Creating an instance of the outer class
        Main outerObj = new Main();

        // Creating an instance of the inner class
        InnerClass innerObj = outerObj.new InnerClass();

        // Calling the inner class method
        innerObj.innerMethod();
    }
}
```

* Inner classes are not visible outside of their containing class, which can limit their reuse in other parts of the code.
36. Tightly coupled vs losely coupled. When is a code tightly coupled? What happens when tightly coupled? ************

37. Palindrome problems

38. # Validating Indian vehicle number plate using Regular Expression

39. Design database schema like japanese e commerce ******

40. nested class nie ektu interview question ghataghati kora lagbe ****

41. nested method? ****

42. 
