# Beginning of blockchain
# Genesis block is placeholder for beginning of chain, holds proof of action
genesis = {'previous hash': 'none',
           'index': 0,
           'transactions': []}
blockchain = [genesis]
# List of open transactions
open_transactions = []
owner = 'Owner'


# Returns the last known block in the blockchain
#     if length is less than 1, returns default
#     otherwise, return last block
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
    # Super simple hash algorithm for verification
    space_separated_keys = get_hash(last_block)
    current_block = {'previous hash': space_separated_keys,
                     'index': len(blockchain),
                     'transactions': open_transactions}

    blockchain.append(current_block)

    for node in current_block:
        print(current_block[node])


# Returns the allotted information given by the user
def get_transaction_values():
    user_in = input('Enter sender, recipient, and value: ').split()
    return user_in


# Very simple hash generation
#     1. Get all key/value pairs in dictionary
#     2. Separate them by a dash ('-')
#     3. Remove the extra dash at the end due to for loop
#     4. Return the calculated, but simple, hash
def get_hash(to_be_hashed):
    space_separated_keys = ''
    for keys in to_be_hashed:
        space_separated_keys += str(to_be_hashed[keys]) + '-'
    return space_separated_keys[:-1]


# Very simple verification method for previous blocks
#     1. Get 'previous hash' key/value from current block
#     2. Calculate actual hash from previous block
#     3. Compare the hashes
#     4. Successful or not <>?
def verify_block():
    i = 0
    for block in blockchain:
        if block == blockchain[0]:
            if block['previous hash'] != 'none':
                print('invalid block')
        else:
            if block['previous hash'] != get_hash(blockchain[i - 1]):
                print('invalid block')
        i += 1
    print('block verified successfully!')


# Get user input for now and add it
received = get_transaction_values()
add_transaction(received[0], received[1], float(received[2]))
received = get_transaction_values()
add_transaction(received[0], received[1], float(received[2]))

# Printing debugs for testing format of transactions
for block in open_transactions:
    mine_block()

# Printing entire blockchain
for node in blockchain:
    for nodes in node:
        print(node[nodes])
    verify_block()
