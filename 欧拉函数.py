import fractions


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount


if __name__ == '__main__':
    print(phi(int(2020)))
