"""
题目：输出指定格式的日期；
"""

import datetime

if __name__ == '__main__':
    # 输出当前日期
    print(datetime.date.today())

    # 创建日期对象
    Z_Birth = datetime.date(1993, 4, 25)
    print(Z_Birth)

    # 指定格式输出
    print(Z_Birth.strftime('%m/%d/%Y'))

    # 日期替换
    Z_Birth = Z_Birth.replace(year=Z_Birth.year+1)
    print(Z_Birth)

    # 日期运算
    Next_Z_Birth = Z_Birth + datetime.timedelta(days=366)
    print(Next_Z_Birth)