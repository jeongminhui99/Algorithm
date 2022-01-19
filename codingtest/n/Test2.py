def fibo(idx):
    if idx == 0:
        return 0
    elif idx == 1 or idx == 2:
        return 1
    else:
        return fibo(idx-1) + fibo(idx-2)

def fubo2(idx):
    f_list = [0, 1, 1]
    if idx == 0:
        return 0
    elif idx == 1 or idx == 2:
        return 1
    for i in range(3, idx+1):
        f_list.append(f_list[i-1] + f_list[i-2])
    return f_list[idx]

def fibo3(idx):
    curr, next, tmp = 0, 1, 0
    if idx == 0:
        return 0
    elif idx == 1 or idx == 2:
        return 1
    else:
        for i in range(idx):
            tmp = next
            next += curr
            curr = tmp
        return next
# 0 1 -> 1 1 -> 1 2 -> 
# 0 1 1 2

1.6 ^ n <= 2^32-1

