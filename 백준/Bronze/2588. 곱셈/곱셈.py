a = int(input())
b = int(input())

b1 = b%10
b10 = (b%100)//10
b100= (b//100)

c3 = a*b1
c4 = a*b10
c5 = a*b100

print(c3)
print(c4)
print(c5)

print(a*b)