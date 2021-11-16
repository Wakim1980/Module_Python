def spam(number):
    return 'bulochka' * number

def my_sum(list_of_numbers):
    b = 0
    for i in list_of_numbers:
        b = b + i
    return b


def shortener(string):
    l1 = string.split()
    l2 = []
    for i in l1:
        sum = len(i)
        if sum > 6:
            i = i[:6] + '*' + i[:0]
            l2.append(i)
        elif sum < 6:
            l2.append(i)
    return(' '.join(l2))



def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here

