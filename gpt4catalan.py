def catalan_numbers(n):
    if n <=1:
        return 1

    catalan = [0 for i in range(n+1)]
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    return catalan

# 打印前10个卡特兰数
for i in range(999999):
    print(catalan_numbers(i))
