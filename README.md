# Python Fibonacci Sequence Calculation Function
A program that calculates the n-th term of the Fibonacci sequence.

# How It Works
Let's refer to Fibonacci as 'F' for now.
Now let's write the formula for it.

Fn = Fn-1 + Fn-2

Where:
- Fn is term number n
- Fn-1 is the previous term
- Fn-2 is the term before that (n-2)

# Okay, So Where Does The Magic Happen In The Code?
Well, obviously it's at the function at line 13:
```python
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
```

More specifically though, it happens on line 16 and 17 here:
```python
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
```

- The first if condition just tells the program that the first two terms are both equal to 1.
- Then if the number we're looking for is greater than 2, it will continue to add the previous two numbers until it reaches that number. In Mathematics this number is referred to as the n-th term.

# Note
The lru_cache package is crucial to making this function do what it's supposed to do without taking 10 years to do it. Without it, the function will slow down substantially if the n-th value is for example 800.
That is because in calculating each term, it has to find the sum of the two previous terms, then the two before it, then the two before it...see where this is going.
This is where this package saves the day by caching each value (in our case I picked 1000) as it goes so later on it can just fetch the value rather than re-calculating it.
