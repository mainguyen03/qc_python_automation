# Cach 1: Dung sum - number de tim ra gia tri diff. Xong do tim diff trong list

my_list = sorted([1,2,3,6,4,5,8,9,0])
sum = int(input('Input sum of 2 number: '))
result = []
while my_list:
    number = my_list.pop()
    diff = sum - number
    if diff in my_list: 
        result.append((number, diff))
print (result)


# Cach 2: Nhưng khi print bị duplicate, chưa lọc được tuple có giá trị ngược nhau bị trùng ví dụ (1,8) và (8,1)---------------------------------
#  my_list = sorted([1,2,3,6,4,5,8,9,0])
# print (my_list)
# sum = int(input('Input sum of 2 number: '))
# other_list = []

# for number in my_list:
#     for other_number in my_list:
#         total = number + other_number
#         if total == sum:
#             my_tup = (number,other_number)
#             other_list.append(my_tup)
 
# print (other_list)

