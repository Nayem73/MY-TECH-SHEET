### In Java, everything is an Object !!!!!!!!!!

1.
 compiler vs interpreter: python is an interpreter language while C++ is
 compiled language. compile korle ki hoy? puro code ekbare compile/run 
hoy. but enterpreter is like python e jemon line by line execute kora 
jay jupyter e oirokom.  
2. So, for python and JS, when you run your 
code, it does not need to be compiled. so it is dynamic type checking 
and java and C++ are static type checking.  
3. A language is 
statically-typed if the type of a variable is known at compile time 
instead at run time. This allows many type-errors to be caught before 
running the code.  
4. A Java class file is a file (with the . class 
filename extension) containing Java bytecode that can be executed on the
 Java Virtual Machine (JVM).  
5. by compiling and running the code , it generates a main.class in out folder.  
6. public static void main << this method is must. but public class Main can be changed to other names.  
7.
 primitive data types and reference data types in java. when we want to 
store simple values, we use primitive data types. like int num = 5; but 
when we want to store complex values, reference types and objects come 
into play.  
8. Point pointA = new Point(2,5); pointA here is an object which is a reference type.  
9. Heap:  

- Space is used to store objects and JRE classes at runtime.  

- New objects are always created in heap space.  

- References to these objects are store in Stack memory.  
10. Stack memory:  
- Stack memory in java is used for static memory allocation and the execution of a thread LIFO.  

- Frame (stack frame) contains all the data for one function call.  

10.

11. java is always pass by 
    value. No pass by reference. primitive type er jonno o pass by value, 
    Reference type er jonno o pass by value.  

12. All the instruction 
    written in a Dockerfile are instructions to docker for setting up the 
    image. Now keep in mind, the image is the template for the container. 
    The image is what you don't run in the end, You run a container based on
    a image.  

13. for primitives, default values are 0 and for Reference types, default value is null  

14. 

15. static keyword before any method or attribute means it belongs to the class and not the instance itself.  

16. static means no need to create an instance of that class. the static method can be invoked directly.  

17. 

18. enums in java:  
    enum Gender {  
    MALE,  
    FEMALE  
    }  

** Also just like creating class, in intellij you get to select enums:  
public enum Gender {  
MALE,  
FEMALE  
}  

final keyword use na kore enum use korar reason holo ei same type er constant gulo ekta group e rakha jasse  

19.
 Each of the primitives(int, float .. ) there is a corresponding Wrapper
 class. the Wrapper class allows us to use the corresponding primitives 
as object. (need to touch on generics in amigos video for more)  

- by 
  using the object (i mean Wrapper class like Integer) you get a bunch of 
  functionalities for example: int n = Integer.min(5,6) ... int n = 
  Integer.ParseInt(someString) ... String s = Integer.toString(55); .. and
  more.  
20. String literals vs String objects  

21. String 
    formattedString = String.format("like printing Strings in C & extra 
    feature: numToString=%s, num=%s\n", numToString, num);  

22. for money, never use double.  

23. Throwable is a superclass of all types of Errors and Exceptions.  

24. so, Error and Exception are the subclass of Throwable  

25. 

26. Object -> Throwable -> Exception -> RuntimeException  

27. checked exception = compile time exception  

28. unchecked exception = runtime exception  

------------------------------------

29. <mark>Checked Exception</mark> and <mark>Unchecked Exception</mark> causing trouble.

30. below code shows error during compile because Exception << this is checked exception meaning compile time exception

```java
package com.nayemtech;

public class Main {
    public static void main(String[] args) {
        neg(3, 10);
    }

    public static void neg(int a, int b) throws Exception {
        if (b >= a) {
            throw new Exception("can not subtract b from a because b is bigger than a");
        }

        a -= b;
        System.out.println(a);
    }
}
```

but to fix above checked Exception we need to use:

- try catch block

- throws keyword in the method signature

we already got the throws keyword . now we need try catch:

```java
package com.nayemtech;

public class Main {
    public static void main(String[] args) {
        try {
            neg(3, 10);
        } catch (Exception e) {
            System.out.println("Exception caught: " + e.getMessage());
        }
    }

    public static void neg(int a, int b) throws Exception {
        if (b >= a) {
            throw new Exception("Can not subtract b from a because b is bigger than a");
        }

        a -= b;
        System.out.println(a);
    }
}

```

so this works.

31. dfdf
