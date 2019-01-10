# Beginning of blockchain, initializes list
genesis = {'previous hash': '',
           'index': 0,
           'transactions': []}
blockchain = [genesis]
# List of open transactions
open_transactions = []
owner = 'Owner'


# Returns the last known block in the blockchain
def get_last_node():
    if len(blockchain) > 0:
        return blockchain[-1]
    else:
        return [1]


# Adds a transaction with the following parameters:
#     sender: the address who initated the transaction
#     recipient: the address who recieved the transaction
#     amount: amount send in the transaction
# end
def add_transaction(sender, recipient, amount=0.0):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


# Research an algo for how blocks are mined
def mine_block():
    last_block = blockchain[-1]
    space_separated_keys = ''
    for keys in last_block:
        space_separated_keys += str(last_block[keys]) + ' '
    block = {'previous hash': space_separated_keys,
             'index': len(blockchain),
             'transactions': open_transactions}
    blockchain.append(block)


# Returns the allotted information given by the user
def get_transaction_values():
    user_in = input('Enter sender, recipient, and value: ').split()
    return user_in


received = get_transaction_values()
add_transaction(received[0], received[1], float(received[2]))

for block in open_transactions:
    mine_block()

for node in blockchain:
    for nodes in node:
        print(node[nodes])
