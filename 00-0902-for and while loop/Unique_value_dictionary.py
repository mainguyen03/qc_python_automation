# cach 1:---------------------------------------------------------------------------------------------------------------
my_dict1 = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
my_dict2 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

result = []
for dict in my_dict2:
    for val in dict.values():
        result.append(val)
result = sorted(result)
final_result = set(result)

print('Unique Value Dictionary is: ', final_result)

# cach 2:----------------------------------------------------------------------------------------------------------------
# my_dict1 = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
# my_dict2 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# unique_value_dictionary = set (val for dict in my_dict1 for val in dict.values())
# print(f'Unique Value Dictionary is: {unique_value_dictionary}')