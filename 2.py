def f(integer):
    remain_list = []
    for i in range(1, integer+1):
        if i % 3 == 0 and i % 5 == 0:
            remain_list.append(i)
        elif i % 3 == 0 or i % 5 == 0:
            continue
        else:
            remain_list.append(i)
    return len(remain_list)

if __name__ == '__main__':
    integer = int(input())
    remain_num = f(integer)
    print(remain_num)