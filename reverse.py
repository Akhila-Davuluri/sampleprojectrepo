##write a program to find the reverse of a given number
def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

def isPalindrome(num):
    return num==reverse(num)

print(reverse(1234))
print(ispalindrome(123))

print(reverse(121))
print(ispalindrome(121))
