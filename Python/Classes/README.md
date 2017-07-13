# Classes

## Dealing with Complex Numbers

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

### Input Format

One line of input: The real and imaginary part of a number separated by a space.

### Output Format

For two complex numbers C and D, the output should be in the following sequence on separate lines:
-   C + D
-   C - D
-   C * D
-   C / D
-   mod(C)
-   mod(D)

For complex numbers with non-zero real(A) and complex part(B), the output should be in the following format:

*A + Bi*

Replace the plus symbol(+) with a minus symbol(-) when B < 0.

For complex numbers with a zero complex part i.e. real numbers, the output should be:

*A + 0.00i*

For complex numbers where the real part is zero and the complex part(B) is non-zero, the output should be:

*0.00 + Bi*

### Sample Input
```Python
2 1
5 6
```

### Sample Output
```Python
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
```
### Concept

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer [here](http://www.diveintopython3.net/iterators.html#defining-classes).

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

`__add__`-> Can be overloaded for + operation

`__sub__` -> Can be overloaded for - operation

`__mul__` -> Can be overloaded for * operation


For more information on operator overloading in Python, refer [here](http://docs.python.org/3.2/reference/datamodel.html).

## Find the Torsional Angle

You are given four points *A, B, C* and *D* in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points *A, B, C* and *B, C, D* in degrees(not radians). Let the angle be *PHI*.

*cos(PHI) = (X.Y)/|X||Y|* where *X = AB x BC* and *Y = BC x CD*.

Here, *X.Y* means the dot product of *X* and *Y*, and *AB x BC*  means the cross product of vectors *AB* and *BC*. Also, *AB = B - A*.

### Input Format

One line of input containing the space separated floating number values of the X, Y and Z coordinates of a point.

### Output Format

Output the angle correct up to two decimal places.

### Sample Input

```Python
0 4 5
1 7 6
0 5 9
1 7 2
```

### Sample Output

```Python
8.19
```
