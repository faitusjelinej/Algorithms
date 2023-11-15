def isPalindrome(x):
    if x<0:
        return False
    revnum = 0    
    y = x    
    while x > 0:
        rem = x%10
        revnum = revnum*10 + rem
        x = x//10
    if y == revnum:
        return True
    else:
        return False
    
x = 121
print(isPalindrome(x))  
