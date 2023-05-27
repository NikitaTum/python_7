def one(str):
    str = str.split()
    list = []
    for word in str:
        sum = 0
        for i in word:
            if i in 'а':
                sum += 1
        list.append(sum)
    return len(list) == list.count(list[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if one(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')