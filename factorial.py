'''
    Implementing a factorial program for a github repository 
'''

def factorial(r) -> int:
    f: int =  1
    i: int = 1
    while ( i <= r):
        f *= i
        i += 1
    print(f"{r}! = {f}")
    
    
