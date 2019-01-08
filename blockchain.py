blockchain = []


def get_last_node():
    return blockchain[-1]


def add_node(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_total = float(input("Please enter the transaction amount: "))
add_node(2)
add_node(last_transaction=get_last_node(), transaction_amount=0)
add_node(10.8, get_last_node())

print(blockchain)
