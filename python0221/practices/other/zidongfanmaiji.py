p=0
Sum = [1, 5, 10]
total=0
while True:
    while True:
        n=input('输入购买饮料种类：1-橙汁-3.5元 2-椰汁-4元 3-矿泉水-2元 4-可乐-4.5元')
        if n in ["1","2","3","4"]:
            break
        else:
            print("输入有误，请重新选择")
    m=int(input("输入购买数量："))
    if n=="1":
        total+=m*3.5
    elif n=="2":
        total+=m*4
    elif n=="3":
        total+=m*2
    elif n=="4":
        total+=m*4.5
    y=input("是否继续购买y/n：")
    if y!="y":
        break
while True:
    while True:
        j=int(input("请付款{0}元".format(total)))
        if j in Sum:
            p+=j
            break
        else:
            print("请重新支付")
    if total<=p:
        l=p-total
        print("找零{0}元".format(l))
        break
    else:
        print("金额不足，请继续支付")