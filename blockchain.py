# Beginning of blockchain, initializes list
blockchain = []
open_transactions = []


def get_last_node():
    return blockchain[-1]


def add_transaction(sender, recipient, amount=0.0):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_values():
    user_in = input('Enter sender, recipient, and value: ').split()
    return user_in


received = get_transaction_values()
add_transaction(received[0], received[1], received[2])

for block in open_transactions:
    print(block)
