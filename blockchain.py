import csv

# Beginning of blockchain
# Genesis block is placeholder for beginning of chain, holds proof of action
genesis = {'previous hash': 'none',
           'index': 0,
           'transactions': []}
blockchain = [genesis]
# List of open transactions
open_transactions = []


# Returns the last known block in the blockchain
#     if length is less than 1, returns default
#     otherwise, return last block
def get_last_node():
    if len(blockchain) > 0:
        return blockchain[-1]
    else:
        return [1]


# Adds a transaction with the following parameters:
#     sender: the address who initiated the transaction
#     recipient: the address who received the transaction
#     amount: amount send in the transaction
# end
def add_transaction(sender, recipient, amount=0.0):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)

    if len(open_transactions) > 9:
        mine_block()


# Research an algo for how blocks are mined
def mine_block():
    last_block = blockchain[-1]
    # Super simple hash algorithm for verification
    space_separated_keys = get_hash(last_block)
    current_block = {'previous hash': space_separated_keys,
                     'index': len(blockchain),
                     'transactions': open_transactions}
    blockchain.append(current_block)


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
    for current_block in blockchain:
        if current_block == blockchain[0]:
            if current_block['previous hash'] != 'none':
                print('invalid block')
        else:
            if current_block['previous hash'] != get_hash(blockchain[i - 1]):
                print('invalid block')
        i += 1
    print('block verified successfully!')


# Write data in the blockchain to a csv file
#     1. Prints each block in chain
#     2. Prints with headers, respectively: previous_hash, index, open_transactions
def write_to_csv():
    keys = blockchain[0].keys()
    with open('data.csv', 'w', newline='') as output:
        writer = csv.DictWriter(output, keys)
        writer.writeheader()
        writer.writerows(blockchain)


# Get user input for now and add it
received = get_transaction_values()
add_transaction(received[0], received[1], float(received[2]))
received = get_transaction_values()
mine_block()
add_transaction(received[0], received[1], float(received[2]))
mine_block()

# Printing debugs for testing format of transactions

# Printing entire blockchain
for node in blockchain:
    counter = 0
    for nodes in node:
        print(node[nodes])
    print(blockchain[counter])
    counter += 1
    verify_block()

write_to_csv()
