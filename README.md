# prime-precision

[![CI](https://github.com/username/prime-precision/actions/workflows/ci.yml/badge.svg)](https://github.com/username/prime-precision/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Aim
I came up with three different algorithms for determining whether a number is
prime. The core of this project is to adopt different perspectives on a
problem, with each way of handling a problem will have pros or cons over
another.

# Algorithms
```
1. Exclude n if n<2. Now, find its square root, then use a for loop in the range
   between 2 and the square root + 1. If there is no number in the loop that is
   divisible by n, then n is prime.
2. Exclude n if it is less than or equal to 1.
      -   If it is equal to 2, it is prime.
      -   If n is greater than 2, use a for loop in the range between 2 and n,
          if there is not any number in the loop that is divisible by n, then n
          is prime.
3. Firstly, set an initial variable divisible equating to 0. Secondly, use a for
loop in the range between 1 and n+1; if any number in that loop is divisible by
n, add 1 to the variable divisible. When the loop is finished, if the variable
divisible is equal to 2 (means only 1 and n is divisible by n), then n is prime.
```

# Extended code to compare algorithms
In order to create a list of all prime numbers less than 10000 from those
defined functions, I first make an empty list, then use a for loop in the range
between 2 and 10000. If i fits the defined function, append i to that list. The
same procedure is done for all three algorithms. After having the list of all
prime numbers less than 10000, I slice it using the operator [n:m] to print the
first ten and the last 10 prime numbers of it.

I use the time module to measure the time taken to perform each function
(including determining if the number is prime, creating the list of all prime
numbers less than 10000 using the function, and printing the first and last ten
numbers of the list). Taking n = 9,999,999 as an example, function a takes 0.028
seconds, function b takes 0.6074 seconds, and function c takes over 7 seconds. 

Since function a works on the square root which greatly minimises the range of
the for loop, it takes by far the shortest time to run.

Since function a and function b are quite similar (they all use a for loop and
divides n by the number i from the loop), function b also takes less time (less
than 1 second). Nonetheless, as function a works on the square root of n, this
makes it considerably quicker than function b.

Lastly, function c takes the longest time (over nine seconds) because it takes
an additional step which is working with the variable 'divisible'. Thus, the
bigger the number n becomes (like 9,999,999), the longer the time taken.

# Sample Output
```
A program to check if a number is prime.
Return True if it is, False otherwise.
Also compares which function is the fastest.

Enter a number for evaluation: 9999999
-----------------------------------------------------------------------
9,999,999 is False
In a list of all prime numbers less than 10,000:
The first ten are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
The last ten are: [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
Function A: time taken = 0.028 seconds.
-----------------------------------------------------------------------
9,999,999 is False
In a list of all prime numbers less than 10,000:
The first ten are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
The last ten are: [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
Function B: time taken = 0.6074 seconds.
-----------------------------------------------------------------------
9,999,999 is False
In a list of all prime numbers less than 10,000:
The first ten are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
The last ten are: [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
Function C: time taken = 7.2864 seconds.
```
