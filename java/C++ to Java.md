# 1. Vector in C++ to Java

1. convert below C++ code to Java:
   
   ```c
   #include <bits/stdc++.h>
   using namespace std;
   
   int main() {
       vector<int> v;
       v.push_back(45);
       v.push_back(34);
       v.pop_back();
       v.push_back(46);
   
       for (auto X: v) cout << X << ' ';
   }
   ```
   
   ```java
   import java.util.ArrayList;
   import java.util.List;
   
   public class Main {
       public static void main(String[] args) {
           List<Integer> v = new ArrayList<>();
           v.add(45);
           v.remove(v.size() - 1); //last index element
           v.add(34);
           v.remove(0); // Remove the first index element
           v.add(46);
   
           for (int X : v) {
               System.out.print(X + " ");
           }
       }
   }
   ```

```
```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> v = new ArrayList<Integer>();
        v.add(45);
        v.add(34);
        v.remove(v.size() - 1); //last index
        v.add(46);
        v.remove(0); // This line removes the first element
        for (int X : v) System.out.print(X + " ");
    }
}
```

# 2. Map

 In Java, you can’t use primitive types as generic arguments So, instead of `Map<int, int>`, you should use `Map<Integer, Integer>`.

# *. Print paragraphs which includes newline:

![](assets/2023-12-24-11-26-49-image.png)

# 3. Set

---------------------------

------------------

# Java Itself

* **To chatGPT:** why error in CalculateArea class? Explain with details and help me understand java in details with code.

```java
package com.nayemtech;

public interface Shape {
    double area();
}


package com.nayemtech;

public class Circle implements Shape {
    double radius;

//    public Circle() {
//    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(this.radius, 2);
    }
}


package com.nayemtech;

public class Triangle implements Shape {
    private double base;
    private double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    @Override
    public double area() {
        return 0.5 * this.base * this.height;
    }
}


package com.nayemtech;

import java.util.ArrayList;

public class CalculateArea {
    ArrayList<Shape> shapes = new ArrayList<>(Shape);
    Shape circle = new Circle(3);
    Shape circle2 = new Circle(5);
    Shape triangle = new Triangle(5, 7);

    shapes.add(circle);
    shapes.add(circl2);
    shapes.add(triangle);
}
```

**chatGPT:**

There are a couple of errors in your `CalculateArea` class. Let's go through them step by step:

1. **ArrayList Initialization:** The initialization of the `ArrayList` is incorrect. You need to specify the type of elements that the `ArrayList` will hold, but in your case, you are passing the `Shape` interface directly to the constructor. Instead, you should use diamond brackets (`<>`) to indicate the generic type.

```java
ArrayList<Shape> shapes = new ArrayList<>();
```

1. **Method Invocation:** The code that adds shapes to the `ArrayList` should be placed inside a method or a constructor. You cannot have statements like `shapes.add(...)` directly at the class level. Let's create a constructor for the `CalculateArea` class and move the shape initialization and addition logic into it.

```java
package com.nayemtech;

import java.util.ArrayList;

public class CalculateArea {
    private ArrayList<Shape> shapes = new ArrayList<>();

    public CalculateArea() {
        Shape circle = new Circle(3);
        Shape circle2 = new Circle(5);
        Shape triangle = new Triangle(5, 7);

        shapes.add(circle);
        shapes.add(circle2);
        shapes.add(triangle);
    }

    // Add any other methods if needed

    public static void main(String[] args) {
        // You can create an instance of CalculateArea here if needed
        // CalculateArea calculator = new CalculateArea();
    }
}
```

**Alhamdulillah** Now It works!

```java
package com.nayemtech;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>();
        Shape circle = new Circle(3);
        Shape circle2 = new Circle(5);
        Shape triangle = new Triangle(5, 7);

        shapes.add(circle);
        shapes.add(circle2);
        shapes.add(triangle);

        List<Shape> shapes2 = List.of(circle, triangle, circle2);

        CalculateArea calculateArea = new CalculateArea();
        System.out.println(calculateArea.totalArea(shapes));
        System.out.println(calculateArea.totalArea(shapes2));
    }
} 



package com.nayemtech;
import java.util.ArrayList;

public class CalculateArea {
    public double totalArea(List<Shape> shapes) { //using List works for ArrayList too
        double sum = 0;
        for (Shape X: shapes) {
            sum +=  X.area();
        }
        return sum;
    }
}


package com.nayemtech;

public class Circle implements Shape {
    double radius;

//    public Circle() {
//    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(this.radius, 2);
    }
}  

