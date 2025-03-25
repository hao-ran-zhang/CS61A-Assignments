type(2)
type(1.5)
type(1+1j)
type(1/3)

## data abstract
1/3
1/3 == 0.333333333333333300000 #True

## 构造有理数
# 在还没有想好表示有理数的情况下先定义加法和乘法
def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)
## 现在还需要某种方法将分子和分母粘合在一起形成一个复合值

# list
[10, 20]
pair = [10,20]
pair
x, y = pair # [10, 20]
x # 10
y # 20

# 索引
# 距离列表开头的偏移量
pair[0]
pair[1]

from operator import getitem
getitem(pair,0)
getitem(pair,1)

# define 分数
from math import gcd
def rational(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

def numer(x):
    return x[0]

def denom(x):
    return x[1]

half = rational(1, 2)
print_rational(half)
third = rational(1, 3)
print_rational(mul_rationals(half, third))
print_rational(add_rationals(third,third))


# 序列
## 列表
digits = [1, 8, 2, 8]
len(digits)
digits[3]

[2, 7] + digits * 2 # [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]

# 嵌套列表
pairs = [[10, 20], [30, 40]]
pairs[0] # [10, 20]
pairs[0][1] # 20

## 使用 for循环来遍历列表
def count_use_while(s, value):
    """统计在序列 s 中出现了多少次值为 value 的元素"""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

print(digits)
count_use_while(digits,8)

def count_use_for(s, value):
    """统计在序列 s 中出现了多少次值为 value 的元素"""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

count_use_for(digits,8)

## 序列解包（Sequence unpacking）
# for 循环可以在头部的 <name> 中包含多个名称
# 来将每个元素序列“解包”到各自的元素中
pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count +=1
same_count # 2

# range 起始值和结束值加一
range(1, 10)  # 包括 1，但不包括 10
list(range(5,8))

# if only one paramter: 默认 0-n
list(range(5))

def count_use_range(s, value):
    """统计在序列 s 中出现了多少次值为 value 的元素"""
    total = 0
    for i in range(len(s)):
        if s[i] == value:
            total = total + 1
    return total

count_use_range(digits,8)

# 如果 name没有在 suite中被用到，可以用_代替
## Ex:
for _ in range(3):
    print("Stat")


## 列表推导式（List Comprehensions）
# [<map expression> for <name> in <sequence expression> if <filter expression>]
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds] # [2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0] # [1, 5]

## 聚合（Aggregation）
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

divisors(4) # [1, 2]
divisors(12) # [1, 2, 3, 4, 6]

# 完美数 perfect number: 约数的和等于自身
[n for n in range(1, 1000) if sum(divisors(n)) == n]
# [1, 6, 28, 496]

# 在给定面积的情况下计算具有整数边长的矩形的最小周长
def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
width(area, 5) # 16
perimeter(16,5) # 42
perimeter(10, 8) # 36
minimum_perimeter(area) # 36
[minimum_perimeter(n) for n in range(1, 10)]
#面积从1到9， 最小的周长[4, 6, 8, 8, 12, 10, 16, 12, 12]

## 高阶函数（Higher-Order Functions）
def apply_to_all(map_fn, s):
        return [map_fn(x) for x in s]

from math import sqrt
apply_to_all(sqrt,odds)
# [1.0, 1.7320508075688772, 2.23606797749979, 2.6457513110645907, 3.0]

def keep_if(filter_fn, s):
        return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

from operator import mul
reduce(mul,[2,4,8],1) # 64

# 使用高阶函数寻找完美数
def divisors_of(n):
        divides_n = lambda x: n % x == 0
        return [1] + keep_if(divides_n, range(2, n))

divisors_of(12) # [1, 2, 3, 4, 6]

from operator import add
def sum_of_divisors(n):
        return reduce(add, divisors_of(n), 0)

def perfect(n):
        return sum_of_divisors(n) == n

keep_if(perfect, range(1, 1000))
# [1, 6, 28, 496]

## 序列抽象
# 成员资格（Membership）
# in and not in
digits  # [1, 8, 2, 8]
2 in digits # True
10 in digits # False

# 切片（Slicing）
# 3 parameters
# 最后一个参数控制步长
digits[0:2] # [1, 8]
digits[1:]  # [8, 2, 8]
digits[::-1] [8, 2, 8, 1]

