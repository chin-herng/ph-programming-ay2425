def prime_number_up_to(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime(i):
            ans.append(i)
    return ans
    
def is_prime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
    
print(prime_number_up_to(100))
