from wallet import Wallet, Client

clients = [Client('Иванов', 50.0), Client('Петров', 100.0), Client('Сидоров', 3.50)]

wallets = Wallet(clients)

wallets.deposit_operation('Иванов', 40.0)
wallets.deposit_operation('Петров', 15.0, False)
wallets.deposit_operation('Сидоров', 20.67)

wallets.show_clients_deposit_info()