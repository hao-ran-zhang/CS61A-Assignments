max(7.5, 9.5)
pow(100, 2) # pow 函数的第二个参数是第一个参数的幂
pow(2, 100)
max(1, -2, 3, -4)
max(min(1, -2), min(pow(3, 5), -4)) # nested 嵌套


## 导入库函数
from math import sqrt
sqrt(256) # 16.0

from operator import add, sub, mul
add(9,16)
sub(100,10)
mul(3,7)

## 多变量赋值
radius = 10
from math import pi
area, circumference = pi * radius * radius, 2 * pi * radius
area
circumference

## 交换值
x, y = 3, 4
y, x = x, y
print("x=",x, "  ","y=",y) # x= 4    y= 3

## define function
def square(x):
    return mul(x, x)
square(5)

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(5,5)

## 除法(浮点数和向下取整)
5/4   # 1.25
5//4  # 1
from operator import truediv, floordiv
truediv(5,4)  # 1.25
floordiv(5,4) # 1

# function design
def pressure(v, t, n):
    """计算理想气体的压力，单位为帕斯卡

使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

v -- 气体体积，单位为立方米
t -- 绝对温度，单位为开尔文
n -- 气体粒子
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v
help(pressure)

## 局部赋值
def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x
percent_difference(40,50)

## 条件语句
def absolute_value(x):
    if x > 0 :
        return x
    elif x ==0 :
        return x
    else:
        return -x
result = absolute_value(-5)
result

## 迭代
def fib(n):
    pred, curr = 0, 1
    k =2
    while k < n:
        pred, curr = curr, pred + curr
        k +=1
    return curr

fib(8)

## 测试
assert fib(8) == 13, '第八个斐波那契数应该是 13'       

## 作为参数的函数
def sum_naturals(n):
## 计算1-n的和
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total
sum_naturals(100) #5050

def sum_cubes(n):
## 计算1-n的立方之和
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total
sum_cubes(100) #25502500

def pi_sum(n):
#收敛到pi
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total
pi_sum(100) # 3.1365926848388144

## 共用一个模板pattern
"""
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
"""

def summation(n,term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

## for example1
def identity(n):
    return n
def sum_natural(n):
    return summation(n,identity)
sum_natural(100) # 5050

## for example2
def cudes(x):
    return x*x*x
def sum_cude(n):
    return summation(n,cudes)
sum_cude(100) # 25502500

## for example 3
def pi_formula(x):
    return 8 / ((4*x-3) * (4*x-1))
def sum_pi(n):
    return summation(n,pi_formula)
sum_pi(100) #3.1365926848388144
sum_pi(1e6) #3.141592153589902

## 作为通用方法的函数
## 将目标拆分为一个个函数
## example: 黄金比例
def golden_update(guess):
    return 1/guess + 1

def square_close_to_success(guess):
    return  approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

improve(golden_update,square_close_to_success)
# 1.6180339887498951
## 检测
from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_success)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'
improve_test()

## 函数嵌套定义
def average(x,y):
    return (x+y)/2

def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update,sqrt_close)
sqrt(121)

## 作为返回值的函数
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h ## 返回了 f(g(x))
def square(x):
    return x * x
def successor(x):
    return x + 1
square_successor = compose1(square, successor)
square_successor(12) # (12+1)^2=169

## Newton-Raphson
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)
#example: x^2 - a
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)
square_root_newton(64) #8.0

## 柯里化 curring
# example
def multiply(x):
    def by(y):
        return x * y
    return by

double = multiply(2)  # 固定 x=2
triple = multiply(3)  # 固定 x=3
print(double(5))  # 输出 10
print(triple(5))  # 输出 15

# pow函数的currying版本
def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h
curried_pow(2)(3) #8

# map
def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
map_to_range(0,10,curried_pow(2))

# lamda 表达式
s = lambda x: x * x
s # <function <lambda> at 0x000001E86EDF53A0>
s(12) # 144
