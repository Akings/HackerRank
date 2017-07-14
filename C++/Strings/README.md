# Strings

## Strings

C++ provides a nice alternative data type to manipulate strings, and the data type is conveniently called string. Some of its widely used features are the following:

-   *Declaration:*
```C++
string a = "abc";
```

-   *Size:*
```C++
int len = a.size();
```

-  *Concatenate two strings:*
```C++
string a = "abc";
string b = "def";
string c = a + b; // c = "abcdef".
```

-   *Accessing i-th element:*
```C++
string s = "abc";
char   c0 = s[0];   // c0 = 'a'
char   c1 = s[1];   // c1 = 'b'
char   c2 = s[2];   // c2 = 'c'
s[0] = 'z';         // s = "zbc"
```

*P.S.:* We will use `cin`/`cout` to read/write a string.

### Input Format

You are given two strings, a and b, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').

### Output Format

In the first line print two space-separated integers, representing the length of *a* and *b* respectively.

In the second line print the string produced by concatenating *a* and *b* (*a+b*).

In the third line print two strings separated by a space, *a\`* and *b\'*. *a\'* and *b\'* are the same as *a* and *b*, respectively, except that their first characters are swapped.

### Sample Input

```C++
abcd
ef
```

### Sample Output

```C++
4 2
abcdef
ebcd af
```

### Explanation
-   *a* = `"abcd"`
-   *b* = `"ef"`
-   *|a|* = `4`
-   *|b|* = `2`
-   *a\'* = `"ebcd"`
-   *b\'* = `"af"`

## StringStream

`stringstream` is a stream class to operate on strings. It basically implements input/output operations on memory (string) based streams. `stringstream` can be helpful in different type of parsing. The following operators/functions are commonly used here

-   Operator `>>` Extracts formatted data.
-   Operator `<<` Inserts formatted data.
-   Method `str()` Gets the contents of underlying string device object.
-   Method `str(string)` Sets the contents of underlying string device object.

Its header file is `sstream`.

One common use of this class is to parse comma-separated integers from a string (e.g., `"23,4,56"`).

```C++
stringstream ss("23,4,56");
char ch;
int a, b, c;
ss >> a >> ch >> b >> ch >> c;  // a = 23, b = 4, c = 56
```

You have to complete the function ```vector parseInts(string str)```. `str` will be a string consisting of comma-separated integers, and you have to return a vector of `int` representing the integers.

**Note** If you want to know how to push elements in a vector, solve the first problem in the STL chapter.

### Input Format

The first and only line consists of n integers separated by commas.

### Output Format

Print the integers after parsing it.

*P.S.:* I/O will be automatically handled. You need to complete the function only.

### Sample Input

```
23,4,56
```

### Sample Output

```
23
4
56
```
