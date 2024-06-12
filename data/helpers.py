import random as r
def generate_order_info():
    order_info = {
        'name': r.choice(['Гарри', 'Рон', 'Гермиона']),
        'surname': r.choice(['Поттер', 'Уизли', 'Грейнджер']),
        'address': r.choice([' ул. Тисовая, 4', 'Площадь Гриммо, 12']),
        'phone_number': '+' + str(r.randint(11111111111, 99999999999)),
        'metro': r.choice(['Сокольники', 'Динамо', 'Мякинино']),
        'day': str(r.randint(10, 30)),
        'period': r.choice(['сутки', 'двое суток']),
        'color': r.choice(['black', 'grey']),
        'comment': r.choice(['Комментарий', 'Еще один комментарий'])
    }
    return order_info
