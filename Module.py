def spam(number):
    return 'bulochka' * number



def my_sum(list_of_numbers):
    b = 0
    for i in list_of_numbers:
        b = b + i
    return b

l = 'have been English literature'
l1 = l.split()
l2 =[]
for i in l1:
    sum = len(i)
    if sum > 6:
        i = i[:6] + '*' + i[:0]
        l2.append(i)
    elif sum < 6:
        l2.append(i)
print(' '.join(l2))