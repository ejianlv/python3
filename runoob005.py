# globals 和 locals
# globals 和 locals 叫做内建函数
a = 1
b = 2

def fun(c,d):
    e = 111
    print("Locals={0}".format(locals()))
    print("Globals={0}".format(globals()))
    
#fun(100, 200)
for i in range(1, 10):
    for j in range(1, i+1):
        print("{0} x {1} = {2}".format(j, i, i*j), end="  ")
    print("")
    print('yes')

    print('you are welcome')





