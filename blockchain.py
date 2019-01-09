# Beginning of blockchain, initializes list
blockchain = []


def get_last_node():
    return blockchain[-1]


def add_node(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_input():
    input_type = float(input("Please enter the transaction amount: "))
    return input_type


amount = get_input()
add_node(amount)

amount = get_input()
add_node(last_transaction=get_last_node(), transaction_amount=amount)

amount = get_input()
add_node(amount, get_last_node())

for node in blockchain:
    print('Outputting single block:')
    print(node)