package com.nayemtech;

public class Triangle implements Shape {
    private double base;
    private double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    @Override
    public double area() {
        return 0.5 * this.base * this.height;
    }
}
```

# Final keyword

- The `Person` class has a `final` field called `name`. Once a `final` field is assigned a value in the constructor, it cannot be changed.
- The `performAction` method is declared as `final`, indicating that it cannot be overridden by subclasses.

```java
public class Person {
    // Instance variables
    private final String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter for the name field
    public String getName() {
        return name;
    }

    // Getter and setter for the age field
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // Method to display information about the person
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    // Example of a final method
    public final void performAction() {
        System.out.println(name + " is performing an action.");
    }

    // Example of a static method
    public static void staticMethod() {
        System.out.println("This is a static method.");
    }

    public static void main(String[] args) {
        // Create an instance of the Person class
        Person person1 = new Person("John", 25);

        // Display information using the displayInfo method
        person1.displayInfo();

        // Call the final method
        person1.performAction();

        // Call the static method using the class name
        Person.staticMethod();
    }
}
```

# Static keyword

* you can not use this keyword inside a static method because, `this` keyword refers to the current instance of the class, and it cannot be used inside a static method because static methods are associated with the class itself, not with a specific instance.

* Static methods are called on the class rather than an instance

### Useful Example(when to use Static): Utility Methods

Suppose you are working on a utility class that performs common mathematical operations. In this case, you might want to use static methods because these operations are not tied to a specific instance of the utility class.

```java
public class MathUtils {
    // Private constructor to prevent instantiation
    private MathUtils() {}

    // Static method for addition
    public static int add(int a, int b) {
        return a + b;
    }

    // Static method for multiplication
    public static int multiply(int a, int b) {
        return a * b;
    }
}

// Usage example
public class MathApp {
    public static void main(String[] args) {
        int sum = MathUtils.add(3, 5);
        System.out.println("Sum: " + sum);

        int product = MathUtils.multiply(4, 6);
        System.out.println("Product: " + product);
    }
}
```

In this example, the `MathUtils` class contains static methods for addition and multiplication. These methods can be used without creating an instance of the `MathUtils` class, making them convenient for general utility functions.

In this example, the `sqrt` and `cos` methods of the `Math` class are static, allowing you to use them without creating an instance of the `Math` class.

```java
public class MathExample {
    public static void main(String[] args) {
        // Using static methods from the Math class
        double squareRoot = Math.sqrt(25.0);
        System.out.println("Square root: " + squareRoot);

        double cosineValue = Math.cos(Math.PI);
        System.out.println("Cosine of PI: " + cosineValue);
    }
}
```

### How java itself uses static

The `Math` class in Java is a utility class that provides mathematical operations. The methods in the `Math` class are `static` because they perform generic mathematical operations and do not depend on maintaining state across instances.

### When Not to use static - Managing State

Suppose you have a `Counter` class that needs to keep track of the count for different instances. Using static for the counter might seem like a solution, but it has drawbacks, especially if you need multiple independent counters.

```java
public class Counter {
    private static int count = 0;

    public Counter() {
        count++;
    }

    public static int getCount() {
        return count;
    }
}

// Usage example
public class CounterApp {
    public static void main(String[] args) {
        Counter counter1 = new Counter();
        Counter counter2 = new Counter();

        System.out.println("Count: " + Counter.getCount()); // Output: 2
    }
}
```

Instead, A better approach for managing state in multiple instances would be to make the count instance-specific: (In this improved example, each instance of the `Counter` class maintains its own count.)

```java
public class Counter {
    private int count = 0;

    public Counter() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

// Usage example
public class CounterApp {
    public static void main(String[] args) {
        Counter counter1 = new Counter();
        Counter counter2 = new Counter();

        System.out.println("Count for counter1: " + counter1.getCount()); // Output: 1
        System.out.println("Count for counter2: " + counter2.getCount()); // Output: 1
    }
}
```

orthat, kono method/attribute er functionality jodi oi class er shokol instance er jonnoi eek e hoy, then we should use static.

### Summary

- **Use `static` when:**
  
  - You have utility methods that perform general operations and do not require an instance.
  - You want to provide convenient access to functionality without the need for object instantiation.

- **Avoid `static` when:**
  
  - You need instance-specific behavior or state.
  - There are modern alternatives available that encourage better practices (e.g., using the `java.time` package for date and time operations).

Java's standard libraries demonstrate a balance between static and non-static methods based on the intended use cases and design principles.
