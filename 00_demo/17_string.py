"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数；
"""

import string

s = input('请输入字符串:\n')
num_letter = 0
num_space = 0
num_digit = 0
num_other = 0

if __name__ == '__main__':

    for i in range(len(s)):
        if s[i].isspace():
            num_space += 1
        elif s[i].isdigit():
            num_digit += 1
        elif s[i].isalpha():
            num_letter += 1
        else:
            num_other += 1

    print('character：', num_letter)
    print('space：', num_space)
    print('digit', num_digit)
    print('other：', num_other)
