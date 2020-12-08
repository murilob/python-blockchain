# Initializing our blockchain list
genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Murilo'



def get_last_blockchain_value():
    """ returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new transaction

    Arguments:
        :sender: The sender of the coins
        :recepient: The receipient of the coins
        :amount: The amount of coins sent with the transaction
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    } #This is a dictionary structure. Holds key-pais values
      #keys are unique values

    open_transactions.append(transaction)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)

def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount) #returns a tuple


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
           continue
        if blockchain[block_index][0] == blockchain[block_index -1]:
           is_valid = True
        else:
           is_valid = False
           break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index -1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[1] = [2]
    elif user_choice == 'q':
        #break
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print('Invalid Blockchain!')
    #     break
else:
    print('User left') #execute after the loop finishes

print('Done!')
