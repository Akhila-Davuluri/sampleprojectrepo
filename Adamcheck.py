num=int(input("Enter a Num:"))
def isAdam(num):
  return square(num)==reverse(reverse(square(num)))
a=isAdam(12)
print(a)
