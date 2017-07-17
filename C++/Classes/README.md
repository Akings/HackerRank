# Classes

## Structs

`struct` is a way to combine multiple fields to represent a composite data structure, which further lays the foundation for Object Oriented Programming. For example, we can store details related to a student in a struct consisting of his age (`int`), first_name (`string`), last_name (`string`) and standard (`int`).

struct can be represented as

```C++
struct NewType {
    type1 value1;
    type2 value2;
    .
    .
    .
    typeN valueN;
};
```
You have to create a struct, named Student, representing the student's details, as mentioned above, and store the data of a student.

### Input Format

Input will consist of four lines.
The first line will contain an integer, representing age.
The second line will contain a string, consisting of lower-case Latin characters ('a'-'z'), representing the first_name of a student.
The third line will contain another string, consisting of lower-case Latin characters ('a'-'z'), representing the last_name of a student.
The fourth line will contain an integer, representing the standard of student.

*Note*: The number of characters in first_name and last_name will not exceed 50.

### Output Format

Output will be of a single line, consisting of age, first_name, last_name and standard, each separated by one white space.

P.S.: I/O will be handled by HackerRank.

### Sample Input

```C++
15
john
carmack
10
```

### Sample Output

```C++
15 john carmack 10
```

## Class

Classes in C++ are user defined types declared with keyword class that has data and functions . Although classes and structures have the same type of functionality, there are some basic differences. The data members of a class are private by default and the members of a structure are public by default. Along with storing multiple data in a common block, it also assigns some functions (known as methods) to manipulate/access them. It serves as the building block of Object Oriented Programming.

It also has access specifiers, which restrict the access of member elements. The primarily used ones are the following:

public: Public members (variables, methods) can be accessed from anywhere the code is visible.
private: Private members can be accessed only by other member functions, and it can not be accessed outside of class.
Class can be represented in the form of

```C++
class ClassName {
    access_specifier1:
        type1 val1;
        type2 val2;
        ret_type1 method1(type_arg1 arg1, type_arg2 arg2,...)
        ...
    access_specifier2:
        type3 val3;
        type4 val4;
        ret_type2 method2(type_arg3 arg3, type_arg4 arg4,...)
        ...
};
```

It's a common practice to make all variables private, and set/get them using public methods. For example:

```C++
class SampleClass {
    private:
        int val;
    public:
        void set(int a) {
            val = a;
        }
        int get() {
            return val;
        }
};
```

We can store details related to a student in a class consisting of his `age` (`int`), `first_name` (`string`), `last_name` (`string`) and `standard` (`int`).

You have to create a class, named `Student`, representing the student's details, as mentioned above, and store the data of a student. Create setter and getter functions for each element; that is, the class should at least have following functions:
-   `get_age`, `set_age`
-   `get_first_name`, `set_first_name`
-   `get_last_name`, `set_last_name`
-   `get_standard`, `set_standard`

Also, you have to create another method `to_string()` which returns the string consisting of the above elements, separated by a comma(,). You can refer to `stringstream` for this.

### Input Format

Input will consist of four lines.
The first line will contain an integer, representing the `age`. The second line will contain a string, consisting of lower-case Latin characters ('a'-'z'), representing the `first_name` of a student.
The third line will contain another string, consisting of lower-case Latin characters ('a'-'z'), representing the `last_name` of a student.
The fourth line will contain an integer, representing the `standard` of student.

*Note*: The number of characters in `first_name` and `last_name` will not exceed 50.

### Output Format

The code provided by HackerRank will use your class members to set and then get the elements of the Student class.

### Sample Input

```C++
15
john
carmack
10
```

### Sample Output

```C++
15
carmack, john
10

15,john,carmack,10
```

## Classes and Objects

A class defines a blueprint for an object. We use the same syntax to declare objects of a class as we use to declare variables of other basic types. For example:

```C++
Box box1;          // Declares variable box1 of type Box
Box box2;          // Declare variable box2 of type Box
```

Kristen is a contender for valedictorian of her high school. She wants to know how many students (if any) have scored higher than her in the  exams given during this semester.

Create a class named `Student` with the following specifications:

-   An instance variable named `scores` to hold a student's  exam scores.
-   A `void input()` function that reads  integers and saves them to `scores`.
-   An `int calculateTotalScore()` function that returns the sum of the student's scores.

### Input Format

Most of the input is handled for you by the locked code in the editor.

In the void `Student::input()` function, you must read 5 scores from stdin and save them to your instance variable.

### Constraints

-   1 <= n <= 100
-   0 <= examscore <= 50

### Output Format

In the `int Student::calculateTotalScore()` function, you must return the student's total grade (the sum of the values in `scores`).

The locked code in the editor will determine how many scores are larger than Kristen's and print that number to the console.

### Sample Input

The first line contains , the number of students in Kristen's class. The  subsequent lines contain each student's exam grades for this semester.

```
3
30 40 45 10 10
40 40 40 10 10
50 20 30 10 10
```

### Sample Output

```
1
```

### Explanation

Kristen's grades are on the first line of grades. Only 1 student scored higher than her.

## Box It!

Design a class named `Box` whose dimensions are integers and private to the class. The dimensions are labelled: length `l`, breadth `b`, and height `h`.

The default constructor of the class should initialize `l`, `b`, and `h` to 0.

The parameterized constructor `Box(int length, int breadth, int height)` should initialize Box's `l`, `b` and `h` to length, breadth and height.

The copy constructor `Box(Box B)` should set `l`, `b` and `h` to B's `l`, `b` and `h`, respectively.

Apart from the above, the class should have 4 functions:

-   `int getLength()` - Return box's length
-   `int getBreadth()` - Return box's breadth
-   `int getHeight()` - Return box's height
-   `long long CalculateVolume()` - Return the volume of the box

Overload the operator `<` for the class `Box`. `Box A` < `Box B` if:

0.  `A.l < B.l`
0.  `A.b < B.b` and `A.l == B.l`
0.  `A.h < B.h` and `A.b == B.b` and `A.l == B.l`

Overload operator `<<` for the class `Box()`.
If  is an object of class Box:

`cout << B` should print `B.l`, `B.b` and `B.h` on a single line separated by spaces.

### Constraints



Two boxes being compared using the  operator will not have all three dimensions equal.
