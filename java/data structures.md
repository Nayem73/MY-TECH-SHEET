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

# SDLC:

- [Everything You Need to Know About SDLC - Bleuwire](https://bleuwire.com/everything-need-to-know-about-sdlc/)

- Planning

- Design

- Building

- Testing

- Deployment

- Maintenance (Added by me)

# Backtracking

```cpp
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

```cpp
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
