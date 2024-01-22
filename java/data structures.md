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
