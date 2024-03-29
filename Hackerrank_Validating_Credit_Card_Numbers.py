def check(s):
    #It must start with a 4,5 or 6 . 
    if s[0] != '4' and s[0] != '5' and s[0] != '6':
        return False
       
    #It must contain exactly 16 digits.
    if len(s.replace("-","")) != 16:
        return False
    
    #It must only consist of digits (0-9).
    for i in range(len(s)):
        if s[i]== '-':
            continue
        if not s[i].isdigit():
            return False
        
    
    #It may have digits in groups of 4, separated by one hyphen "-".
    d = 0
    for i in range(len(s)):
        if (s[i] == '-' and d!= 4):
            return False
        elif (s[i] == '-' and d==4):
            d= 0
        else:
            d+= 1
            
    
    
    #It must NOT use any other separator like ' ' , '_', etc.
    if (" " in s or "_" in s):
        return False
            
    #It must NOT have 4 or more consecutive repeated digits.
    c=0
    cc = s.replace("-","")
    for i in range(len(cc)-1):
        if (cc[i]!= cc[i+1]):
            c= 0
        else:
            c+=1
        if c==3:
            return False    


    return True

num = input()
for i in range(int(num)):
    s = input()
    if (check(s)):
        print("Valid")
    else:
        print("Invalid")
