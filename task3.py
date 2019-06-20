x = int(input("First number: "))
y = int(input("Second number: "))

xb = format(x, '032b')
yb = format(y, '032b')
xb_str = str(xb)
yb_str = str(yb)
xb_set = list(xb_str)
yb_set = list(yb_str)


test = sum(c1 != c2 for c1, c2 in zip(xb_set, yb_set))

print(test)
