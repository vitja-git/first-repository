a=[1,2,3,4,5,6]
p=3
while len(a)>1:
    l=len(a)
    print(a.pop(p%l))
    print(a)
    p+=3
print(2%5)
print(5%2)
a=list(range(1,4))
print(a)
print(a.pop(2))