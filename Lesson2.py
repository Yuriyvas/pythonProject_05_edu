x = 5
print(x < 8 and x > 3)
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
def give_me_power (num, st):
    print('Hello');
    return num ** st

print( give_me_power(7,8))



#homework








