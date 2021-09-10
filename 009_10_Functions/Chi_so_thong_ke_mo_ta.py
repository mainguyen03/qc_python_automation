# Cách 1: Tự định nghĩa hàm, không dùng thư viện sẵn
from collections import Counter

score_list = [4,4,5,4,5,5,6, 6, 6, 9]
# [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

def mean(a):
    Sum = sum(a)
    mean = Sum / len(a)
    
    return mean

def median(b):
    if len(b) % 2 == 0:
        i = len(b) // 2
        j = len(b) // 2  + 1
        median = (b[i] + b[j]) / 2 
        
        return median
    else: 
        k = (len(b) // 2) + 1
        median = b[k]

        return median
    
def mode(c):
    x = list (Counter(c).values())  # Bản chất hàm Counter sẽ trả về 1 Dictionary trong đó có key là số a, value là: tần suất xuất hiện của số a trong list. 
    max_item = max(x)               # Tìm ra tần xuất xuất hiện của số nào là cao nhất
    max_list = []
    for index in range (len(x)):
        if x[index] == max_item:    
            y = list(Counter(c).keys())
            max_list.append(y[index]) 
            # Note: Chỗ này nếu gán luôn max_list = y[index] sẽ chỉ trả ra 1 giá trị cao nhất. Ví dụ 4 và 5 đều có tần suất xuất hiện cao nhất là 3 
            # Thì nó sẽ chỉ trả về giá trị là 5. Cần phải thêm .append() thì sẽ trả về cả 4,5. 

    return max_list
    
final_result = (mean(score_list), median(score_list), mode(score_list))
print ('Mean, Median, Mode of list is:',final_result)


#Cách 2: Dùng thư viện sẵn của numpy, stats
import numpy as np
from scipy import stats

score_list = [4,4,5,4,5,5,6, 6, 6, 9]
Mean = np.mean(score_list)
Median = np.median(score_list)
Mode = stats.mode(score_list)
final_result = (Mean, Median, Mode) # Chưa rõ vì sao khi dùng mode có sẵn chỉ trả ra giá trị 4 với tần suất xuất hiện 3. Còn 5 cũng xuất hiện 3 lần nhưng lại không trả ra????
print ('Mean, Median, Mode of list is:',final_result)  
