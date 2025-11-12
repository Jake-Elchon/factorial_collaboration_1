'''
    Implementing a factorial program for a github repository 
'''

def factorial(a) -> int:
    f: int =  1
    i: int = 1
    while ( i <= a):
        f *= i
        i += 1
    print(f"{a}! = {f}")
    
    
