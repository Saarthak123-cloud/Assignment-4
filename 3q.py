import random

list = []
for i in range(0, 10):
    list.append(i)
for i in range(0,10):
    a = random.choice(list)
    b = random.choice(list)
    print("Question ", i+1 ,": ", a, 'x', b, ' = ', end = '')
    answer = int(input(''))
    if answer == round(a*b): print(' Right!')
    else: print('Wrong!. The answer is ', round(a*b))