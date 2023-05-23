import time

# 1
# def do_something(x):
#     answer = 0
#     array = [x, x**0, x//x, x % (x-4), [x]]
#     for i in range(x):
#         answer += array[i]
#     return answer


# x = int(input())

# try:
#     do_something(x)
# except ZeroDivisionError:
#     print('input should be more than 4')
# except ValueError:
#     print('input should be integer numbers')
# except TypeError:
#       print('input TypeError')


# 2
# def do_something(x):
#     answer = 0
#     array = [x, x**0, x//x, x % (x-4), [x]]
#     for i in range(x):
#         answer += array[i]
#     return answer


# x = int(input())

# try:
#     do_something(x)
# except ZeroDivisionError:
#     print('input should be more than 4')
# except ValueError:
#     print('input should be integer numbers')
# except TypeError:
#     print('input TypeError')
# else:
#     print(do_something(x))


# 3
#x = input()

# def countrycode(x):
#     if type(x) != str:
#         raise TypeError
#     if x[0] == '+':
#         if x.isdigit:
#             raise ValueError
#          if len(x) != 13:
#              raise IndexError
#         if x[1] == '6' and x[2] == '6':
#             print('Thailand')
#         if x[1] == '3' and x[2] == '4':
#             print('Spain')
#         else:
#             print('Other country')
#     else:
#         raise LookupError

# countrycode(x)

# 4
# x = input()

# def countrycode2(x):
#     assert type(x) != str
#     assert x[0] == '+'
#     assert x.isdigit
#     assert len(x) != 13

#     if x[1] == '6' and x[2] == '6':
#         print('Thailand')
#     if x[1] == '3' and x[2] == '4':
#         print('Spain')
#     else:
#         print('Other country')

# countrycode2(y)

# 5
# x = list(input())
# l = []
# def enum(x):
#     for i in range(len(x)):
#         a = (i,x[i])
#         l.append(a)
#     print(l)
# enum(x)

# 6
# def lcm(x, y):
#     for i in range(max(x, y), x*y+1):
#         if i%x == 0 and i%y == 0:
#             break
#     return i

# t_start = time.time()
# print(lcm(13, 97))
# t_end = time.time()
# print(t_end - t_start)
# # print(t_end)
# # print(t_start)