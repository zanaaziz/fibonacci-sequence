# Python Fibonacci Sequence Function
The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.

Let's refer to Fibonacci as 'F'.

Now let's write the formula for it.

**F(n) = F(n-1) + F(n-2)**

**Where:**
- F(n) is term number n
- F(n-1) is the previous term
- F(n-2) is the term before that

**For example,**

F(11) = F(11-1) + (11-2)

F(11) = 89

# Okay, So Where Does The Magic Happen In The Code?
```python
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return "[n must be a positive integer]"
```

This where the most significant condition is tested:
```python
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
```

- The first if condition just tells the program that the first two terms are both equal to 1.
- Then if the number we're looking for is greater than 2, it will continue to add the previous two numbers until it reaches that number. In Mathematics this number is referred to as the n-th term.
- Finally, the else will return a message saying n must be a positive integer (because if n is not 1, not 2 and also not greater than 2, then obviously it's not a positive integer)

# Important Note
The **lru_cache** package is crucial to making this function do what it's supposed to do without taking 10 years to do it. Without it, the function will slow down substantially if the n-th value is for example, 800.
That is because in calculating each term, it has to find the sum of the two previous terms, then the two before it, then the two before it...see where this is going.
This is where this package saves the day by caching each value (in our case I picked 1000) as it goes so later on it can just fetch the value rather than re-calculating it.
