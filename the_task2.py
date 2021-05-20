def pen_ifo(**kwargs):
    return ' '.join(kwargs.values())
name = input('Введите имя')
sname = input('Введите фамилию')
data = input('Ввежите год рождения')
gor = input('Введите город')
mail = input('Введите имэил')
tel = input('Введите телефон')

print(pen_ifo(name=name, sname=sname, data=data, gor=gor, mail=mail, tel=tel))





