class Wallet:
    def __init__(self, clients):
        self.clients = clients

    def deposit_operation(self, client_name, deposit, add=True):
        for client in self.clients:
            if client.name == client_name:
                client.balance += deposit if add else -deposit

    def show_clients_deposit_info(self):
        for client in self.clients:
            print(f'Клиент - «{client.name}». Баланс: {client.balance} руб.')


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = 0
        self.set_balance(balance)

    def set_balance(self, value):
        if isinstance(value, float):
            if value > 0:
                self.balance = value
            else:
                print('Баланс не может быть отрицательным')
        else:
            print('Не числовое значение')
