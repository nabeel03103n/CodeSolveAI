# Without walrus operator
x = 10
if x > 5:
    print(x)

# With walrus operator
if (x := 10) > 5:
    print(x)
