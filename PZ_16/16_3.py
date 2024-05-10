# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.
import pickle


class Bank:
    def __init__(self, balance, interest_rate, time_period, amount):
        self.balance = balance
        self.interest_rate = interest_rate
        self.time_period = time_period
        self.amount = amount

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100) * self.time_period
        return interest

    def withdraw(self):
        if self.amount > self.balance:
            raise ValueError("Недостаточно средств на балансе.")
        self.balance -= self.amount
        return self.balance


def save_def(they_bank, filename):
    with open(filename, 'wb') as f:
        pickle.dump(they_bank, f)


def load_def(filename):
    with open(filename, 'rb') as f:
        they_bank = pickle.load(f)
    return they_bank


bank1 = Bank(5000, 5.3, 4, 2000)
bank2 = Bank(6000, 5.5, 5, 3000)
bank3 = Bank(5000, 5.7, 6, 4000)
they_bank = [bank1, bank2, bank3]

save_def(they_bank, 'they_bank.pkl')
loaded_they_bank = load_def('they_bank.pkl')
for banks in loaded_they_bank:
    print(f"Начисленные проценты: {banks.calculate_interest():.2f} руб.")
    print("Новый баланс после снятия:", banks.withdraw())
    print()
