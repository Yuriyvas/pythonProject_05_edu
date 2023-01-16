x = 5
print(8 > x > 3)
print(x < 8 or x > 3)
print(x < 8 and not x > 3)

#part 2

print('*** Part 2 ***')

x = 8
if x == 5:
    print('Five')
elif x > 5:
    print('More then five')
else:
    print('Not five')
print('End')

#part 3

print('*** Part 3 ***')

i = 1
while i <  5:
    print('Hello ' + str(i))
    if i == 3:
        break
    i = i + 1

#for

name = 'Yuriy'
for letter in name:
    print(letter)

print('*' * 15)

for n in range(30, -31, -2):
    print(n, end=' ')
print('')


# def
print("* " * 15)
def give_me_power (xyz, st):
    print('Hello')
    return xyz ** st

print( give_me_power(7,8))



#homework

#hw1
print('**** Homework #1 ***')

health = float(input('Health: '))
if health >0:
    print('True')
else: print('False')


#hw2
print('**** Homework #2 ***')

num = float(input('Enter any number: '))
if num % 2 == 1 :
    print('Odd')
else: print('Even')

#hw3

print('**** Homework #3 ***')

# year = float(input('Enter any year: '))
year = input('Enter any year: ')
if year % 400 == 0:
    print(f'{year} Leap year 400')
elif year % 100 == 0:
    print(f'{year} Not-leap year 100')
elif year % 4 == 0:
    print(f'{year} Leap year')
else: print(f'{year} Not-leap year', end=' ')

#hw4
print('**** Homework #4 ***')

text = input('Input any text: ')+ '\n'
repeat = int(input('How mach repeat it:'))
print(text * repeat)













