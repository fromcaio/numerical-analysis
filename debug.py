def calculate_S(n, x):
    """Recursively computes S = 10000 - sum(x for k=1 to n)"""
    if n == 0:
        return 10000
    else:
        return calculate_S(n-1, x) - x

# Example usage:
n = 100000
x = 0.1
S = calculate_S(n, x)
print(f"S = {S}")