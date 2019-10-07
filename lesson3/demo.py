import random

number = random.randint(0,100)
input_num = int(input("输入数字:"))
if input_num > number:
    print("大了")
elif input_num < number:
    print("小了")
else:
    print("好了")
print("随机数是：",number)
