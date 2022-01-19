def change(money):
    if len(str(money)) < 4:
        return str(money)
    else :
        list_m = list(str(money))
        if len(list_m) % 3 == 1:  # 1,000,000
            list_m.insert(1,',')
            idx = 1
            for i in range(len(list_m)//3):
                list_m.insert(idx+4, ',')
        elif len(list_m) % 3 == 2: # 10,000,000
            list_m.insert(2, ',')
            idx = 2
            for i in range(len(list_m)//3):
                list_m.insert(idx+4, ',')
        else : #  100,000,000
            idx = -1
            for i in range(len(list_m)//3):
                list_m.insert(idx+4, ',')
    return ''.join(list_m)

print(change(1000))