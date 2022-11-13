a = int(input("Enter a:"))
b = int(input("Enter b:"))
i = 0
j = 0
if a% 3 == 0:
        for i in range(a,b,3):
                print(i)
                j += i
elif a% 3 == 1:
        for i in range(a+2,b,3):
                print(i)
                j +=i
elif a% 3 == 2:
        for i in range(a+1,b,3):
                print(i)
                j += i
if b% 3 == 0:
        print(b)
        j += b
print("-"*6, " +",)
print(j)
