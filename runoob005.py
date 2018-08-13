# globals 和 locals
# globals 和 locals 叫做内建函数
a = 1
b = 2

def fun(c,d):
    e = 111
    print("Locals={0}".format(locals()))
    print("Globals={0}".format(globals()))
    
fun(100, 200)
