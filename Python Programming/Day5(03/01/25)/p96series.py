Number = int(input("Enter the limit => "))
s = 0
for i in range(1, Number + 1):
    if i%2==0:
        print(i, end=" + ")
        s = s + i

print("\n",s)