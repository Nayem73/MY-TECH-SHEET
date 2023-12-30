* Class Initialize korar jonno oi class er constructor call kora lage. for example:
  
  * ```java
    Car car = new Car(); //init by empty constructor
    Animal animal = new Animal("Dog", "brown", 2); //init by constructor with parameters
    ```

## java will force you to find entities which will have attributes and behaviours. That entity will be a java class.

class is a blueprint of an object which brings the question as what is object an object is basically an instance of the class.

a class is technically a logical entity

We can think of class as an entity in the world. we say that java is heavily inspired from real life examples and classes and objects are the reason we say that because whatever you see in the world is always basically

some entity - human beings are an entity, cars are an entity, students are an entity ,so all the actors which we see in the world are basically entities and we can map them as classes.

in java why do we want to map them - because these entities have basically

two kind of specifications - Every entity will have some attributes and it will have some behavior and actually that is how you identify an entity for example human

beings have attributes like we have hands we have eyes we have ears legs etc

these are our attributes. Then we have our behaviors. Behaviors are actions. Human being can speak so speaking is an action - it's abehavior. 

they can listen - is an action, it's a behavior. Can walk is an action is a behavior

similarly can eat is also an action or a behavior so that's how you basically represent an entity.

<u>*Entities have attributes and behaviors. if we see those two specifications in any entity we can map that entity or  write that enity as a class because a class in java - Will exactly have these two properties it will have some attributes which are called fields or member variables and it will have some behaviors which are called as methods so it will have attributes and behaviours similar to real-world entity*</u>

Together, the methods and fields of a class are commonly referred to as its members. Members encapsulate the behavior (methods) and state (fields) of the class. So, when discussing the components that make up a class in Java, you can use the term "class members" to encompass both methods and fields.

## why do we need it?

when a client provides me his requirements for a particular project, I will be able to identify the attributes and behaviors of the entities of that project and able to create classes according to the requirements. Thats how I would be able to transfer the real world requirements of a project into code.

# inside a class

* how do you initialize objects/attributes/fields in a classe? -> through setters and constructors.

## Access Modifiers

![](assets/2023-12-26-17-00-56-image.png)

Access modifiers are used to only expose the attributes, methods and classes which are supposed to be exposed to the consumer.

# Inheritance

* When we have multiple classes to share similar behaviour(mehtods) and attributes(fields)

* For example, let's say we have banking system, we can have commercial account, personal account, loan account etc. In these classes, we have some common behavior but at the same time we also have some different behavior so whenever you have such scenario always think about applying the concept of inheritance.

* here's another simple way to spot whether inheritance can be used at a particular place or not: 
  
  Inheritance is also used when there's a relationship(relationship of a super class and subclass/'es) between two entities or classes. whenever you read the requirements from a client just try to find the words which use this particular phrase "is a"
  
  - for example car "is a" vehicle. 
  
  - savings account "is a" type of account.

# Encapsulation

* Encapsulation is basically to combine methods and attributes in a single unit, which is a class and protect  the attributes/properties of the class to the outside world(package) Which allows us to have full contol on how the outside world can access or modify the attributes.

* We have full control of the class:
  
  * We control the visibility/access of the attributes/fields
  
  * We control how they should be assigned through setters
  
  * We control how they should be accessed through getters

# Abstraction

* abstract classes cannot be instantiated explicitly. They can only be instantiated by the child classes through the internal mechanisms of java itself (inheritance)
* Abstraction is necessary when we want subclasses to inherit from a super class and when we only need the objects of those subclasses. For example, we make a generic class for all type of Vehicles as Vehicle and Car, Bike, CNG etc. will extend from that class and in such cases we will only work with these subclasses. So we make Vehicle as an abstract class.
* So why we make Vehicle as abstract? Of course we will have some common methods and attributes inside the Vehicle class that all Vehicle should have, for example each vehicle has tires, but the layout or number of tires can be different, so we have some common characteristics but we cannot implement the exact type. So we should declare a common method and let the sub classes override it and implement their own functionalities. This is where we need to make Abstract methods. And of course to achieve this functionality, to avoid code duplication and write better code, we need to make the parent class abstract as well, only then we can use abstract methods.

# Interface

- Interface defines the specifications or contract on how a class should act.

- A subclass can not have two superclasses in java. It can only be done through interface. 

- So, we say you cannot use multiple inheritance with classes in java - a child cannot have two parent or two base classes in java. It is also called the diamond problem because the child class does not know whether to follow the route of base-1 class or the base-2 class.

- To solve it, we need interfaces.

# Polymorphism

* Interface allows us to achieve Polymorphism.
* Polymorphism is a concept where we achieve different functionalities with a common code structure. For example, Interface allows us to achieve Polymorphism. What do we do in interface? We declare abstract methods in an interface and several other classes may implement that interface to override the methods. Here we see that same method, we achieve different functionalities in different classes based on implementation.
* Also, with Inheritance, we achieve similar results as we override the methods of the  super class in the base class as needed.
* Sometimes, we need to call same methods with different parameters - which we know as method overloading also achieves different functionalities with common code.
* Also, when we need to add two numbers, we use the + operator. And when we need to concatenate two strings, we also use + operator. - This is also another example where we achieve different functionalities with + operator in different scenarios.

**Interface allows us to achieve Polymorphism. - How?**

When we use interface, we declare abstract methods in it as necessary and when we implement that interface with different classes, we must override those abstract methods in the interface, achieving different functionalities as per our implementation.

# polymorphism example > shape interface

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
public interface Shape {
    double area();
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
