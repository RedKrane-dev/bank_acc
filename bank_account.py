class BankAccount:
    def __init__(self, balance: int | float=0) -> None:
        self.__balance = balance


    def deposit(self, value: int | float) -> str:
        """
        Пополнение счета
        """
        try:
            if value > 0:
                self.__balance += value
                return f'Баланс пополнен на {value}'
            else:
                return 'Депозит должен быть больше "0"'
        except ValueError:
            return 'Ошибка. Не подходящий тип данных'


    def withdrawal(self, value: int | float) -> str:
        """
        Снятие со счета
        """
        try:
            if self.__balance >= value:
                self.__balance -= value
                return f'Выданы средства на сумму: {value}'
            else:
                return 'Недостаточно средств. Попробуйте изменить сумму'
        except ValueError:
            return 'Ошибка. Не подходящий тип данных'


    def get_balance(self) -> str:
        """
        Проверка баланса
        """
        return f'Ваш текущий баланс: {self.__balance}'
