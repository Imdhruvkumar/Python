username = " dhruvkumar"

def func():
    username = "chai"
    print(username)

print(username)
func()


x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(2)
# print(result)


def func3():
    global x 
    x = 12
    return x
  

# result = func3()
# print(result)


def f1():
    x = 88
    def f2():
        print(x)
    return f2()
f1()


def chaicoder(num):
    def actual(x):
        return x**num
    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(2))