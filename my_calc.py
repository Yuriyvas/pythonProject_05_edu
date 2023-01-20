from functools import reduce


# def my_sum():
# print(my_sum(a))
    # print(my_sum(b))
    # print(my_sum(c))
    # # print(reduce(lambda x, y: x + y, my_sum(a, b, c)))
def my_sum(x,y):
   return x+y
def my_minus(x,y):
   return x-y
def my_stepen(x,y):
   return x**y

def my_umn(x,y):
   return x*y

def devision (x, y):
   red = "\033[31m{}".format
   blue = "\033[34m{}".format
   reset = "\033[0m{}".format('')
   try:
      return x/y
   except ZeroDivisionError:
      print(red('На ноль делить нельзя!'), reset )
      return 0

