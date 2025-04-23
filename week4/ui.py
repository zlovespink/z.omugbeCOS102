# x = 0
# for i in range(1,6):
#    if i%2 ==0:
#     x+=i 
# else:
#     x-=i
#     print(x)


# x = 0
# for i in range(1,6):
#     if i % 2 == 0:
#       x += i
#     else:
#       x -= i
# print(x)


s = 'numbers'
print(s[:-3])


num = 0
for num in range(6):
    num = num+1
    if num==3:
        continue
    print('Num has value'+ str(num))
    print('End of loop')