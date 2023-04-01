def can_eat(x, y):
    if x[0]==x[3] or x[3]==y[3]:
        print("result = False")
    else:
        print("result = True")
can_eat(x = input(), y = input())