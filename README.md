# square-root-calculator
Just a proof of concept of a custom made algorithm for calculating square roots.
(aka a dummy program for calculating square roots)

# How it works
A loop iterates for the number of decimal places specified by precision.
Within this loop:
  An inner loop tests digits from 9 to 0 to determine the next digit of the square root.
  At each step, the script checks if the current partial result squared ```mpf(sqrt + str(x)) ** 2``` is less than the target number ```mpf(num)```.
  If it is valid, the digit is appended to the result string ```sqrt```.
  If it matches exactly, the computation continues but halts further updates to the partial result for the current digit.
  This process is repeated until the desired precision is reached.

**Example**
```
Enter a number to get its square root: 2
Enter the precision of the square root (number of digits): 5
1.41421
```

# Features and Limitations
**Features:**
- Arbitrary precision
  
**Limitations:**
- The script assumes valid numeric inputs. Invalid inputs (e.g., non-numeric values) will cause runtime errors.
- Computing very high precision may be computationally expensive for large numbers.
- The algorithm does not handle negative numbers or non-square roots.
