"""
打印出100以内的质数，质数也叫素数，是指在大于1的自然数中，如果该数除了能被1和它本身整除外，其他皆不能整除，则该数为质数
这个题目主要考在循环中使用else，掌握else配合break在循环中用法
"""
print("using else")
a = 2
while a < 101:
    for b in range(2,a):
        if a%b == 0:
            break
    else:
        print(a,end=" ")
    a += 1


"""
同行求100以内的素数，不使用else
"""
print("\n\nnot using else")
a = 2
while a <101:
    flag = 0
    for b in range(2,a):
        if a%b == 0:
            flag = 1
            break
    if flag ==0 :
        print(a, end =" ")
    a +=1
print("\n")
