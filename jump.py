for i in range(1, 101):
    a = i // 10
    b = i % 10
    c = i % 7
    if  a == 7 or b == 7 or c == 0:
        continue
    else:
        print(i)

