#num={1:4,2:9,3:5,4:12}
num={}
oper={1:'+',2:'-',3:'*',4:'/'}

for i in range(1,5):
    num[i]=int(input('第'+str(i)+'个'))

print(num)


l_num=[]
l_oper=[]
s_num=[]

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
                        s_num.append(num[n])
                    l_num.append(s_num)
                    s_num=[]
                    key_list[3] = 0
                else:
                    continue
            key_list[2] = 0
        key_list[1] = 0

key_list=[0,0,0]
s_num=[]
for i1 in range(1,5):
    key_list[0]=i1
    for i2 in range(1,5):
        key_list[1] = i2
        for i3 in range(1, 5):
            key_list[2] = i3
            for n in key_list:
                s_num.append(oper[n])
            l_oper.append(s_num)
            s_num=[]

for nums in l_num:
    for opers in l_oper:
        '''
        value=eval(str(nums[0])+opers[0]+str(nums[1]))
        value = eval(str(value) + opers[1] + str(nums[2]))
        value = eval(str(value) + opers[2] + str(nums[3]))
       '''
        s=[]
        s.append(str(nums[0])+opers[0]+str(nums[1])+ opers[1] + str(nums[2])+ opers[2] + str(nums[3]))
        s.append('('+str(nums[0])+opers[0]+str(nums[1])+')'+ opers[1] + str(nums[2])+ opers[2] + str(nums[3]))
        s.append('('+str(nums[0])+opers[0]+str(nums[1])+ opers[1] + str(nums[2])+')'+ opers[2] + str(nums[3]))
        s.append(str(nums[0])+opers[0]+'('+str(nums[1])+ opers[1] + str(nums[2])+')'+ opers[2] + str(nums[3]))
        s.append(str(nums[0])+opers[0]+'('+str(nums[1])+ opers[1] + str(nums[2])+ opers[2] + str(nums[3])+')')
        s.append(str(nums[0])+opers[0]+str(nums[1])+ opers[1] + '('+str(nums[2])+ opers[2] + str(nums[3])+')')
        for ss in s:
#            print(ss)
            try:
                value=eval(ss)
            except ZeroDivisionError:
                continue
            if round(value,1)<=24.01 and round(value,1)>=23.99:
                print('算法：',end='')
                print(ss)
                exit(0)
print('我算不出来：（')




