"""
Iterative:

If exponent is 0
    return 0
If exponent is a negative integer
    prompt for positive integer
Else 
    multiply the base to itself exponent - 1 time

Recursive:

If exponent is 0
    return 0
If exponent is 1
    return the base
Else
    multiply base to base raise to exponent of exponent - 1

Test Cases:

iterative_power(3, 6) : 729
recursive_power(3, 6) : 729

iterative_power(6, 9) : 10077696
recursive_power(6, 9) : 10077696

iterative_power(420, 1) : 420
recursive_power(420, 1) : 420
"""

def iterativePower(base, exp):
    """

    """
    result = base
    if exp == 0:
        return 1
    elif exp < 0:
        exp = int(input("(Exponent must be positive integer) Exponent: "))
    for n in range(1, exp):
        result *= base
    return result

def recursivePower(base, exp):
    """

    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recursivePower(base, exp - 1)

def main():
    result_iter = iterativePower(100, 0)
    result_recur = recursivePower(100, 0)
    print(f"Iterative: {result_iter}\nRecursive: {result_recur}") 

if __name__ == "__main__":
    main()