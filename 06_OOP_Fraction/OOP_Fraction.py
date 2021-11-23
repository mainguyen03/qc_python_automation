# ### Exercise

# Tạo class `Fraction` (phân số)

# - Hàm khởi tạo nhận 2 giá trị `nr` (tử số) và `dr` (mẫu số)
# - Nếu `dr` âm, chuyển dấu cho `nr` (VD: 1/-2 => -1/2)
# - Triển khai phương thức phù hợp để in ra phân số (VD: `print(fr)` => `-1/2`)
# - Viết hàm `hcf` tìm ước chung lớn nhất của `nr` và `dr`
# - Thêm phương thức `reduce` rút gọn phân số (gọi trong `__init__`)
# - Nếu `nr == 0`, chỉ in ra `0`
# - Nếu `dr == 0`, raise ZeroDevisonError
# - Nếu `dr == 1`, chỉ in ra `nr`
# - Triển khai các phương thức phù hợp cho phép +-*/ với 2 `Fraction` hoặc 1 `Fraction` với 1 số (`int` hoặc `float`), kết quả trả về 1 `Fraction` mới
                                    # -------------------------------------------------------
# @author: Sao Mai 
# Created at: 29/09/21

from typing import Mapping, NoReturn

def hcf(a,b):                                           
  if a == 0:
    return b
  else:
    return hcf(b % a, a)

class Fraction:
    def __init__(self, nr, dr):
        gcd = hcf(nr,dr)
        self.nr = nr/gcd
        self.dr = dr/gcd

    def __repr__(self):
        if self.nr == 0:
            return str(0)
        elif self.dr == 0:
            raise ZeroDivisionError
        elif self.dr == 1:
            return f'{self.nr:.0f}' 
        elif self.dr < 0:
            new_nr = -1 * self.nr
            new_dr = abs(self.dr)
            return f'{new_nr:.0f}/{new_dr:.0f}'
        else: 
            return f'{self.nr:.0f}/{self.dr:.0f}'

    def __add__ (self, other):
        if type(other) == int or type(other) == float:
            new_nr = self.nr + self.dr * other
            new_dr = self.dr
            return Fraction(new_nr, new_dr)
        else:
            new_nr = self.nr * other.dr +  other.nr * self.dr
            new_dr = self.dr * other.dr
            return Fraction(new_nr, new_dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            new_nr = self.nr - self.dr * other
            new_dr = self.dr
            return Fraction(new_nr, new_dr)
        else:
            new_nr = self.nr * other.dr -  other.nr * self.dr
            new_dr = self.dr * other.dr
            return Fraction(new_nr, new_dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            new_nr = self.nr * other
            new_dr = self.dr
            return Fraction(new_nr, new_dr)
        else:
            new_nr = self.nr * other.nr
            new_dr = self.dr * other.dr
            return Fraction(new_nr, new_dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            new_nr = self.nr 
            new_dr = self.dr * other
            return Fraction(new_nr, new_dr)
        else:
            new_nr = self.nr * other.dr
            new_dr = self.dr * other.nr
            return Fraction(new_nr, new_dr)

fr = Fraction(1, 2)
other = Fraction(1.5, -3)
print(fr, other)

print()

print(fr + other)
print(fr - other)
print(fr * other)
print(fr / other)

print()

fr = Fraction(1, 2)
print(fr + 1)
print(fr - 1.5)
print(fr * 2)
print(fr / 2)
