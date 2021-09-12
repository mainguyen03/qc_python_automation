# Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:
# m1 = midterm1
# m2 = midterm2
# e = endterm
# Cho một list gồm danh sách điểm thi của sinh viên 1 lớp. 
# Viết chương trình Python để sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple (sắp xếp theo điểm cuối kỳ - endterm tăng dần).
# vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)]

# *********************************************************** Sao *** Mai *************************************************************************************

#Cach 1: dung lambda trong key cua sorted-------------------------------------------------------

my_list_tup = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]

output = sorted(my_list_tup, key=lambda x: x[-1])
print ('Sorting list tuple by last element of tup:', output)

#Cach 2: dinh nghia 1 function roi dung function nhu mot doi tuong. truyen vao key cua sorted.---

my_list_tup = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]

def sort_tup_by_last_element(my_list_tup):
    x = my_list_tup [-1]

    return x

output = sorted(my_list_tup, key = sort_tup_by_last_element)  
print ('Sorting list tuple by last element of tup:', output)
