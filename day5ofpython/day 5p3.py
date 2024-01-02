# # #for loop with range
# # for number in range(1,10,2):
# #     print(number)
# # total=0
# for number in range(0,10):
#     # total+=number
#     print(number)





# to print sum of even numbers from 1 to user choice
target=int(input("Enter the range:\n"))
total=0
for number in range(1,target+1):
    if number%2==0:
        total+=number
    else:
        pass
print(total)


target=int(input("Enter the range:\n"))
total=0
for number in range(2,target+1,2):
    total+=number
print(total)



