def recursion(num):
    if num == 0:
        return 1
    else:
        return num * recursion(num-1)

result = recursion(5)

print(result)