import random

#生成一个0-99的随机数
i = random.randint(0,100)

while True:
    j = int(input("请输入一个0到99之间的整数："))
    if i==j:
        print("恭喜你猜对了！")
        break
    elif i < j:
        print("猜大了，再来！")
        continue
    elif i > j:
        print("猜小了，再来！")
        continue
print("游戏结束!")        
