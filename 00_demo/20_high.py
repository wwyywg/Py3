"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

if __name__ == '__main__':
    # 初始距离
    distance = 100

    total = 0

    total += distance

    # 第10次落地时，经历了9次弹起到落地
    for i in range(9):
        distance /= 2
        total += 2 * distance
    print('总共经过距离：', total)
    print('第10次反弹距离：', distance / 2)