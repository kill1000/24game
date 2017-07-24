num={}      #定义一个字典，用来存放需要计算的数字
oper={1:'+',2:'-',3:'*',4:'/'}      #存放运算符的字典

#读入四个数字
for i in range(1,5):
    num[i]=int(input('输入第'+str(i)+'个数：'))


l_num=[]    #用于存放4个数字不同的排列组合的列表
l_oper=[]   #用于存放运算符组合的列表
temp=[]     #临时列表

#生成4个数字的所有排列组合，数字不可重复使用
key_list=[0,0,0,0]
for i1 in range(1,5):
    key_list[0]=i1
    for i2 in range(1,5):
        if i2 not in key_list:
            key_list[1]=i2
        else:
            continue
        for i3 in range(1, 5):
            if i3 not in key_list:
                key_list[2]=i3
            else:
                continue
            for i4 in range(1, 5):
                if i4 not in key_list:
                    key_list[3]=i4
                    for n in key_list:
                        temp.append(num[n])
                    l_num.append(temp)
                    temp=[]
                    key_list[3] = 0
                else:
                    continue
            key_list[2] = 0
        key_list[1] = 0

#生成所有运算符的排列组合，运算符可以重复使用
key_list=[0,0,0]
temp=['','','']
for i1 in range(1,5):
    temp[0]=oper[i1]
    for i2 in range(1,5):
        temp[1] = oper[i2]
        for i3 in range(1, 5):
            temp[2] = oper[i3]
            l_oper.append(temp.copy())


#取出数字和运算符，进行组合
for nums in l_num:
    for opers in l_oper:
        s=[]
        #数字和运算符组合好之后还要考虑括号的情况，这里实在不知道怎么用循环来写，只好把括号的每一种情况都写出来
        s.append(str(nums[0])+opers[0]+str(nums[1])+ opers[1] + str(nums[2])+ opers[2] + str(nums[3]))
        s.append('('+str(nums[0])+opers[0]+str(nums[1])+')'+ opers[1] + str(nums[2])+ opers[2] + str(nums[3]))
        s.append('('+str(nums[0])+opers[0]+str(nums[1])+ opers[1] + str(nums[2])+')'+ opers[2] + str(nums[3]))
        s.append(str(nums[0])+opers[0]+'('+str(nums[1])+ opers[1] + str(nums[2])+')'+ opers[2] + str(nums[3]))
        s.append(str(nums[0])+opers[0]+'('+str(nums[1])+ opers[1] + str(nums[2])+ opers[2] + str(nums[3])+')')
        s.append(str(nums[0])+opers[0]+str(nums[1])+ opers[1] + '('+str(nums[2])+ opers[2] + str(nums[3])+')')

        #把最后生成的每一个表达式用eval来运算一下
        for ss in s:
#            print(ss)
            #分母为 0 时，不知道怎么处理，只要抓异常了
            try:
                value=eval(ss)
            except ZeroDivisionError:
                continue
            #考虑到除法运算会产生小数，所以最终取值在23.99 和 24.01之间
            if round(value,1)<=24.01 and round(value,1)>=23.99:
                print('算法：',ss)
                exit(0)
print('算不出来:(')
