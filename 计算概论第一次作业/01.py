def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        # 递推关系
        return (n - 1) * (derangement(n - 1) + derangement(n - 2))

# 示例：计算n=10时的错排数
n = 4
print(f"n={n}时的错排数为：{derangement(n)}")
