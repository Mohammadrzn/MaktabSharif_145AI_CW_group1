while 1:
    score = int(input('please enter your score:'))
    if 0 <= score <= 100:
        break
    else:
        continue

if 90 <= score <= 100:
    print ('a')
elif 80 <= score <= 89:
    print('b')
elif 70 <= score <= 79:
    print('c')
else:
    print('you failed!!!')