a = input()
b = input()
if a == 'камень' and b == 'ножницы' or a == 'ножницы' and b == 'бумага' or\
        a == 'бумага' and b == 'пират' or a == 'камень' and b == 'ром' or a == 'ножницы'\
        and b == 'ром' or a == 'пират' and b == 'ножницы' or a == 'пират' and b == 'камень' or \
        a == 'ром' and b == 'пират' or a == 'ром' and b == 'бумага' or a == 'бумага'\
        and b == 'камень':
    print('первый')
elif b == 'камень' and a == 'ножницы' or b == 'ножницы' and a == 'бумага' or\
        b == 'бумага' and a == 'пират' or b == 'камень' and a == 'ром' or b == 'ножницы'\
        and a == 'ром' or b == 'пират' and a == 'ножницы' or b == 'пират' and a == 'камень' or \
        b == 'ром' and a == 'пират' or b == 'ром' and a == 'бумага' or b == 'бумага'\
        and a == 'камень':
    print('второй')
elif a == b:
    print('ничья')