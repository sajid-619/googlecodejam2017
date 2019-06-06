def non_decreasing_number(num):
    remainder = 10
    while num > 0 :
        if num % 10 <= remainder :
            remainder = num % 10
            num /= 10;
        else :
            return False
    return True
    
def last_tidy_number(num):
    subtrahend = ( num % 10 ) + 1
    num -= subtrahend
    subtrahend = 10
    while not non_decreasing_number(num) :
        if num % (subtrahend * 10) == (subtrahend * 10) - 1 :
            subtrahend *= 10
        num -= subtrahend
    return num
    
t = int(input())
for i in range(0, t):
    n = int(input())
    if non_decreasing_number(n):
        print("Case #", i + 1, ": ",  n,  "\n")
    else :
        print("Case #", i + 1, ": ", last_tidy_number(n),  "\n")