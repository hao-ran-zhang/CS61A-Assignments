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
def number(n):
    return n
def sum_natural(n):
      return summation(n,number)
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
def 