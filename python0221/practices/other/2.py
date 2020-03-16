# list_1=["1"]
# list_2=["1","2"]
# list_3=["1","2","3"]
# list_all=[list_1,list_2,list_3]
# list_4=["1","2","3","4"]
# list_all.insert(4,list_4)
# print(list_all)
# 一：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 1  2  3  4
# 1  2  3  4
# 1  2  3  4
# 1开头:
# 111 112 113 114---- x
# 121 122 123 124----123 124
# 131 132 133 134----132 134
# 141 142 143 144----142 143


input_list=[1,2,3,4]  #输入列表
output_list=[]  #输出列表
# 取百位数 hundred
for hundred in input_list:
    # hundred=100*hundred
    # print(hundred)
    # 取十位数 decade
    for decade in input_list:
        # decade=10*decade
        # print(decade)
    # # 取各位数 bit
        for bit in input_list:
            # bit*= 1
        #     要求三位数互不相同
            if hundred!=decade and decade!=bit and hundred!=bit:
                #     获得三位数 three_digit并加入输出列表中
                three_digit=hundred*100+decade*10+bit*1
                output_list.append(three_digit)
 # 去重 获取结果列表,set去重后获得结果为字符串
last_list=list(set(output_list))  #结果列表
print(sorted(last_list))
# print(type(set(output_list)))






# for n in range(0,len(output_list)):  # (0,1) n=0 m=1 (1,2)
#     for m in range(1,len(output_list)+1):
#             if output_list[n]!=output_list[n+m]:
#                 last_list.append(output_list[n])
#
#
# print(output_list)
# print(last_list)


#
# for n in range(0,1):  # (0,1) n=0 m=1 (1,2)
#     for m in range(1,2):
#             if output_list[n]!=output_list[n+m]:
#                 last_list.append(output_list[n])
# print(n+m)
# print(output_list)
# print(last_list)














# 二：有1、2、3、4。。N个数字，能组成多少个互不相同且无重复数字的N-1位数？都是多少？