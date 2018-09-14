# -*- coding: utf-8 -*-
import sys

# 打开一个文件
f = open("foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()
#----------------------------------------------------------------
f = open("foo.txt", "r")

str1 = f.read()
print(str1)

f.close()

#----------------------------------------------------------------

f = open("foo.txt", "r")

str1 = f.readline()
print(str1)

f.close()

#----------------------------------------------------------------

f = open("foo.txt", "r")

str1 = f.readlines()
print(str1)

f.close()
#----------------------------------------------------------------

f = open("foo.txt", "r")

for line in f:
    print(line, end="")

f.close()    
#----------------------------------------------------------------
f = open("foo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()

#----------------------------------------------------------------
f = open("foo1.txt", "w")
print(f.tell())
value = ('www.runoob.com', 14)
f.write(str(value))
print(f.tell())
s = str(value)
f.write(s)

# 关闭打开的文件
print(f.tell())
f.close()
#----------------------------------------------------------------

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

print(str(selfref_list))
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
#----------------------------------------------------------------
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
#----------------------------------------------------------------
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()        
#----------------------------------------------------------------