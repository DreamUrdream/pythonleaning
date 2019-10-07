import random

number = random.randint(0,100) #随机选择一个0到100的整数
step = 0 # 定义一个变量 step 用来记录步数 
input_num = int(input("输入数字:")) # 等待输入数字，int将字符串类转换成整型
while input_num != number: # while 循环，如果输入的数字与随机选择的数据不相等则一直循环
   if input_num > number: # 如果大于则打印大了
        print("大了")
   elif input_num < number: #否则如果小于则打印小了
        print("小了")
   step +=1 # 步数加1 += 自加符 等同于step = step +1 
   input_num = int(input("输入数字:")) #等待用户重新输入数字
print("好了, 你用了 %d 步" %step) # 游戏结束，打印用了多少步
