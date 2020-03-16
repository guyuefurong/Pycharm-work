
# while True:
#     n=int(input("打印等腰三角形腰长为： n=1 2 3 ")) #n=3时 i=1 j=2 k=1 i=2 j=1 k=3
#     for i in range(1,n+1):
#         j=n-i
#         m=2*i-1
#         if n == 3:
#             break
#         print(" "*j,end=" ")
#         print("*"*m)
#     c = input("是否继续y/n：")
#     if c=='n':
#         break


for i in range(1,10): #控制为9行，第一行，当i=1，j=1   i=2，j=1 2  i=3，j=1 2 3
		for j in range(1,i+1):
			print("{0}x{1}={2}".format(i,j,i*j),end=" ")
		print("")


