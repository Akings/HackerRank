# Warmup

## Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).

Your task is to find their comparison points by comparing a0 with b0, a1 with b1, and a2 with b2.

-   If ai > bi, then Alice is awarded 1 point.
-   If ai < bi, then Bob is awarded 1 point.
-   If ai = bi, then neither person receives a point.

Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective comparison points?

### Input Format

The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective values in triplet A.
The second line contains  space-separated integers, b0, b1, and b2, describing the respective values in triplet B.

### Constraints

-   1 <= ai <= 100
-   1 <= bi <= 100

### Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

### Sample Input

```shell
5 6 7
3 6 10
```

### Sample Output

```shell
1 1
```

### Explanation

In this example:

-   A = (a0, a1, a2) = (5, 6, 7)
-   B = (b0, b1, b2) = (3, 6, 10)

Now, let's compare each individual score:

-   a0 > b0, so Alice receives 1 point.
-   a1 = b1, so nobody receives a point.
-   a2 < b2, so Bob receives 1 point.
Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we print `1 1` (Alice's comparison score followed by Bob's comparison score) on a single line.

## Mini-Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

### Input Format

A single line of five space-separated integers.

### Constraints

Each integer is in the inclusive range \[1, 10^9\].

### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

### Sample Input

```shell
1 2 3 4 5
```
### Sample Output

```shell
10 14
```

### Explanation

Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the following sums using four of the five integers:

0.  If we sum everything except 1, our sum is 2+3+4+5 = 14.
0.  If we sum everything except 2, our sum is 1+3+4+5 = 13.
0.  If we sum everything except 3, our sum is 1+2+4+5 = 12.
0.  If we sum everything except 4, our sum is 1+2+3+5 = 11.
0.  If we sum everything except 5, our sum is 1+2+3+4 = 10.

As you can see, the minimal sum is 10 and the maximal sum is 14. Thus, we print these minimal and maximal sums as two space-separated integers on a new line.

**Hints:** Beware of integer overflow! Use 64-bit Integer.

## Birthday Cake Candles

Colleen is turning n years old! Therefore, she has n candles of various heights on her cake, and candle i has height height\[i]. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height\[i] for each individual candle, find and print the number of candles she can successfully blow out.

### Input Format

The first line contains a single integer, n, denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer i describes the height of candle i.

### Constraints

-   1 <= n <= 10^5
-   1 <= height[i] <= 10^7

### Output Format

Print the number of candles Colleen blows out on a new line.

### Sample Input 0

```shell
4
3 2 1 3
```

### Sample Output 0

```shell
2
```

### Explanation 0

We have one candle of height , one candle of height , and two candles of height . Colleen only blows out the tallest candles, meaning the candles where . Because there are  such candles, we print  on a new line.
