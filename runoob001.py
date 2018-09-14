
#!/usr/bin/python3
# http://www.runoob.com/python3/python3-module.html

import sys
import runoob002

'''
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print(sys.argv)
 
print('\n\nPython 路径为：', sys.path, '\n')
'''
runoob002.print_func("Runoob")
runoob002.fib(1000)
print(runoob002.fib2(1000))
print(runoob002.__name__)
print(dir(runoob002))
