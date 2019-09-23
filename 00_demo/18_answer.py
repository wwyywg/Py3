
if __name__ == '__main__':
    num = input('输入重复的数字:\n')
    times = int(input('你的重复的次数:\n'))

    answer = 0
    for i in range(times):
        answer += int(num)
        num += num[0]

    print('结果为：', answer)