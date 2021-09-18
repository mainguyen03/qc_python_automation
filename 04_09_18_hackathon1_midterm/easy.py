# 1
from datetime import date, datetime
import re


def day_diff(release_date, code_complete_day):
    release_date1 = datetime.strptime(release_date, "%y/%m/%d")
    code_complete_day1 = datetime.strptime(code_complete_day,"%y-%d-%m" )
    delta = (release_date1 - code_complete_day1)
    print (delta)

# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05


# 2

def alpha_num(sentence):
    # Find word must have word + digit
    pattern = re.compile(r"\w+\d+")
    matches = pattern.findall(sentence)
    list_match = []
    for match in matches:
        list_match.append(match)
    print(list_match)
