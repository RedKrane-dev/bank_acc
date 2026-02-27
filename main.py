from bank_account import BankAccount


def main(account):
    # Пополнение
    print(account.deposit(75_000))

    # Проверка баланса
    print(account.get_balance())

    # Снятие
    print(account.withdrawal(50_000))

    # Проверка баланса
    print(account.get_balance())

if __name__ == '__main__':
    bank_account = BankAccount(100_000)
    main(bank_account)
