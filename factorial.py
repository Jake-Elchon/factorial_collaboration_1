'''
    Implementing a factorial program for a github repository 
'''

def factorial(n) -> int: 
    f: int =  1
    i: int = 1
    while ( i <= n):
        f *= i
        i += 1
    print(f"{n}! = {f}")
    
    
