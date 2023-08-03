# 打印前 n 个卡特兰数
ans, n = 1, 99999999
print("1:" + str(ans))
for i in range(2, n + 1):
    ans = ans * (4 * i - 2) // (i + 1)
    print(str(i) + ":" + str(ans))