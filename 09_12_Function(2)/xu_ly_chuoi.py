# Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). 
# Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. (kết quả là "Chicken The For Coming Is Fox The")

 
# *********************************************************** Sao *** Mai *************************************************************************************
# Có 04 cách:
# Cách 01: Using lamba function instead define function. Bản chất giống hệt cách 02
# Cách 02: Bản chất muốn loại vòng for để giảm độ phức tạp thuật toán 
# Cách 03: Dùng 01 vòng for. 
# Cách 04: Dùng 02 vòng for -> phức tạp nhất.


# Cách 1: Using lambda function-----------------------

import re

my_string = "tHE fOX iS cOMING fOR tHE cHICKEN"
# replace all lower case characters with upper case
new_string = re.sub(r"[a-zA-Z]",
                    lambda x :  x.group(0).upper()
                                if x.group(0).islower()
                                else x.group(0).lower(),
                    my_string)

# reverse string after change lower or upper                  
final_str = ' '.join(reversed(new_string.split(" ")))
print(final_str)


# Cách 2: sử dụng thư viện re. để có thể chuyển all thành hoa thường và ngược lại. Cách này sẽ giúp loại bỏ vòng for -> giảm độ phức tạp.------------------------- 
import re

def reverse_case(match_obj):
    char_elem = match_obj.group(0)
    if char_elem.islower():
        return char_elem.upper()
    else:
        return char_elem.lower()
my_string = "tHE fOX iS cOMING fOR tHE cHICKEN"
# replace all lower case characters with upper case 
new_string = re.sub(r"[a-zA-Z]",reverse_case, my_string)
# reverse string after change lower or upper
final_str = ' '.join(reversed(new_string.split(" ")))
print(final_str)


# Cách 3: -----------------------------------------------------------
my_string = "tHE fOX iS cOMING fOR tHE cHICKEN"

def string_function(my_string):
    # replace character in tring to lower or uper
    my_string1 = ""
    for ch in my_string:
        if ch.isupper():
            new_ch = ch.lower()
        else: 
            new_ch = ch.upper()
        my_string1 += new_ch

    # reverse string after change lower or upper
    new_string = ' '.join(reversed(my_string1.split(" ")))

    return new_string

print(string_function(my_string))


# Cách 4: ------------------------------------------------------------
my_string = "tHE fOX iS cOMING fOR tHE cHICKEN"

def string_function(my_string):
    # replace character in tring to lower or uper
    my_string1 = ""
    for ch in my_string:
        if ch.isupper():
            new_ch = ch.lower()
        else: 
            new_ch = ch.upper()
        my_string1 += new_ch

    #Convert string after change lower or upper
    new_string = my_string1 [::-1].split(" ")

    #Convert each str in tring
    s = ''
    for str in new_string:
        new_str = str [::-1]
        s += new_str + " "

    return s
print(string_function(my_string))