# Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:

# s = "Hello World! 123"

# Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".

# a) Viết hàm trên dùng bất kỳ hàm built in nào của python
# b) Viết hàm chỉ dùng 1 hàm built in duy nhất.
# Gợi ý: Bộ ký tự đơn giản in ra màn hình được còn được gọi là bộ mã ASCII (đọc là 'As key') nguyên gốc gồm 128 ký tự. Bạn có thể in ra thử với câu lệnh sau.

# ASCII = "".join(chr(x) for x in range(33, 128))
# print(ASCII)
# Tài liệu tham khảo tiếng Anh. Bạn có thể tìm các tài liệu tiếng Việt các khái niệm tương tự có rất nhiều.


# Cách 1: Dùng nhiều hàm built in
my_string = "Hello World! 123"

def count_char_type(s):
    numbers = sum(c.isdigit() for c in s)
    letters   = sum(c.isalpha() for c in s)
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    space = sum(c.isspace() for c in s)
    others  = len(s) - numbers - letters - space
    final_result = {"LETTERS":letters, "CASE": {"UPPER CASE":upper, "LOWER CASE":lower}, "DIGITS":numbers}

    return final_result

print ('Số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi:', count_char_type(my_string))

#Cách 2: Chỉ dùng 1 hàm built in duy nhất

