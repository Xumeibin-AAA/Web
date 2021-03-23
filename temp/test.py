def f(f1):
    print(f"装饰器开始{f1}")
    def f1(x):
        print(f"装饰器结束{x}")
    return f1
@f(49)
def f2(a):
    print(f2+f"普通函数{a}")

