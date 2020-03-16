# 杨辉三角
# 1
# 1 1
# 1 2 1                 a2
# 1 3 3 1               a2=4-1 a3
# 1 4 6 4 1             a2 a3 a4
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

# 杨辉三角边长 a  控制行数
a=int(input("输入杨辉三角边长：")) #a=3
list=[]
list_1=[]
for i in range(1,a+1):  #1,2,3,4
    if i in [1,2]:
        list.append(1)
    else:
        list_1=list.copy()
        for k in range(1,i-1):#0,1,2,3,4    (1,3)  k=1 2
            if k==i-2:
                list.insert(k,list_1[k-1]+list_1[k])
            else:
                list[k]= list_1[k-1] + list_1[k]
        # for l in range(i,i):
        #     del list[i-1]




    print(list)





# for i in range(1,4):  #1,2,3
#     for j in range(0,i): #0 第一行
#           print("*",end=" ")
#
#     print(" ")



