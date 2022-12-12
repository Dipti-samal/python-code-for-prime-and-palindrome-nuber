n=int(input("enter the number:"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    if flag==1:
        print("entered number is not a prime palindrome number")
    else:
        print(n,"is prime number")
    x=n
    sum=0
    while x>0:
        r=x%10
        sum=sum*10+r
        x=x//10
    if sum==n:
        print(n,"is a palindrome number")
    else:
        print(n,"not a prime number")
