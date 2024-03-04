# Linked List

### Advantages:

1. lots of insertions and deletions

2. combining linked lists: a linked list with huge amounts of nodes can be added to another large linked list with only O(1) time complexity (in constant time)

3. same as above, splitting and creatng many separate linked list in constant time.

### Disadvantage:

1. can not access elements in middle of the list in constant time (can not access by index like arrays)

2. takes more memory as it needs to add the next pointers along with the value

# Regex

```tex
why doesn't it match for     string s1 = "Mr Karim Mia";
regex pattern("(Mr|Mr.|Mrs|Mrs.|Ms.|Ms)[A-Z]{1}[a-z][ A-z]?[a-z]*");
```

The regular expression pattern you provided is not matching the string “Mr Karim Mia” because of the following reasons:

1. The pattern `(Mr|Mr.|Mrs|Mrs.|Ms.|Ms)` is looking for titles with or without a period (.) after them. This part matches with “Mr” in your string.

2. The next part `[A-Z]{1}` is looking for exactly one uppercase letter, which doesn’t match with the space character after “Mr” in your string.

3. The part `[a-z]` is looking for exactly one lowercase letter, which doesn’t match with “Karim Mia” in your string.

4. The part `[ A-z]?` is looking for zero or one occurrence of a space character or any letter (upper or lower case), which doesn’t match with “Karim Mia” in your string.

5. The last part `[a-z]*` is looking for zero or more lowercase letters, which doesn’t match with “Karim Mia” in your string.

To match the string “Mr Karim Mia”, you can modify your regular expression to something like this:

```cpp
regex pattern("(Mr|Mr.|Mrs|Mrs.|Ms.|Ms)\\s[A-Z][a-z]*\\s[A-Z][a-z]*");
```

This pattern will match a title (with or without a period), followed by a space, then a word starting with an uppercase letter and followed by any number of lowercase letters, another space, and another word starting with an uppercase letter and followed by any number of lowercase letters. This should match names in the format “Title Firstname Lastname”. Please note the double backslash `\\` before `s` is used to escape the backslash in C++. In other languages, you might only need a single backslash.

Remember, regular expressions are very powerful, but they can also be quite complex and tricky to get right. It’s always a good idea to test your patterns thoroughly to make sure they’re working as expected.

```tex
will the above regex also work for Mr Karim
```

The provided regular expression `(Mr|Mr.|Mrs|Mrs.|Ms.|Ms)\\s[A-Z][a-z]*\\s[A-Z][a-z]*` expects a title, followed by a space, a capitalized word, another space, and another capitalized word. Therefore, it would not match “Mr Karim” because there’s no second capitalized word.

If you want to match names that may or may not have a last name, you can modify the regular expression to make the last name optional:

```cpp
regex pattern("(Mr|Mr.|Mrs|Mrs.|Ms.|Ms)\\s[A-Z][a-z]*(\\s[A-Z][a-z]*)?");
```

In this pattern, `(\\s[A-Z][a-z]*)?` makes the last name optional. This pattern will match both “Mr Karim” and “Mr Karim Mia”.

## Validating IP Address

If you want to match numbers between 0 and 255 with no leading zeros, you can modify the regular expression as follows:

```c
regex pattern("^([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0)$");
```

Here’s how it works:

- `[1-9][0-9]?` matches any number between 1 and 99.
- `1[0-9]{2}` matches any number between 100 and 199.
- `2[0-4][0-9]` matches any number between 200 and 249.
- `25[0-5]` matches any number between 250 and 255.
- `0` matches the number 0.

This pattern will match any number between 0 and 255 without leading zeros. I hope this helps! Let me know if you have any other questions. 😊

---------

```c
will it work?


    string s1 = "192.168.1.1";
    string s2 = "192.168.1.0";

    string s3 = "192.168.01.1";
    string s4 = "192.168.1.00";
    string s5 = "192.168@1.1";

    // regex pattern("(0|[1-9][0-9]?[0-9]?).[1-9][0-9]?[0-9]?.[1-9][0-9]?[0-9]?.[1-9][0-9]?[0-9]?");
    regex pattern("(0|[1-9][0-9]?[0-9]?)\\.(0|[1-9][0-9]?[0-9]?)\\.(0|[1-9][0-9]?[0-9]?)\\.(0|[1-9][0-9]?[0-9]?)");

    vector<string> store{s1,s2,s3,s4,s5};
    for (int i = 0; i < (int)store.size(); i++) {
        bool isMatch = regex_match(store[i], pattern);
        cerr << store[i] << " ----- "<< isMatch<< endl;
    }
```

