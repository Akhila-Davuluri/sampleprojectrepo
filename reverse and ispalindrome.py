##write a program to find the reverse of a given number
def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

def isPalindrome(num):
    return num==reverse(num)


print(reverse(1235))

print(reverse(1234))

print(isPalindrome(123))

print(reverse(121))
print(isPalindrome(121))

def getPalindrome(strat,end):
    res=","
    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res
print(getPalindrome(1,10000))
