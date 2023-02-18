# Программа "Личный счет"

def choice_menu():  # menu
    my_menu = {'1': 'пополнение счета', '2': 'покупка', '3': 'история покупок', '4': 'баланс', '5': 'средний чек', '0': 'выход'}
    print('.' * 21)
    for key, val in my_menu.items():
        print(f'{key}. {val}')
    print('.' * 21)
    to_do = input('Выберите пункт меню: ')
    return to_do


def bank_account(user_bank):  # 1. пополнение счета
    try:
        new_sum = float(input('Введите сумму для пополнения счета: '))
        if new_sum >= 10:
            user_bank += new_sum
        else:
            print('Сумма должна быть не менее 10 ..\n')
    except:
        print('Ошибка ввода суммы!')
    return user_bank


def make_purchase(user_bank, user_purchase):  # 2. покупка
    try:
        purchase_sum = float(input('Ввведите сумму покупки: '))
        if purchase_sum < 10:
            print('Стоимость покупки не может быть менее 10 ..')
        elif purchase_sum <= user_bank:
            user_bank -= purchase_sum
            purchase = input('Введите название покупки: ')
            user_purchase[purchase] = purchase_sum
        else:
            print('Денег не хватает!')
    except:
        print('Ошибка ввода суммы!')
    return user_bank, user_purchase


def user_history(user_bank, user_purchase):  # 3. история покупок
    if len(user_purchase) > 0:
        for key, val in user_purchase.items():
            print(f' - Стоимость {key} = {val}')
        print('Сделано покупок: ', len(user_purchase))
        average_check(user_purchase)
        bank_balance(user_bank)
        print()
    else:
        print('Еще не было покупок!')


def bank_balance(user_bank):  # 4. баланс
    info = f'💰 Остаток на счету: {user_bank}'
    print(info)
    return info


def average_check(user_purchase):  # 5. средний чек
    if len(user_purchase) > 0:
        info = f'🛒Средний чек = {round(sum(user_purchase.values()) / len(user_purchase), 1)}'
    else:
        info = 'Еще не было покупок!'
    print(info)
    return info


def my_bank():
    yes_no = True
    user_bank = 0.
    user_purchase = {}
    while yes_no:
        choice = choice_menu()
        if choice == '1':
            user_bank = bank_account(user_bank)
        elif choice == '2':
            user_bank, user_purchase = make_purchase(user_bank, user_purchase)
        elif choice == '3':
            user_histroy(user_bank, user_purchase)
        elif choice == '4':
            bank_balance(user_bank)
        elif choice == '5':
            average_check(user_purchase)
        elif choice == '0':
            yes_no = False
        else:
            print('Неверный пункт меню\n')

            
if __name__ == '__bank_account__':
    my_bank()
