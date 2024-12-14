# sum of natural number that is only positive number

num = int(input('Enter a number here:'))

if num<0:
    print('please enter positibe number:')
else:
    sum= 0
    while num>0:
        sum +=num
        num -=1
        print(sum)
