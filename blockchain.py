# Beginning of blockchain, initializes list
blockchain = []
# List of open transactions
open_transactions = []


# Returns the last known block in the blockchain
def get_last_node():
    return blockchain[-1]


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
    pass


# Returns the alloted information given by the user
def get_transaction_values():
    user_in = input('Enter sender, recipient, and value: ').split()
    return user_in


received = get_transaction_values()
add_transaction(received[0], received[1], float(received[2]))

for block in open_transactions:
    print(block)
