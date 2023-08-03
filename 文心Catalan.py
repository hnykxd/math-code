import math  
  
def catalan_number(n):  
    """  
    Returns the nth Catalan number.  
    """  
    if n < 0:  
        return 0  
    elif n == 0:  
        return 1  
    else:  
        return catalan_number(n-1) * (2*n - 1) // (n + 1)  
  
# Output the first 200 Catalan numbers  
for i in range(200):  
    print(catalan_number(i))
