from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер1 на час',
        'Выведение1 из запоя',
        'Услуги экскаватора-погрузчика1, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})

def contacts(request, *args, **kwargs):
    contacts = ["телефон - 8-800-708-19-45", "email: sales@company.com"
    ]

    return render(request, 'advertisements/contacts.html', {'contacts': contacts})
