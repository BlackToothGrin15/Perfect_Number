n=int(input("Enter a number:"))
f=0
for i in range(1,n):
    if n%i==0:
        f+=i
if f==n:
    print("The number is perfect")
else:
    print("The number is not perfect")