The regular expression you provided will not work as expected for validating IP addresses. Here’s why:

- The expression `[1-9][0-9]?[0-9]?` will match numbers from 1 to 999, which is outside the valid range for an IP address octet (0-255).

# SDLC:

[Everything You Need to Know About SDLC - Bleuwire](https://bleuwire.com/everything-need-to-know-about-sdlc/)

- **<u>Planning & Analysis:</u>** This is the initial stage where you gather business requirements, set goals, identify risks, and evaluate the feasibility of creating the product.

- **<u>Feasibility Study:</u>**  In this stage, you assess the practicality of the proposed project.

- **<u>Design:</u>** This stage involves organizing the ideas into a cohesive plan and design.

- **<u>Building / Coding or Implementation:</u>** This is where the actual coding of the software takes place.

- **<u>Testing: </u>** The software is tested to ensure it works as expected.

- **<u>Installation/Deployment:</u>** The software is deployed to the users.

- **<u>Maintenance:</u>** After deployment, the software is maintained to fix bugs and implement updates.

# Backtracking

```c
which of these two codes is backtracking?
first code:
void rec(string s, int indxS, string& new_s) {
    if (indxS >= (int)s.length()) return;

    if (s[indxS] >= 'A' && s[indxS] <= 'Z') {
        s[indxS] += 32;
    }

    if (s[indxS] == 'a' || s[indxS] == 'e' || s[indxS] == 'i' || s[indxS] == 'o' || s[indxS] == 'u' || 
            (s[indxS] >= '0' && s[indxS] <= '9')) {
        //nothing.
    } else {
        if (s[indxS] >= 'a' && s[indxS] <= 'z') {
            s[indxS] -= 32;
        }
        new_s += "*";
        new_s += s[indxS];
    }

    rec(s, indxS+1, new_s);
}


second code:
void rec(string s, int indxS, string& new_s) {
    if (indxS >= (int)s.length()) return;
    rec(s, indxS+1, new_s);

    if (s[indxS] >= 'A' && s[indxS] <= 'Z') {
        s[indxS] += 32;
    }

    if (s[indxS] == 'a' || s[indxS] == 'e' || s[indxS] == 'i' || s[indxS] == 'o' || s[indxS] == 'u' || 
            (s[indxS] >= '0' && s[indxS] <= '9')) {
        //nothing.
    } else {
        if (s[indxS] >= 'a' && s[indxS] <= 'z') {
            s[indxS] -= 32;
        }
        new_s += "*";
        new_s += s[indxS];
    }
}
```

Both of these codes use recursion, but neither of them is using backtracking in the traditional sense.

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be extended to a valid solution.

The difference between these two codes is the order of operations:

- The **first code** processes the current character and then makes the recursive call.
- The **second code** makes the recursive call first and then processes the current character.

However, neither of these codes “backtracks” or undoes the changes it made during the recursive call. They simply process the characters in a different order. Therefore, neither of these codes is a backtracking algorithm. They are both examples of simple recursive functions.

- ***<u>make it backtracking then</u>***

Sure, here’s an example of a backtracking algorithm. This is a simple permutation generator, which is a common use case for backtracking:

```c
void permute(string s, int l, int r) {
    if (l == r)
        cout << s << endl;
    else {
        for (int i = l; i <= r; i++) {
            swap(s[l], s[i]);  // make a choice
            permute(s, l+1, r);  // explore the choice
            swap(s[l], s[i]);  // undo the choice for the next iteration, this is the backtracking step
        }
    }
}
```

In this code, we’re generating all permutations of a string. We make a choice by swapping two characters, then we recursively explore all permutations with this choice made. After we’re done exploring, we undo the choice (swap the characters back), which is the backtracking step. This allows us to explore all other permutations in subsequent recursive calls. This is a classic example of a backtracking algorithm.

Please note that this is a different problem than the one solved by your original code. The concept of backtracking doesn’t apply to the problem your original code is solving. Backtracking is typically used in problems where you need to find all solutions, or find an optimal solution, and making a wrong choice along the way can be corrected by ‘backtracking’ and making a different choice. Your original code is simply processing each character in a string, which doesn’t involve making choices that could be ‘wrong’ or ‘right’. Therefore, it doesn’t make sense to apply backtracking to this problem. If you have a different problem in mind where backtracking could be applied, please let me know and I’d be happy to help with that!

-------

-------

------

# what is null?

In Java, `null` is a special value that represents the absence of a value or object reference. It’s not the same as an empty string (`""`) or zero. It’s a literal that can be used as a value for any reference type. Here’s how you might explain it:

1. **Literal Value**: `null` is a literal in Java, similar to `true` and `false` which are literals for boolean.

2. **Default Value**: `null` is the default value of any reference type variable in Java. For example, if you declare a variable of type `Object` but do not create an object and assign it to the variable, the variable will have the value `null`.

3. **Represents Absence**: `null` represents the absence of a value or object reference. It’s not equivalent to zero or an empty string.

4. **NullPointerException**: If you try to call a method or access a property on a `null` object, Java will throw a `NullPointerException`. This is a runtime exception that often indicates a programming error.

5. **Useful for Garbage Collection**: `null` can be used to make an object eligible for garbage collection. If you set an object reference to `null`, there are no more references to the object, and the Java garbage collector can reclaim the memory.

Remember, understanding `null` and how to handle it is crucial to avoiding common pitfalls and writing robust Java code.

------------

- ekta graph e highest n^2 ta edge possible. (sobar shathe sobar edge ase)

- dijkstra complexity: (n+m logn) ... worst case m = n^2 ... so worst case n^2 logn

# what is a skewed tree?

- A skewed tree is a binary tree where each node has only one child node or none.

# Adjacency List VS Adjacency Matrix

<style>
 table {
 border: 1px solid #c4c7c5;
 border-radius: 4px;
 font-size: 16px;
 }
 th {
 padding: 18px 16px;
 text-align: left;
 }
 td {
 padding: 16px;
 border-top: 1px solid #c4c7c5;
 }
 button.js-code-copy {
 display: none;
 }
 .katex-mathml{
 display: block;
 text-align: center;
 }
 .katex-html {
 display: none;
 }

</style>

Sure, let’s compare the time and space complexity of adjacency list and adjacency matrix in graph traversal:

**Adjacency Matrix**:

- **Space Complexity**: An adjacency matrix requires `O(n^2)` space, where `n` is the number of nodes. [This is because it keeps a value (1/0) for every pair of nodes, whether the edge exists or not](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[1](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[2](https://stackoverflow.com/questions/32608288/time-space-complexity-of-adjacency-matrix-and-adjacency-list).
- **Time Complexity**: The time complexity to build such a matrix is `O(n^2)`. [To check if there exists an edge between any two nodes, it takes `O(1)` time](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[1](https://www.baeldung.com/cs/adjacency-matrix-list-complexity).
- [**Pros**: Fast to lookup and check for the presence or absence of a specific edge between any two nodes](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c)[3](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c).
- **Cons**: Requires more space, especially if the graph is sparse (i.e., has fewer edges). [It is also slow to iterate over all edges](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[3](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c).

**Adjacency List**:

- **Space Complexity**: An adjacency list is more space-efficient, especially for sparse graphs. [It only contains existing edges, so its length is at most the number of edges](https://stackoverflow.com/questions/32608288/time-space-complexity-of-adjacency-matrix-and-adjacency-list)[2](https://stackoverflow.com/questions/32608288/time-space-complexity-of-adjacency-matrix-and-adjacency-list).
- **Time Complexity**: The time complexity to build an adjacency list is `O(m + n)`, where `m` is the number of edges and `n` is the number of nodes. [To find the presence or absence of a specific edge between any two nodes, it takes `O(k)` time, where `k` is the number of neighbor nodes](https://stackoverflow.com/questions/23925009/why-does-the-time-complexity-of-dfs-and-bfs-depend-on-the-way-the-graph-is-repre)[4](https://stackoverflow.com/questions/23925009/why-does-the-time-complexity-of-dfs-and-bfs-depend-on-the-way-the-graph-is-repre).
- **Pros**: Fast to iterate over all edges. [More space-efficient for sparse graphs](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[3](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c).
- [**Cons**: Slightly slower than the adjacency matrix to check for the presence or absence of a specific edge between any two nodes](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c)[3](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c).

[In conclusion, the choice between an adjacency list and an adjacency matrix depends on the specific requirements of your problem, such as whether the graph is sparse or dense, and whether you need to frequently check for the existence of edges](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[1](https://www.baeldung.com/cs/adjacency-matrix-list-complexity)[3](https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c)[5](https://www.baeldung.com/cs/graph-adjacency-and-incidence). I hope this helps! Let me know if you have any other questions. 😊
