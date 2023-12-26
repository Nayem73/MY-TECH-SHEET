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
