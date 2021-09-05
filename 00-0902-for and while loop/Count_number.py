# Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
# my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# Trả ra
# {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}
#---------------------------------------------------------------------------------------------------------------

#Cách 1: Dùng count()-------------------------------------------------------------------------------------------
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
my_dict = {}
for number in set(my_list):
    #gán giá trị vào my_dict với key = number, values = count(number)
    my_dict[number] = my_list.count(number) 
print ('Count number in my list: ', my_dict)


