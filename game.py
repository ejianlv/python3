import random

for ii in range(0,30):
    i = random.randint(1,99)
    j = random.randint(1,99)
    
    print("{0}".format(i).rjust(2),"+".rjust(1),"{0}".format(j).rjust(2),"=".rjust(2))
    
    while True:
        try:
            k = int(input("答案是："))
            break
        except ValueError:
            print("输入无效，请输入数字,请再次输入！")
            continue
    
    if k == i + j:
        print("恭喜你，答对了！")
    else:
        print("很遗憾，答错了！正确答案是：{0}".format(i+j))
    
    if i > j:
        print("{0}".format(i).rjust(2),"-".rjust(1),"{0}".format(j).rjust(2),"=".rjust(2))
    else:
        print("{0}".format(j).rjust(2),"-".rjust(1),"{0}".format(i).rjust(2),"=".rjust(2))

    while True:
        try:
            k = int(input("答案是："))
            break
        except ValueError:
            print("输入无效，请输入数字,请再次输入！")
            continue
    
    if k == abs(i - j):
        print("恭喜你，答对了！")
    else:
        print("很遗憾，答错了！正确答案是：{0}".format(abs(i - j)))  

